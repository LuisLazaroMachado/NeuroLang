FILENAME = NeuroLang.g4
# Derivamos el nombre base quitando la extensión .g4
PREFIX = $(basename $(FILENAME))
CC = clang-18

all:
	java -jar /usr/local/lib/antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor $(FILENAME) -o gen/

# Corre solo el front end + back end (genera salida.tac y salida.ll), sin producir ejecutable
run:
	python3 main.py $(FILE)

# Pipeline completo: .nl -> salida.ll -> ejecutable nativo
# Uso: make build FILE=tests/pruebaA.nl
build: run
	$(CC) salida.ll -o programa

# Corre el ejecutable ya compilado alimentándolo con señales simuladas
# Uso: make demo FILE=tests/pruebaA.nl INPUT=tests/inputs/pruebaA.txt
demo: build
	./programa < $(INPUT)

# Corre toda la batería de pruebas (léxicas/sintácticas, semánticas y funcionales)
test:
	python3 tests/run_tests.py

clean:
	rm -f gen/$(PREFIX)*.py gen/$(PREFIX)*.tokens gen/$(PREFIX)*.interp
	rm -f salida.tac salida.ll programa
	rm -rf build/
	rm -rf gen/__pycache__ semantic/__pycache__ codegen/__pycache__
