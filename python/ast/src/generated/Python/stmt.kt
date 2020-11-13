
        package generated.Python
        
        sealed class stmt(open val lineno: int, open val col_offset: int, open val end_lineno: int, open val end_col_offset: int)
        
        
        data class FunctionDef(val name: identifier, val args: arguments, val body: stmt, val decorator_list: expr, val returns: expr, val type_comment: string, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class AsyncFunctionDef(val name: identifier, val args: arguments, val body: stmt, val decorator_list: expr, val returns: expr, val type_comment: string, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class ClassDef(val name: identifier, val bases: expr, val keywords: keyword, val body: stmt, val decorator_list: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Return(val value: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Delete(val targets: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Assign(val targets: expr, val value: expr, val type_comment: string, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class AugAssign(val target: expr, val op: operator, val value: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class AnnAssign(val target: expr, val annotation: expr, val value: expr, val simple: int, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class For(val target: expr, val iter: expr, val body: stmt, val orelse: stmt, val type_comment: string, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class AsyncFor(val target: expr, val iter: expr, val body: stmt, val orelse: stmt, val type_comment: string, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class While(val test: expr, val body: stmt, val orelse: stmt, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class If(val test: expr, val body: stmt, val orelse: stmt, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class With(val items: withitem, val body: stmt, val type_comment: string, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class AsyncWith(val items: withitem, val body: stmt, val type_comment: string, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Raise(val exc: expr, val cause: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Try(val body: stmt, val handlers: excepthandler, val orelse: stmt, val finalbody: stmt, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Assert(val test: expr, val msg: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Import(val names: alias, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class ImportFrom(val module: identifier, val names: alias, val level: int, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Global(val names: identifier, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Nonlocal(val names: identifier, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Expr(val value: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Pass(override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Break(override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Continue(override val lineno: int, override val col_offset: int, override val end_lineno: int, override val end_col_offset: int) 
            : stmt(lineno, col_offset, end_lineno, end_col_offset) 
        
    