import sys
from antlr4 import CommonTokenStream, FileStream
from gen.NeuroLangLexer import NeuroLangLexer
from gen.NeuroLangParser import NeuroLangParser

def main():
    archivo = sys.argv[1]
    input_stream = FileStream(archivo, encoding='utf-8')
    lexer  = NeuroLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = NeuroLangParser(stream)
    tree   = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print('Errores sintácticos encontrados.')
    else:
        print('Análisis sintáctico: OK')
        print(tree.toStringTree(recog=parser))

main()
