# Head First Kotlin Practice

Simple Kotlin learning exercises without a full IDE.

## Files

- **hello.kt** - Basic "Hello, World!" program
- **Chapter1ExplainEachLine.kt** - Practice with classes, loops, conditionals
- **krun** - Bash script to compile and run Kotlin files

## Quick Start

Compile and run any Kotlin file:
```bash
./krun filename.kt
# or
./krun filename
```

## Manual Compilation (if needed)

```bash
# Compile to JAR
kotlinc MyFile.kt -include-runtime -d MyFile.jar

# Run the JAR
java -jar MyFile.jar
```

## Requirements

- Kotlin compiler (`kotlinc`)
- Java 17+ (Java 21 works)
