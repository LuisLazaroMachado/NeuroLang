# NeuroLang

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
| Semántico (canales y umbrales declarados, sin duplicados) | `semantic/semantic_visitor.py` |
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

### Errores semánticos

`tests/pruebaErrorSemantico.nl` y `tests/pruebaErrorUmbral.nl` usan un canal o umbral sin declarar y terminan con un mensaje de error.

## Regenerar el parser

Solo si modificas `NeuroLang.g4` (requiere Java y el jar de ANTLR 4.13.1):

```powershell
java -jar <ruta>\antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor NeuroLang.g4 -o gen/
```

## Limitaciones actuales

- Los canales se inicializan en `0.0` y el lenguaje no define cómo recibir valores de señal, por lo que las reglas `when` con umbrales positivos no se activan.
- El tipo de señal (`eeg`, `emg`, `eog`) se valida sintácticamente pero no influye en el análisis semántico ni en la generación de código.
