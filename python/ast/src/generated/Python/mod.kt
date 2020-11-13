
        package generated.Python
        
        sealed class mod()
        
        
        data class Module(val body: kotlin.collections.List<stmt>, val type_ignores: kotlin.collections.List<type_ignore>) 
            : mod() 
        

        data class Interactive(val body: kotlin.collections.List<stmt>) 
            : mod() 
        

        data class Expression(val body: expr) 
            : mod() 
        

        data class FunctionType(val argtypes: kotlin.collections.List<expr>, val returns: expr) 
            : mod() 
        
    