# NeuroLang

[![CI](https://github.com/LuisLazaroMachado/NeuroLang/actions/workflows/ci.yml/badge.svg)](https://github.com/LuisLazaroMachado/NeuroLang/actions/workflows/ci.yml)

Compilador de un lenguaje de dominio específico (DSL) para definir reglas de umbral sobre señales biomédicas (EEG, EMG, EOG). Recorre todas las fases de un compilador: análisis léxico y sintáctico (ANTLR4), análisis semántico, código de tres direcciones (3AC) y generación de LLVM IR.

## El lenguaje

```
channel C3 : eeg;
threshold alto : 0.80;
when signal(C3) > alto { output("A"); }
```

- `channel <ID> : eeg | emg | eog;` declara un canal.
- `threshold <ID> : <número>;` declara un umbral.
- `when signal(<canal>) <op> <umbral|número> { output("..."); }` ejecuta los `output` si se cumple la condición. Operadores: `> < >= <= == !=`.

La gramática completa está en [`NeuroLang.g4`](NeuroLang.g4).

## Pipeline

| Fase | Archivo |
|---|---|
| Léxico y sintáctico | `NeuroLang.g4` → `gen/` (generado con ANTLR 4.13.1) |
| Semántico (declaración previa, sin duplicados ni nombres cruzados canal/umbral; errores con línea:columna) | `semantic/semantic_visitor.py` |
| Código de tres direcciones | `codegen/tac_visitor.py`, `codegen/TACEmitter.py` |
| LLVM IR | `codegen/code_gen_visitor.py` (usa `llvmlite`) |

## Uso (Windows, PowerShell)

Requiere Python 3.12 (versión con la que se probó).

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py tests\pruebaA.nl
```

Escribe `salida.tac` y `salida.ll` en el directorio actual.

### Ejemplo

Entrada: `tests/pruebaA.nl`. Salida 3AC:

```
C3 = 0.0
alto = 0.80
t1 = C3 > alto
if t1 goto L0_si else goto L0_fin
L0_si:
  output("A")
  goto L0_fin
L0_fin:
```

### Valores de señal y ejecución

El lenguaje no lee señales en ejecución: el valor inicial de cada canal se fija al compilar (por defecto `0.0`).

```powershell
python main.py tests\pruebaLetras.nl --signal C3=0.85 --run
```

`--run` ejecuta el código de tres direcciones e imprime los `output` que se activan (aquí: `A`, `B`, `C`).

### Errores semánticos

`tests/pruebaErrorSemantico.nl` y `tests/pruebaErrorUmbral.nl` usan un canal o umbral sin declarar y terminan con un mensaje de error.

## Tests

```powershell
pip install -r requirements-dev.txt
pytest -v
```

La suite compila los programas de `tests/` y comprueba el código de tres direcciones, la ejecución con `--signal` y los errores sintácticos y semánticos. Se ejecuta automáticamente en GitHub Actions en cada push.

## Regenerar el parser

Solo si modificas `NeuroLang.g4` (requiere Java y el jar de ANTLR 4.13.1):

```powershell
java -jar <ruta>\antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor NeuroLang.g4 -o gen/
```

## Limitaciones actuales

- Los valores de señal no se leen en ejecución: se fijan al compilar con `--signal CANAL=VALOR` (por defecto `0.0`).
- El tipo de señal (`eeg`, `emg`, `eog`) se registra en la tabla de símbolos, pero el lenguaje aún no define reglas que dependan de él.
