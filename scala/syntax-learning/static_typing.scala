var greet : String = "hello"
printlin(green)

// can also type var greet = "hello",
// and it still works because it infers greet
// as type String at compiletime.

greet = "howdy"
// can change value
println(greet)

// greet = 1 cannot work -- compile time error

// var = mutable
// val = immutable

val greeting = "hello"
// greeting = "howdy"
// does not work
//
