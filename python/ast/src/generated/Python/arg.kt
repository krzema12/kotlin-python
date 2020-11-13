
        package generated.Python
        
        sealed class arg(open val lineno: int, open val col_offset: int, open val end_lineno: int?, open val end_col_offset: int?)
        
        
        data class argImpl(val arg: identifier, val annotation: expr?, val type_comment: string?, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : arg(lineno, col_offset, end_lineno, end_col_offset) 
        
    