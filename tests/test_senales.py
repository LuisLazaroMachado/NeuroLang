import os
import subprocess
import sys
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent
MAIN = RAIZ / "main.py"
FUENTES = RAIZ / "tests"


def compilar(nombre, carpeta, *extra):
    return subprocess.run(
        [sys.executable, str(MAIN), str(FUENTES / nombre), *extra],
        cwd=carpeta,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
    )


def ejecucion(stdout):
    return stdout.split("=== EJECUCIÓN ===")[1].split()


@pytest.mark.parametrize(
    "valor, esperado",
    [("0.85", ["A", "B", "C"]), ("0.5", ["C"]), ("0.3", [])],
)
def test_run_con_senal(valor, esperado, tmp_path):
    r = compilar("pruebaLetras.nl", tmp_path, "--signal", f"C3={valor}", "--run")
    assert r.returncode == 0, r.stderr
    assert ejecucion(r.stdout) == esperado


def test_sin_signal_nada_se_activa(tmp_path):
    r = compilar("pruebaLargo.nl", tmp_path, "--run")
    assert ejecucion(r.stdout) == []


def test_dos_canales(tmp_path):
    r = compilar("pruebaLargo.nl", tmp_path,
                 "--signal", "C3=0.85", "--signal", "C4=0.7", "--run")
    assert ejecucion(r.stdout) == ["B", "C", "D", "G", "H"]


def test_senal_se_refleja_en_tac(tmp_path):
    compilar("pruebaA.nl", tmp_path, "--signal", "C3=0.85")
    assert "C3 = 0.85" in (tmp_path / "salida.tac").read_text()


def test_canal_inexistente(tmp_path):
    r = compilar("pruebaA.nl", tmp_path, "--signal", "Z9=1")
    assert r.returncode == 1
    assert "canal 'Z9' no declarado" in r.stdout


def test_valor_invalido(tmp_path):
    r = compilar("pruebaA.nl", tmp_path, "--signal", "C3=abc")
    assert r.returncode == 1
