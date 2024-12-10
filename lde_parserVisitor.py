# Generated from lde_parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .lde_parser import lde_parser
else:
    from lde_parser import lde_parser

# This class defines a complete generic visitor for a parse tree produced by lde_parser.

class lde_parserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lde_parser#programa.
    def visitPrograma(self, ctx:lde_parser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#declaracion.
    def visitDeclaracion(self, ctx:lde_parser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#modificacion.
    def visitModificacion(self, ctx:lde_parser.ModificacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#expresion.
    def visitExpresion(self, ctx:lde_parser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#writeStmt.
    def visitWriteStmt(self, ctx:lde_parser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#graficarStmt.
    def visitGraficarStmt(self, ctx:lde_parser.GraficarStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#tipoGrafico.
    def visitTipoGrafico(self, ctx:lde_parser.TipoGraficoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#extraerStmt.
    def visitExtraerStmt(self, ctx:lde_parser.ExtraerStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#exportarStmt.
    def visitExportarStmt(self, ctx:lde_parser.ExportarStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#ifStmt.
    def visitIfStmt(self, ctx:lde_parser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#forStmt.
    def visitForStmt(self, ctx:lde_parser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#whileStmt.
    def visitWhileStmt(self, ctx:lde_parser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#breakStmt.
    def visitBreakStmt(self, ctx:lde_parser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#regresionLinealStmt.
    def visitRegresionLinealStmt(self, ctx:lde_parser.RegresionLinealStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#funcionAct.
    def visitFuncionAct(self, ctx:lde_parser.FuncionActContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#classificadorStmt.
    def visitClassificadorStmt(self, ctx:lde_parser.ClassificadorStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#predecirStmt.
    def visitPredecirStmt(self, ctx:lde_parser.PredecirStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#evaluarStmt.
    def visitEvaluarStmt(self, ctx:lde_parser.EvaluarStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#agruparStmt.
    def visitAgruparStmt(self, ctx:lde_parser.AgruparStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#bloque.
    def visitBloque(self, ctx:lde_parser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#termino.
    def visitTermino(self, ctx:lde_parser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#factor.
    def visitFactor(self, ctx:lde_parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#acceso.
    def visitAcceso(self, ctx:lde_parser.AccesoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#addStmt.
    def visitAddStmt(self, ctx:lde_parser.AddStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#delStmt.
    def visitDelStmt(self, ctx:lde_parser.DelStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#sizeStmt.
    def visitSizeStmt(self, ctx:lde_parser.SizeStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#trigonometrica.
    def visitTrigonometrica(self, ctx:lde_parser.TrigonometricaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#lista.
    def visitLista(self, ctx:lde_parser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#matriz.
    def visitMatriz(self, ctx:lde_parser.MatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#relacional.
    def visitRelacional(self, ctx:lde_parser.RelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#logico.
    def visitLogico(self, ctx:lde_parser.LogicoContext):
        return self.visitChildren(ctx)



del lde_parser