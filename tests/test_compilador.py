import os
import subprocess
import sys
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent
MAIN = RAIZ / "main.py"
FUENTES = RAIZ / "tests"

VALIDOS = [
    "pruebaA.nl",
    "pruebaLetras.nl",
    "pruebaLetraNumero.nl",
    "pruebaLargo.nl",
]

TAC_PRUEBA_A = (
    "C3 = 0.0\n"
    "alto = 0.80\n"
    "t1 = C3 > alto\n"
    "if t1 goto L0_si else goto L0_fin\n"
    "L0_si:\n"
    '  output("A")\n'
    "  goto L0_fin\n"
    "L0_fin:"
)


def compilar(nombre, carpeta_trabajo):
    """Ejecuta main.py sobre tests/<nombre> con cwd en una carpeta temporal."""
    return subprocess.run(
        [sys.executable, str(MAIN), str(FUENTES / nombre)],
        cwd=carpeta_trabajo,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
    )


@pytest.mark.parametrize("nombre", VALIDOS)
def test_programa_valido_compila(nombre, tmp_path):
    r = compilar(nombre, tmp_path)
    assert r.returncode == 0, r.stderr
    assert "Análisis semántico: OK" in r.stdout
    assert (tmp_path / "salida.tac").exists()
    assert (tmp_path / "salida.ll").exists()


def test_tac_de_pruebaA(tmp_path):
    compilar("pruebaA.nl", tmp_path)
    assert (tmp_path / "salida.tac").read_text() == TAC_PRUEBA_A


def test_pruebaLargo_genera_16_outputs(tmp_path):
    compilar("pruebaLargo.nl", tmp_path)
    tac = (tmp_path / "salida.tac").read_text()
    assert tac.count("output(") == 16


@pytest.mark.parametrize(
    "nombre, mensaje",
    [
        ("pruebaErrorSemantico.nl", "Canal 'C3' usado pero no declarado"),
        ("pruebaErrorUmbral.nl", "Umbral 'alto' usado pero no declarado"),
    ],
)
def test_error_semantico(nombre, mensaje, tmp_path):
    r = compilar(nombre, tmp_path)
    assert r.returncode == 1
    assert mensaje in r.stdout
    assert not (tmp_path / "salida.tac").exists()


def test_error_sintactico(tmp_path):
    r = compilar("pruebaErrorEEG.nl", tmp_path)
    assert "Errores sintácticos" in r.stdout
    assert not (tmp_path / "salida.tac").exists()
