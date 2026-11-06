import os
import subprocess
import sys
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent
MAIN = RAIZ / "main.py"
FUENTES = RAIZ / "tests"


def compilar(nombre, carpeta):
    return subprocess.run(
        [sys.executable, str(MAIN), str(FUENTES / nombre)],
        cwd=carpeta,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
    )


@pytest.mark.parametrize(
    "nombre, esperado",
    [
        ("pruebaErrorDuplicado.nl", "línea 2:8: Canal 'C3' ya declarado"),
        ("pruebaErrorNombreCruzado.nl", "línea 2:10: 'x' ya está declarado como canal"),
        ("pruebaErrorCanalComoUmbral.nl", "'C4' es un canal, se esperaba un umbral o un número"),
        ("pruebaErrorUmbralComoCanal.nl", "'alto' es un umbral, se esperaba un canal en signal(...)"),
    ],
)
def test_errores_semanticos_con_posicion(nombre, esperado, tmp_path):
    r = compilar(nombre, tmp_path)
    assert r.returncode == 1
    assert esperado in r.stdout
    assert not (tmp_path / "salida.tac").exists()
