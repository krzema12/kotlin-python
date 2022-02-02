fun withJavaConfigured(command: String) = "JDK_9=\"\$JAVA_HOME\" $command"

fun gradle(command: String) = withJavaConfigured("./gradlew $command")
