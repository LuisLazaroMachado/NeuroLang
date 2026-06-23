import sys
from antlr4 import CommonTokenStream, FileStream
from gen.NeuroLangLexer import NeuroLangLexer
from gen.NeuroLangParser import NeuroLangParser
from semantic.semantic_visitor import SemanticVisitor
from codegen.tac_visitor import TACVisitor
from codegen.code_gen_visitor import CodeGenVisitor

def main():
    # 1. Leer el archivo fuente .nl
    entrada = FileStream(sys.argv[1], encoding="utf-8")

    # 2. Análisis léxico y sintáctico (ANTLR4)
    lexer  = NeuroLangLexer(entrada)
    tokens = CommonTokenStream(lexer)
    parser = NeuroLangParser(tokens)
    arbol  = parser.program()      # regla inicial

    if parser.getNumberOfSyntaxErrors() > 0:
        print('Errores sintácticos encontrados. Abortando.')
        return

    print('Análisis sintáctico: OK')

    # 3. Análisis semántico
    semantico = SemanticVisitor()
    semantico.visit(arbol)

    if semantico.errores:
        print('\n=== ERRORES SEMÁNTICOS ===')
        for e in semantico.errores:
            print(' ', e)
        sys.exit(1)

    print('Análisis semántico: OK')

    # 4. Generación de código de tres direcciones (3AC)
    tac_visitor = TACVisitor()
    tac_visitor.visit(arbol)
    codigo_tac = tac_visitor.tac.codigo()

    print('\n=== CÓDIGO DE TRES DIRECCIONES ===')
    print(codigo_tac)

    with open('salida.tac', 'w') as f:
        f.write(codigo_tac)

    # 5. Generación de código LLVM IR
    codegen = CodeGenVisitor()
    codegen.visit(arbol)
    codegen.finalizar()

    # 6. Guardar y mostrar el IR generado
    ir_texto = codegen.emitir("salida.ll")
    print('\n=== LLVM IR GENERADO ===')
    print(ir_texto)

# ejecutar main
main()
