# NeuroLang

Lenguaje de programación de alto nivel para describir interfaces
cerebro-computadora (BCI): declara canales de electrodos, umbrales de
activación, y reglas `when` que traducen señales cerebrales en símbolos
de salida (letras, números, palabras).

Ejemplo:

```
channel C3 : eeg;
threshold alto : 0.80;
when signal(C3) > alto { output("A"); }
```

## Arquitectura del compilador

NeuroLang se implementa como un compilador clásico de varias fases,
usando **ANTLR4** para el front end y **LLVM (vía llvmlite)** para el
back end:

```
 archivo .nl
     │
     ▼
┌─────────────────────┐
│  Lexer (ANTLR4)      │  gen/NeuroLangLexer.py
│  Parser (ANTLR4)     │  gen/NeuroLangParser.py
└─────────────────────┘
     │  árbol de sintaxis (parse tree)
     ▼
┌─────────────────────┐
│  Análisis semántico   │  semantic/semantic_visitor.py
│  (tabla de símbolos:  │  - valida canales/umbrales declarados una sola vez
│   canales, umbrales)  │  - valida que todo `when` use símbolos ya declarados
└─────────────────────┘
     │  árbol validado
     ▼
┌─────────────────────┐
│  Generación de TAC    │  codegen/tac_visitor.py + TACEmitter.py
│  (3 direcciones)      │  - representación intermedia legible, con
└─────────────────────┘    temporales, etiquetas y saltos
     │
     ▼
┌─────────────────────┐
│  Generación LLVM IR   │  codegen/code_gen_visitor.py
│  (llvmlite)           │  - declara canales como memoria (alloca)
└─────────────────────┘    - construye el bucle de lectura de señales
     │  salida.ll             - traduce cada `when` a un if/branch
     ▼
┌─────────────────────┐
│  clang (LLVM backend) │  compila salida.ll -> ejecutable nativo
└─────────────────────┘
     │
     ▼
 ejecutable (`programa`)
```

`main.py` orquesta las fases en orden: lexer → parser → semántico → TAC
→ LLVM IR. Si el análisis sintáctico o semántico encuentra errores, el
proceso se detiene ahí y no llega a generar código.

### Cómo se simulan las señales cerebrales

El caso de uso real (un paciente generando señales EEG que cambian en
el tiempo) requiere que el programa reaccione a **valores que varían**,
no a una señal fija. Por eso el ejecutable generado no evalúa los
`when` una sola vez: en su lugar, `main` arma un bucle que en cada
iteración:

1. Lee, con `scanf`, un valor `double` por cada canal declarado (en el
   mismo orden en que se declararon con `channel`), desde `stdin`.
2. Si logró leer un valor para cada canal, evalúa **todas** las
   sentencias `when` contra los valores recién leídos y vuelve a
   iterar.
3. Si `scanf` no pudo leer un valor completo (fin de archivo o dato
   inválido), termina el programa.

Esto permite simular una sesión completa (por ejemplo, deletrear una
palabra letra por letra) alimentando el binario con un archivo de
texto donde cada línea representa una "lectura" simultánea de todos
los canales:

```
0.90 0.10   <- primera lectura: C3=0.90, C4=0.10
0.10 0.90   <- segunda lectura: C3=0.10, C4=0.90
```

Nota de diseño: cada `when` es independiente y no hay `elif`/exclusión
mutua entre umbrales del mismo canal. Si una señal supera varios
umbrales a la vez (p. ej. `0.90` supera `alto`, `medio` y `bajo`), se
disparan **todos** los `output` correspondientes. Es un comportamiento
intencional para esta etapa (mantiene la gramática simple), documentado
aquí para que se entienda al leer las salidas de las pruebas.

## Estructura del repositorio

```
NeuroLang.g4              gramática ANTLR4
gen/                       lexer/parser/visitor generados por ANTLR (ver `make all`)
semantic/semantic_visitor.py   análisis semántico (tabla de símbolos)
codegen/tac_visitor.py         generación de código de 3 direcciones
codegen/TACEmitter.py          helper de emisión de TAC
codegen/code_gen_visitor.py    generación de LLVM IR (llvmlite)
main.py                        driver: corre las 4 fases sobre un .nl
tests/*.nl                      programas de prueba (válidos y con error)
tests/inputs/*.txt               señales simuladas para las pruebas funcionales
tests/esperado/*.txt             salida esperada de cada prueba funcional
tests/run_tests.py                script de validación automatizada
Makefile                        atajos de build
```

## Requisitos

- Java (para ANTLR4, solo si vas a regenerar `gen/` con `make all`)
- Python 3.10+
- `pip install antlr4-python3-runtime==4.13.1 llvmlite`
- `clang` (para compilar el `.ll` a ejecutable nativo; en Ubuntu:
  `sudo apt-get install clang-18`)

## Uso

```bash
# Solo front end + back end: genera salida.tac y salida.ll
make run FILE=tests/pruebaA.nl

# Pipeline completo: genera además el ejecutable nativo `programa`
make build FILE=tests/pruebaA.nl

# Compila y corre el ejecutable con señales simuladas desde un archivo
make demo FILE=tests/pruebaA.nl INPUT=tests/inputs/pruebaA.txt

# Corre toda la batería de pruebas (sintácticas, semánticas y funcionales)
make test
```

## Plan de validación

Las pruebas se organizan en tres categorías, todas automatizadas en
`tests/run_tests.py`:

| Categoría | Qué valida | Casos |
|---|---|---|
| Léxico/sintáctico | El parser rechaza tokens o construcciones inválidas | `pruebaErrorEEG.nl` (tipo de señal inexistente `eg`) |
| Semántico | La tabla de símbolos detecta canales/umbrales usados sin declarar | `pruebaErrorSemantico.nl`, `pruebaErrorUmbral.nl` |
| Funcional (end-to-end) | El ejecutable, alimentado con señales simuladas, produce exactamente la secuencia de símbolos esperada | `pruebaA.nl`, `pruebaPequena.nl`, `pruebaLetras.nl`, `pruebaLetraNumero.nl`, `pruebaLargo.nl` |

Para cada caso funcional, `tests/inputs/<caso>.txt` contiene las
señales simuladas (una lectura por línea, un valor por canal en orden
de declaración) y `tests/esperado/<caso>.txt` contiene la salida exacta
que el ejecutable debe producir. `run_tests.py` compila cada caso,
genera el ejecutable con `clang`, lo corre con su entrada simulada, y
compara la salida real contra la esperada carácter por carácter.

Resultado actual: **8/8 pruebas pasan** (`make test`).
