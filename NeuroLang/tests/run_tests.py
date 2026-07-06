#!/usr/bin/env python3
"""
Ejecuta el plan de validación de NeuroLang de forma automática.

Tres categorías de prueba:
  1. syntax_error   -> se espera que el análisis sintáctico falle
  2. semantic_error -> se espera que el análisis semántico reporte errores
  3. functional     -> se espera que el binario compilado, alimentado con
                        señales simuladas (tests/inputs/<nombre>.txt),
                        produzca exactamente la salida esperada
                        (tests/esperado/<nombre>.txt)

Uso:
    python3 tests/run_tests.py
"""

import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TESTS_DIR = RAIZ / "tests"
INPUTS_DIR = TESTS_DIR / "inputs"
ESPERADO_DIR = TESTS_DIR / "esperado"
BUILD_DIR = RAIZ / "build"

CASOS = {
    # nombre: categoria
    "pruebaErrorEEG":        "syntax_error",
    "pruebaErrorSemantico":  "semantic_error",
    "pruebaErrorUmbral":     "semantic_error",
    "pruebaA":               "functional",
    "pruebaPequena":         "functional",
    "pruebaLetras":          "functional",
    "pruebaLetraNumero":     "functional",
    "pruebaLargo":           "functional",
}


def correr_main(nombre_nl):
    """Corre main.py sobre tests/<nombre>.nl y devuelve (returncode, stdout, stderr)."""
    ruta = TESTS_DIR / f"{nombre_nl}.nl"
    resultado = subprocess.run(
        [sys.executable, "main.py", str(ruta)],
        cwd=RAIZ, capture_output=True, text=True,
    )
    return resultado.returncode, resultado.stdout, resultado.stderr


def probar_syntax_error(nombre):
    code, out, err = correr_main(nombre)
    ok = "Errores sintácticos encontrados" in out
    return ok, out + err


def probar_semantic_error(nombre):
    code, out, err = correr_main(nombre)
    ok = "ERRORES SEMÁNTICOS" in out and code == 1
    return ok, out + err


def probar_functional(nombre):
    # 1. Compilar el .nl -> salida.ll (vía el pipeline completo)
    code, out, err = correr_main(nombre)
    if code != 0 or "LLVM IR GENERADO" not in out:
        return False, f"Fallo en la compilación:\n{out}\n{err}"

    # 2. Compilar salida.ll -> ejecutable con clang
    BUILD_DIR.mkdir(exist_ok=True)
    binario = BUILD_DIR / nombre
    r = subprocess.run(
        ["clang-18", str(RAIZ / "salida.ll"), "-o", str(binario)],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        return False, f"Fallo al compilar el .ll con clang:\n{r.stderr}"

    # 3. Ejecutar con las señales simuladas y comparar con lo esperado
    entrada = INPUTS_DIR / f"{nombre}.txt"
    esperado = (ESPERADO_DIR / f"{nombre}.txt").read_text()
    with open(entrada) as f_in:
        r = subprocess.run([str(binario)], stdin=f_in, capture_output=True, text=True)

    if r.stdout != esperado:
        return False, f"Salida distinta.\n--- esperado ---\n{esperado}--- obtenido ---\n{r.stdout}"
    return True, "OK"


DISPATCH = {
    "syntax_error": probar_syntax_error,
    "semantic_error": probar_semantic_error,
    "functional": probar_functional,
}


def main():
    total = 0
    fallidos = 0
    for nombre, categoria in CASOS.items():
        total += 1
        ok, detalle = DISPATCH[categoria](nombre)
        estado = "PASA" if ok else "FALLA"
        print(f"[{estado}] {nombre:25s} ({categoria})")
        if not ok:
            fallidos += 1
            print("   " + detalle.replace("\n", "\n   "))

    print(f"\n{total - fallidos}/{total} pruebas pasaron.")
    sys.exit(1 if fallidos else 0)


if __name__ == "__main__":
    main()
