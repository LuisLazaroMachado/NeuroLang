"""Intérprete mínimo del código de tres direcciones (3AC) de NeuroLang."""
import operator
import re

NUM = re.compile(r"^-?\d+(\.\d+)?([eE][-+]?\d+)?$")
SALIDA = re.compile(r'^output\("(.*)"\)$')
CMP = re.compile(r"^(\w+) = (\S+) (>=|<=|==|!=|>|<) (\S+)$")
COPIA = re.compile(r"^(\w+) = (\S+)$")
SALTO = re.compile(r"^if (\w+) goto (\w+) else goto (\w+)$")
GOTO = re.compile(r"^goto (\w+)$")
ETIQ = re.compile(r"^(\w+):$")

OPS = {
    ">": operator.gt, "<": operator.lt, ">=": operator.ge,
    "<=": operator.le, "==": operator.eq, "!=": operator.ne,
}


def ejecutar_tac(codigo):
    """Ejecuta el 3AC y devuelve la lista de textos emitidos por output()."""
    lineas = [l.strip() for l in codigo.splitlines() if l.strip()]
    etiquetas = {}
    for i, l in enumerate(lineas):
        m = ETIQ.match(l)
        if m:
            etiquetas[m.group(1)] = i

    env = {}

    def valor(tok):
        return float(tok) if NUM.match(tok) else env[tok]

    salida = []
    pc = 0
    while pc < len(lineas):
        l = lineas[pc]
        pc += 1
        if ETIQ.match(l):
            continue
        if m := SALIDA.match(l):
            salida.append(m.group(1))
        elif m := CMP.match(l):
            env[m.group(1)] = OPS[m.group(3)](valor(m.group(2)), valor(m.group(4)))
        elif m := COPIA.match(l):
            env[m.group(1)] = valor(m.group(2))
        elif m := SALTO.match(l):
            pc = etiquetas[m.group(2) if env[m.group(1)] else m.group(3)]
        elif m := GOTO.match(l):
            pc = etiquetas[m.group(1)]
        else:
            raise ValueError(f"Instrucción 3AC no reconocida: {l}")
    return salida
