"""listener.py - provides the custom listener for Typt."""

from antlr.TyptParser import TyptParser
from antlr.TyptVisitor import TyptVisitor

from typt.typt_types import NameTypePair
from typt.typt_types import Type
from typt.typt_types import NoneType
from typt.typt_types import BoolType
from typt.typt_types import IntType
from typt.typt_types import FloatType
from typt.typt_types import StringType
from typt.typt_types import ObjectBaseType
from typt.typt_types import ListType
from typt.typt_types import TupleType
from typt.typt_types import SetType
from typt.typt_types import DictType
from typt.typt_types import FunctionType
from typt.typt_types import ObjectType


from typt.node import Node
from typt.program_node import ProgramNode
from typt.using_node import UsingNode
from typt.func_def_node import FuncDefNode
from typt.func_signature_node import FuncSignatureNode
from typt.stmt_node import StmtNode
from typt.expr_stmt_node import ExprStmtNode
from typt.assignment_expr_stmt_node import AssignmentExprStmtNode
from typt.var_dec_stmt_node import VarDecStmtNode
from typt.pass_stmt_node import PassStmtNode
from typt.break_stmt_node import BreakStmtNode
from typt.continue_stmt_node import ContinueStmtNode
from typt.return_stmt_node import ReturnStmtNode

from typt.suite_node import SuiteNode

from typt.test.atom_node import AtomNode
from typt.test.var_ref_node import VarRefNode
from typt.test.literal_node import LiteralNode

# 20th:
#   TODO: del_stmt (skipped as need exprlist done first)
#   TODO: REWRITE TO USE NameTypePair
#   TODO: REWRITE TO USE visitName

# 21st:
#   TODO: __repr__ for every node -- test output (ADD DEPTH!!!!!!)
#   TODO: Switch from representing types as strings to Type objects

# Done:
#   program
#   using
#   func_def
#   func_signature
#       func_parameter_list
#   stmt
#       simple_stmt
#           small_stmt
#               expr_stmt
#                   anassign
#                   augassign
#               var_dec_stmt
#               ¬del_stmt
#               pass_stmt
#               flow_stmt
#                   break_stmt
#                   continue_stmt
#                   return_stmt
#       compound_stmt
#           TODO compound statements
#   suite
#   TODO: test
#   name
#   typt_type


