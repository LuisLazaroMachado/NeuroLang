from .TACEmitter import TACEmitter
from gen.NeuroLangVisitor import NeuroLangVisitor

class TACVisitor(NeuroLangVisitor):
    """Genera código de tres direcciones (3AC) para NeuroLang."""

    def __init__(self):
        self.tac = TACEmitter()

    # -- channel C3 : eeg;
    def visitChannelDecl(self, ctx):
        nombre = ctx.ID().getText()
        # declarar canal con valor inicial 0.0
        self.tac.emitir_copia(nombre, "0.0")

    # -- threshold alto : 0.80;
    def visitThresholdDecl(self, ctx):
        nombre = ctx.ID().getText()
        valor  = ctx.NUMBER().getText()
        # declarar umbral con su valor
        self.tac.emitir_copia(nombre, valor)

    # -- when signal(C3) > alto { output("A"); }
    def visitWhenStmt(self, ctx):
        canal  = ctx.signal().ID().getText()
        op     = ctx.RELOP().getText()

        # obtener el umbral o valor de la expresión
        expr = ctx.expression()
        if expr.NUMBER():
            umbral = expr.NUMBER().getText()
        else:
            umbral = expr.ID().getText()

        # generar temporal para la comparación
        temp = self.tac.nuevo_temp()
        self.tac.emitir(f"{temp} = {canal} {op} {umbral}")

        # generar etiquetas para el bloque if/fin
        etq_num = self.tac._etiqueta
        lsi  = f"L{etq_num}_si"
        lfin = f"L{etq_num}_fin"
        self.tac._etiqueta += 1

        # salto condicional
        self.tac.emitir(f"if {temp} goto {lsi} else goto {lfin}")

        # bloque verdadero
        self.tac.emitir(f"{lsi}:")
        for out in ctx.outputStmt():
            self.visit(out)
        self.tac.emitir(f"  goto {lfin}")

        # bloque fin
        self.tac.emitir(f"{lfin}:")

    # -- output("A");
    def visitOutputStmt(self, ctx):
        texto = ctx.STRING_LIT().getText()  # incluye comillas
        self.tac.emitir(f"  output({texto})")
