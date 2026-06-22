from llvmlite import ir
from gen.NeuroLangVisitor import NeuroLangVisitor

class CodeGenVisitor(NeuroLangVisitor):
    def __init__(self):
        # Tipos de datos LLVM que usaremos
        self.i32 = ir.IntType(32)       # entero 32 bits (para printf y main)
        self.i8  = ir.IntType(8)        # carácter (para strings)
        self.f64 = ir.DoubleType()      # flotante 64 bits (para señales y umbrales)

        # Módulo: contenedor principal de todo el IR generado
        self.module = ir.Module(name="neurolang")
        self.module.triple = "x86_64-pc-linux-gnu"  # arquitectura destino: Linux 64 bits

        # Declarar printf (función externa de C para imprimir)
        # Recibe un puntero a char (i8*) y argumentos variables
        printf_tipo = ir.FunctionType(
            self.i32,
            [ir.PointerType(self.i8)],
            var_arg=True
        )
        self.printf = ir.Function(self.module, printf_tipo, name="printf")

        # Cadena de formato "%s\n" para imprimir strings con salto de línea
        fmt = bytearray(b"%s\n\0")                          # \0 = terminador de cadena en C
        fmt_tipo = ir.ArrayType(self.i8, len(fmt))
        self.fmt_global = ir.GlobalVariable(self.module, fmt_tipo, name="fmt")
        self.fmt_global.global_constant = True
        self.fmt_global.initializer = ir.Constant(fmt_tipo, fmt)

        # Crear la función main: punto de entrada del programa
        main_tipo = ir.FunctionType(self.i32, [])
        self.main_func = ir.Function(self.module, main_tipo, name="main")
        bloque = self.main_func.append_basic_block("entry") # bloque de entrada
        self.builder = ir.IRBuilder(bloque)                 # builder: inserta instrucciones

        # Tablas de símbolos
        self.canales  = {}  # canal  → puntero alloca (f64 en memoria)
        self.umbrales = {}  # umbral → constante f64
        self.strings  = {}  # texto  → variable global de string

    # -- Helpers --
    def _get_string(self, texto):
        """Crea o reutiliza una variable global para un string literal."""
        if texto in self.strings:
            return self.strings[texto]
        encoded = bytearray((texto + "\0").encode("utf-8"))  # codifica a bytes con \0 final
        s_tipo  = ir.ArrayType(self.i8, len(encoded))
        gvar    = ir.GlobalVariable(self.module, s_tipo,
                                    name=f"str_{len(self.strings)}")
        gvar.global_constant = True
        gvar.initializer     = ir.Constant(s_tipo, encoded)
        self.strings[texto]  = gvar
        return gvar

    def _ptr_to_str(self, gvar):
        """Obtiene puntero i8* al primer carácter del string global (para printf)."""
        cero = ir.Constant(self.i32, 0)
        return self.builder.gep(gvar, [cero, cero], name="sptr")  # GEP: aritmética de punteros

    # -- channel C3 : eeg;
    def visitChannelDecl(self, ctx):
        nombre = ctx.ID().getText()
        ptr = self.builder.alloca(self.f64, name=nombre)        # reserva espacio en stack
        self.builder.store(ir.Constant(self.f64, 0.0), ptr)     # inicializa en 0.0
        self.canales[nombre] = ptr                               # guarda puntero en tabla

    # -- threshold alto : 0.80;
    def visitThresholdDecl(self, ctx):
        nombre = ctx.ID().getText()
        valor  = float(ctx.NUMBER().getText())
        self.umbrales[nombre] = ir.Constant(self.f64, valor)    # guarda constante f64

    # -- when signal(C3) > alto { output("A"); }
    def visitWhenStmt(self, ctx):
        # 1. Leer el valor actual del canal desde memoria
        canal = ctx.signal().ID().getText()
        ptr   = self.canales[canal]
        val   = self.builder.load(ptr, name=canal + "_val")     # load: lee el valor del canal

        # 2. Obtener el umbral de comparación
        expr = ctx.expression()
        if expr.NUMBER():
            umbral_val = ir.Constant(self.f64, float(expr.NUMBER().getText()))
        else:
            umbral_val = self.umbrales[expr.ID().getText()]     # busca en tabla de umbrales

        # 3. Comparación flotante: signal RELOP umbral
        op = ctx.RELOP().getText()
        cmp_map = {
            '>'  : 'ogt',   # ordered greater than
            '<'  : 'olt',   # ordered less than
            '>=' : 'oge',   # ordered greater or equal
            '<=' : 'ole',   # ordered less or equal
            '==' : 'oeq',   # ordered equal
            '!=' : 'one',   # ordered not equal
        }
        cond = self.builder.fcmp_ordered(cmp_map[op], val, umbral_val, name="cond")

        # 4. Crear bloques básicos para el if/merge (estructura de flujo de control)
        bloque_si  = self.main_func.append_basic_block("cuando_si")   # bloque verdadero
        bloque_fin = self.main_func.append_basic_block("cuando_fin")  # bloque de salida
        self.builder.cbranch(cond, bloque_si, bloque_fin)             # salto condicional

        # 5. Bloque verdadero: ejecutar los output()
        self.builder.position_at_end(bloque_si)
        for out in ctx.outputStmt():
            self.visit(out)
        self.builder.branch(bloque_fin)     # salto incondicional al bloque de salida

        # 6. Continuar construyendo desde el bloque de salida
        self.builder.position_at_end(bloque_fin)

    # -- output("A");
    def visitOutputStmt(self, ctx):
        texto  = ctx.STRING_LIT().getText()[1:-1]   # quita las comillas del string
        gvar   = self._get_string(texto)            # obtiene o crea el string global
        sptr   = self._ptr_to_str(gvar)             # puntero i8* para printf
        cero   = ir.Constant(self.i32, 0)
        fmtptr = self.builder.gep(self.fmt_global, [cero, cero], name="fptr")
        self.builder.call(self.printf, [fmtptr, sptr])  # llama a printf("%s\n", texto)

    # -- Finalizar: agrega ret i32 0 al final de main
    def finalizar(self):
        self.builder.ret(ir.Constant(self.i32, 0))

    def emitir(self, archivo="salida.ll"):
        """Convierte el módulo a texto IR y lo guarda en un archivo .ll"""
        ir_texto = str(self.module)
        with open(archivo, "w") as f:
            f.write(ir_texto)
        return ir_texto
