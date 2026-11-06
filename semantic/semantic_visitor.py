from gen.NeuroLangVisitor import NeuroLangVisitor


class SemanticVisitor(NeuroLangVisitor):
    def __init__(self):
        self.canales = {}    # nombre -> tipo de señal (eeg, emg, eog)
        self.umbrales = {}   # nombre -> valor numérico
        self.errores = []    # errores semánticos con línea:columna

    def _error(self, token, mensaje):
        self.errores.append(f"línea {token.line}:{token.column}: {mensaje}")

    # -- channel C3 : eeg;
    def visitChannelDecl(self, ctx):
        tok = ctx.ID().getSymbol()
        nombre = tok.text
        if nombre in self.canales:
            self._error(tok, f"Canal '{nombre}' ya declarado")
        elif nombre in self.umbrales:
            self._error(tok, f"'{nombre}' ya está declarado como umbral")
        else:
            self.canales[nombre] = ctx.signalType().getText()

    # -- threshold alto : 0.80;
    def visitThresholdDecl(self, ctx):
        tok = ctx.ID().getSymbol()
        nombre = tok.text
        if nombre in self.umbrales:
            self._error(tok, f"Umbral '{nombre}' ya declarado")
        elif nombre in self.canales:
            self._error(tok, f"'{nombre}' ya está declarado como canal")
        else:
            self.umbrales[nombre] = float(ctx.NUMBER().getText())

    # -- when signal(C3) > alto { output("A"); }
    def visitWhenStmt(self, ctx):
        tok = ctx.signal().ID().getSymbol()
        canal = tok.text
        if canal not in self.canales:
            if canal in self.umbrales:
                self._error(tok, f"'{canal}' es un umbral, se esperaba un canal en signal(...)")
            else:
                self._error(tok, f"Canal '{canal}' usado pero no declarado")

        expr = ctx.expression()
        if expr.ID():
            tok = expr.ID().getSymbol()
            nombre = tok.text
            if nombre not in self.umbrales:
                if nombre in self.canales:
                    self._error(tok, f"'{nombre}' es un canal, se esperaba un umbral o un número")
                else:
                    self._error(tok, f"Umbral '{nombre}' usado pero no declarado")

        for out in ctx.outputStmt():
            self.visit(out)

    def visitOutputStmt(self, ctx):
        pass  # nada que verificar semánticamente en output("A")
