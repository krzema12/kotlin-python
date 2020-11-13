
        package generated.Python
        
        sealed class mod()
        
        
        data class Module(val body: stmt, val type_ignores: type_ignore) 
            : mod() 
        

        data class Interactive(val body: stmt) 
            : mod() 
        

        data class Expression(val body: expr) 
            : mod() 
        

        data class FunctionType(val argtypes: expr, val returns: expr) 
            : mod() 
        
    