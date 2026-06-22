from gen.NeuroLangVisitor import NeuroLangVisitor

class SemanticVisitor(NeuroLangVisitor):
    def __init__(self):
        self.canales  = set()  # nombres de canales declarados con 'channel'
        self.umbrales = set()  # nombres de umbrales declarados con 'threshold'
        self.errores  = []     # lista de errores semánticos encontrados

    # -- channel C3 : eeg;
    def visitChannelDecl(self, ctx):
        nombre = ctx.ID().getText()
        if nombre in self.canales:
            # error: canal declarado dos veces
            self.errores.append(f"Canal '{nombre}' ya declarado")
        else:
            self.canales.add(nombre)  # registrar canal como declarado

    # -- threshold alto : 0.80;
    def visitThresholdDecl(self, ctx):
        nombre = ctx.ID().getText()
        if nombre in self.umbrales:
            # error: umbral declarado dos veces
            self.errores.append(f"Umbral '{nombre}' ya declarado")
        else:
            self.umbrales.add(nombre)  # registrar umbral como declarado

    # -- when signal(C3) > alto { output("A"); }
    def visitWhenStmt(self, ctx):
        # verificar que el canal usado en signal(ID) fue declarado
        canal = ctx.signal().ID().getText()
        if canal not in self.canales:
            self.errores.append(f"Canal '{canal}' usado pero no declarado")

        # verificar que el umbral usado en la expresión fue declarado
        expr = ctx.expression()
        if expr.ID():
            umbral = expr.ID().getText()
            if umbral not in self.umbrales:
                self.errores.append(f"Umbral '{umbral}' usado pero no declarado")

        # visitar cada output dentro del when
        for out in ctx.outputStmt():
            self.visit(out)

    def visitOutputStmt(self, ctx):
        pass  # nada que verificar semánticamente en output("A")
