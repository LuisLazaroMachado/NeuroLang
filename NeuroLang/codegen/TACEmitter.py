class TACEmitter:
    """Generador de código de tres direcciones (Three-Address Code)."""

    def __init__(self):
        self._contador     = 0   # contador de temporales
        self._etiqueta     = 0   # contador de etiquetas
        self._instrucciones = [] # lista de instrucciones 3AC

    def nuevo_temp(self) -> str:
        """Devuelve el nombre del siguiente temporal: t1, t2, ..."""
        self._contador += 1
        return f"t{self._contador}"

    def nueva_etiqueta(self, prefijo: str) -> str:
        """Devuelve una etiqueta única: L0_si, L0_fin, L1_si, ..."""
        self._etiqueta += 1
        return f"L{self._etiqueta}_{prefijo}"

    def emitir(self, instruccion: str) -> None:
        """Registra una instrucción 3AC en texto libre."""
        self._instrucciones.append(instruccion)

    def emitir_copia(self, dest: str, src: str) -> None:
        """Registra: dest = src"""
        self._instrucciones.append(f"{dest} = {src}")

    def codigo(self) -> str:
        """Devuelve todas las instrucciones 3AC como texto."""
        return "\n".join(self._instrucciones)
