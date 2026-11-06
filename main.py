import argparse
import sys

from antlr4 import CommonTokenStream, FileStream
from gen.NeuroLangLexer import NeuroLangLexer
from gen.NeuroLangParser import NeuroLangParser
from semantic.semantic_visitor import SemanticVisitor
from codegen.tac_visitor import TACVisitor
from codegen.code_gen_visitor import CodeGenVisitor
from codegen.tac_interprete import ejecutar_tac


def parsear_senales(items):
    senales = {}
    for item in items:
        nombre, _, valor = item.partition("=")
        try:
            senales[nombre] = float(valor)
        except ValueError:
            sys.exit(f"Error: --signal espera CANAL=VALOR, recibido '{item}'")
    return senales


def main():
    ap = argparse.ArgumentParser(description="Compilador NeuroLang")
    ap.add_argument("archivo", help="programa fuente .nl")
    ap.add_argument("--signal", action="append", default=[], metavar="CANAL=VALOR",
                    help="valor del canal (repetible); por defecto 0.0")
    ap.add_argument("--run", action="store_true",
                    help="ejecuta el 3AC e imprime los output()")
    args = ap.parse_args()
    senales = parsear_senales(args.signal)

    # 1. Leer el archivo fuente .nl
    entrada = FileStream(args.archivo, encoding="utf-8")

    # 2. Análisis léxico y sintáctico (ANTLR4)
    lexer = NeuroLangLexer(entrada)
    tokens = CommonTokenStream(lexer)
    parser = NeuroLangParser(tokens)
    arbol = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print('Errores sintácticos encontrados. Abortando.')
        sys.exit(1)

    print('Análisis sintáctico: OK')

    # 3. Análisis semántico
    semantico = SemanticVisitor()
    semantico.visit(arbol)

    if semantico.errores:
        print('\n=== ERRORES SEMÁNTICOS ===')
        for e in semantico.errores:
            print(' ', e)
        sys.exit(1)

    desconocidos = [n for n in senales if n not in semantico.canales]
    if desconocidos:
        print('\n=== ERRORES ===')
        for n in desconocidos:
            print(f"  --signal: canal '{n}' no declarado en el programa")
        sys.exit(1)

    print('Análisis semántico: OK')

    # 4. Código de tres direcciones (3AC)
    tac_visitor = TACVisitor(senales)
    tac_visitor.visit(arbol)
    codigo_tac = tac_visitor.tac.codigo()

    print('\n=== CÓDIGO DE TRES DIRECCIONES ===')
    print(codigo_tac)

    with open('salida.tac', 'w', encoding='utf-8') as f:
        f.write(codigo_tac)

    # 5. LLVM IR
    codegen = CodeGenVisitor(senales)
    codegen.visit(arbol)
    codegen.finalizar()

    ir_texto = codegen.emitir("salida.ll")
    print('\n=== LLVM IR GENERADO ===')
    print(ir_texto)

    # 6. Ejecución opcional del 3AC
    if args.run:
        print('\n=== EJECUCIÓN ===')
        for linea in ejecutar_tac(codigo_tac):
            print(linea)


if __name__ == "__main__":
    main()