class Typt(TyptVisitor):
    """Provide custom Typt listener."""

    def __init__(self):
        """Initialise custom visitor."""
        self.program = ProgramNode()

        super().__init__()

    def visitProgram(self, ctx: TyptParser.ProgramContext) -> ProgramNode:
        """Visit `program' rule.

        Args:
            ctx (ProgramContext) : The program context

        Get the child using-declarations and statements.

        program ::= using* stmt* EOF

        """
        # Add using-declarations to program
        for using_ctx in ctx.using():
            self.program.using_list += [self.visitUsing(using_ctx)]

        # Add stmts to program
        for stmt_ctx in ctx.stmt():
            self.program.stmt_list += [self.visitStmt(stmt_ctx)]

        return self.program

    def visitUsing(self, ctx: TyptParser.UsingContext) -> UsingNode:
        """Visit `using' rule.

        Args:
            ctx (UsingContext) : ...

        using ::= ...

        """
        library_name = self.visitName(ctx.library_name)

        # If no alias => alias is same as name, otherwise get alias
        library_alias = library_name
        if ctx.library_alias:
            library_alias = self.visitName(ctx.library_alias)

        using = UsingNode(library_name, library_alias)

        # Add function signatures to using-declaration
        for fs_ctx in ctx.func_signature():
            using.function_signature_list += [self.visitFunc_signature(fs_ctx)]

        return using

    def visitStmt(self, ctx: TyptParser.StmtContext) -> StmtNode:
        """Visit `stmt' rule."""
        # If simple statment, visit child
        if ctx.simple_stmt():
            return self.visitSimple_stmt(ctx.simple_stmt())

        # Otherwise (is compound stmt), visit child
        return self.visitCompound_stmt(ctx.compound_stmt())

    def visitArgument_list(self, ctx: TyptParser.Argument_listContext):
        """Visit `argument_list' rule.

        Args:
            ctx (Argument_listContext) : ...

        argument_list ::= ...

        """
        return self.visitChildren(ctx)

    def visitArgument(self, ctx: TyptParser.ArgumentContext):
        """Visit `argument' rule.

        Args:
            ctx (ArgumentContext) : ...

        argument ::= ...

        """
        return self.visitChildren(ctx)

    def visitSimple_stmt(self, ctx: TyptParser.Simple_stmtContext) -> StmtNode:
        """Visit `simple_stmt' rule."""
        # Visit the child small_stmt
        return self.visitSmall_stmt(ctx.small_stmt())

    def visitSmall_stmt(self, ctx: TyptParser.Small_stmtContext) -> StmtNode:
        """Visit `small_stmt' rule."""
        # Return the child statement
        if ctx.expr_stmt():
            return self.visitExpr_stmt(ctx.expr_stmt())
        if ctx.var_dec_stmt():
            return self.visitVar_dec_stmt(ctx.var_dec_stmt())
        if ctx.del_stmt():
            return self.visitDel_stmt(ctx.del_stmt())
        if ctx.pass_stmt():
            return self.visitPass_stmt(ctx.pass_stmt())
        if ctx.flow_stmt():
            return self.visitFlow_stmt(ctx.flow_stmt())

        raise NotImplementedError('Small statment type not implemented yet.')

    def visitExpr_stmt(self, ctx: TyptParser.Expr_stmtContext) -> StmtNode:
        """Visit `expr_stmt' rule.

        Args:
            ctx (Expr_stmtContext) : ...

        expr_stmt ::= ...

        """
        # If no right-hand side (i.e. not an assignment expression)
        if not ctx.rhs:
            return ExprStmtNode(self.visitTest(ctx.lhs))

        # Otherwise (i.e. is assignment expression), get type of assignment
        if ctx.anassign():
            assignment_type = ctx.anassign().getText()
        if ctx.augassign():
            assignment_type = ctx.augassign().getText()

        return AssignmentExprStmtNode(
            self.visitTest(ctx.lhs),
            assignment_type,
            self.visitTest(ctx.rhs)
        )

    def visitAnassign(self, ctx: TyptParser.AnassignContext):
        """Dead method (never called)."""
        raise NotImplementedError('Should not be reached (anassign).')

    def visitAugassign(self, ctx: TyptParser.AugassignContext):
        """Dead method (never called)."""
        raise NotImplementedError('Should not be reached (augassign).')

    def visitVar_dec_stmt(self, ctx: TyptParser.Var_dec_stmtContext) -> VarDecStmtNode:
        """Visit `var_dec_stmt' rule.

        Args:
            ctx (Var_dec_stmtContext) : ...

        var_dec_stmt ::= ...

        """
        # If no initial value given, set to None
        if not ctx.rhs:
            return VarDecStmtNode(
                self.visitTest(ctx.lhs), ctx.typt_type().getText()
            )

        # Otherwise, parse intial value
        return VarDecStmtNode(
            self.visitTest(ctx.lhs),
            ctx.typt_type().getText(),
            self.visitTest(ctx.rhs)
        )

    def visitDel_stmt(self, ctx: TyptParser.Del_stmtContext):
        """Visit `del_stmt' rule."""
        # TODO: IMPLEMENT MEEEEEEEEEE! FOR IMMORTAN JOE ARRRRRRRRRRRRRGGG

        return self.visitChildren(ctx)

    def visitPass_stmt(self, ctx: TyptParser.Pass_stmtContext) -> PassStmtNode:
        """Visit `pass_stmt' rule."""
        # Return new pass statment, not data or anything needed! :D
        return PassStmtNode()

    def visitFlow_stmt(self, ctx: TyptParser.Flow_stmtContext) -> StmtNode:
        """Visit `flow_stmt' rule."""
        # Return relevant flow-stmt
        if ctx.break_stmt():
            return self.visitBreak_stmt(ctx.break_stmt())
        if ctx.continue_stmt():
            return self.visitContinue_stmt(ctx.continue_stmt())
        if ctx.return_stmt():
            return self.visitReturn_stmt(ctx.return_stmt())

        raise NotImplementedError('Flow statement type not implemented.')

    def visitBreak_stmt(self, ctx: TyptParser.Break_stmtContext) -> BreakStmtNode:
        """Visit `break_stmt' rule."""
        # Return a new break statement
        return BreakStmtNode()

    def visitContinue_stmt(self, ctx: TyptParser.Continue_stmtContext) -> ContinueStmtNode:
        """Visit `continue_stmt' rule."""
        # Return a new continue statement
        return ContinueStmtNode()

    def visitReturn_stmt(self, ctx: TyptParser.Return_stmtContext) -> ReturnStmtNode:
        """Visit `return_stmt' rule."""
        # Return statement with return value
        if ctx.test():
            return ReturnStmtNode(self.visitTest(ctx.test()))

        # 'Empty' return statement
        return ReturnStmtNode()

    def visitCompound_stmt(self, ctx: TyptParser.Compound_stmtContext):
        """Visit `compound_stmt' rule.

        Args:
            ctx (Compound_stmtContext) : ...

        compound_stmt ::= ...

        """
        return self.visitChildren(ctx)

    def visitIf_stmt(self, ctx: TyptParser.If_stmtContext):
        """Visit `if_stmt' rule.

        Args:
            ctx (If_stmtContext) : ...

        if_stmt ::= ...

        """
        return self.visitChildren(ctx)

    def visitWhile_stmt(self, ctx: TyptParser.While_stmtContext):
        """Visit `while_stmt' rule.

        Args:
            ctx (While_stmtContext) : ...

        while_stmt ::= ...

        """
        return self.visitChildren(ctx)

    def visitFor_stmt(self, ctx: TyptParser.For_stmtContext):
        """Visit `for_stmt' rule.

        Args:
            ctx (For_stmtContext) : ...

        for_stmt ::= ...

        """
        return self.visitChildren(ctx)

    def visitSuite(self, ctx: TyptParser.SuiteContext) -> SuiteNode:
        """Visit `suite' rule.

        Args:
            ctx (SuiteContext) : ...

        suite ::= simple_stmt | NEWLINE INDENT stmt+ DEDENT

        """
        suite_node = SuiteNode()

        # If the suite is just a simple statement, add it
        if ctx.simple_stmt():
            suite_node.stmt_list = [self.visitSimple_stmt(ctx.simple_stmt())]

        # Otherwise, it is a block => add each stmt in the block
        for s in ctx.stmt():
            suite_node.stmt_list += [self.visitStmt(s)]

        return suite_node

    def visitFunc_def(self, ctx: TyptParser.Func_defContext) -> FuncDefNode:
        """Visit `func_def' rule."""
        # Get function signature
        func_signature = self.visitFunc_signature(ctx.func_signature())

        # Get suite
        suite = self.visitSuite(ctx.suite())

        # Return FuncDefNode
        return FuncDefNode(func_signature, suite)

    def visitFunc_signature(self, ctx: TyptParser.Func_signatureContext) -> FuncSignatureNode:
        """Visit `func_signature' rule."""
        func_signature = FuncSignatureNode(
            self.visitName(ctx.name()), ctx.typt_type().getText()
        )

        # If parameters non-empty, get parameter nodes
        if ctx.func_parameter_list():
            func_signature.parameter_list = \
                self.visitFunc_parameter_list(ctx.func_parameter_list())

        return func_signature

    def visitFunc_parameter_list(self, ctx: TyptParser.Func_parameter_listContext) -> list:
        """Visit `func_parameter_list' rule."""
        # Return the parameter list as a list of tuples of form (id, type)
        parameter_list = list()

        names = [self.visitName(name) for name in ctx.name()]
        types = [type.getText() for type in ctx.typt_type()]

        return list(zip(names, types))

    def visitClass_def(self, ctx: TyptParser.Class_defContext):
        return self.visitChildren(ctx)

    def visitClass_dec(self, ctx: TyptParser.Class_decContext):
        return self.visitChildren(ctx)
    
    def visitClass_method(self, ctx: TyptParser.Class_methodContext):
        return self.visitChildren(ctx)
    
    def visitClass_static_method(self, ctx: TyptParser.Class_static_methodContext):
        return self.visitChildren(ctx)
    
    def visitTest(self, ctx: TyptParser.TestContext):
        return self.visitChildren(ctx)
    
    def visitOr_test(self, ctx: TyptParser.Or_testContext):
        return self.visitChildren(ctx)
    
    def visitAnd_test(self, ctx: TyptParser.And_testContext):
        return self.visitChildren(ctx)
    
    def visitNot_test(self, ctx: TyptParser.Not_testContext):
        return self.visitChildren(ctx)
    
    def visitComparison(self, ctx: TyptParser.ComparisonContext):
        return self.visitChildren(ctx)
    
    def visitComp_op(self, ctx: TyptParser.Comp_opContext):
        return self.visitChildren(ctx)
    
    def visitExpr(self, ctx: TyptParser.ExprContext):
        return self.visitChildren(ctx)
    
    def visitXor_expr(self, ctx: TyptParser.Xor_exprContext):
        return self.visitChildren(ctx)
    
    def visitAnd_expr(self, ctx: TyptParser.And_exprContext):
        return self.visitChildren(ctx)
    
    def visitShift_expr(self, ctx: TyptParser.Shift_exprContext):
        return self.visitChildren(ctx)
    
    def visitArith_expr(self, ctx: TyptParser.Arith_exprContext):
        return self.visitChildren(ctx)
    
    def visitTerm(self, ctx: TyptParser.TermContext):
        return self.visitChildren(ctx)
    
    def visitFactor(self, ctx: TyptParser.FactorContext):
        return self.visitChildren(ctx)
    
    def visitPower(self, ctx: TyptParser.PowerContext):
        return self.visitChildren(ctx)
    
    def visitAtom_expr(self, ctx: TyptParser.Atom_exprContext):
        return self.visitChildren(ctx)

    def visitAtom(self, ctx: TyptParser.AtomContext) -> AtomNode:
        """Return VarRefNode or LiteralNode, depending on atom."""
        # If the atom is a variable reference, return a new VarRefNode
        if ctx.name():
            return VarRefNode(self.visitName(ctx.name()))

        # TODO Number => int/float

        # Otherwise, get type from literal value
        text = ctx.getText()
        if text == 'None':
            return LiteralNode('NoneType', text)
        if text == 'True':
            return LiteralNode('Bool', text)
        if text == 'False':
            return LiteralNode('Bool', text)
        if text == 'self':
            # TODO self references
            print('Self not implemented @ visitAtom')
            return LiteralNode('', text)

        # TODO If none of the above => then string

        return self.visitChildren(ctx)

    def visitTrailer(self, ctx: TyptParser.TrailerContext):
        return self.visitChildren(ctx)
    
    def visitSubscriptlist(self, ctx: TyptParser.SubscriptlistContext):
        return self.visitChildren(ctx)
    
    def visitSubscript(self, ctx: TyptParser.SubscriptContext):
        return self.visitChildren(ctx)
    
    def visitSliceop(self, ctx: TyptParser.SliceopContext):
        return self.visitChildren(ctx)
    
    def visitExprlist(self, ctx: TyptParser.ExprlistContext):
        return self.visitChildren(ctx)

    def visitTestlist(self, ctx: TyptParser.TestlistContext):
        return self.visitChildren(ctx)

    def visitName(self, ctx: TyptParser.NameContext) -> str:
        """Return the contents."""
        return ctx.getText()

    def visitTypt_type(self, ctx: TyptParser.Typt_typeContext) -> Type:
        """Temporary visit for typt_type."""
        text = ctx.getText()

        # Base Types (None, Bool, Int, Float, String, ObjectBaseType)
        if ctx.none_type:
            return NoneType()
        if ctx.bool_type:
            return BoolType()
        if ctx.int_type:
            return IntType()
        if ctx.float_type:
            return FloatType()
        if ctx.string_type:
            return StringType()
        if ctx.object_base_type():
            return ObjectBaseType()

        # Object Type
        if ctx.object_type:
            # Get members names, types
            names = [self.visitName(name) for name in ctx.name()]
            types = [self.visitTypt_type(t) for t in ctx.typt_type()]

            # Create NameTypePairs
            members = list()
            for (n, t) in zip(names, types):
                members += [NameTypePair(n, t)]

            return ObjectType(members)

        # Function Type
        if ctx.function_type:
            return_type = self.visitTypt_type(ctx.return_type)

            # Get parameter types
            parameter_types = list()
            for ctx_type in ctx.typt_type():
                parameter_types += [self.visitTypt_type(ctx_type)]

            return FunctionType(parameter_types, return_type)

        # List, Tuple, Set, Dict
        if ctx.list_type:
            return ListType(self.visitTypt_type(ctx.element_type))
        if ctx.tuple_type:
            # Get type list
            element_types = list()
            for ctx_typt_type in ctx.typt_type():
                element_types += [self.visitTypt_type(ctx_typt_type)]

            return TupleType(element_types)
        if ctx.set_type:
            return SetType(self.visitTypt_type(ctx.element_type))
        if ctx.dict_type:
            return DictType(
                self.visitTypt_type(ctx.key_type),
                self.visitTypt_type(ctx.value_type)
            )

        raise NotImplementedError(
            'The type \'{}\' is not implemented yet.'.format(text)
        )
