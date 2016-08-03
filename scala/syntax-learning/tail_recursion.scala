// Iterative
def factorialIterative(n : Int) : Int = {
  var fact = 1
  for (i <- 1 to n) {
    fact *= i
  }
  fact
}

// Recursive
def factorialRecursive(n : Int) : Int = {
  if (n == 1)
    1
  else
    n * factorialRecursive(n - 1)
}

// SICP
// Structure and Interpretation of Computer Programs

// Procedure vs Process
//
// A procedure is the code you write; a process is the code that runs.
//
// Iterative procedure -> iterative process
// Recursive procedure -> recursive process
// Big gains: recursive procedure, but somehow, quietly...
//  -> it runs as a iterative process.
// Best of both worlds.
//    - Recursion is expressive.
//    - Runs as an iteration. (More perfomant.)
// The scala solution for this: tail recursion.
// (Functional programming advantages.)

// Best of both worlds.
// Tail call recusion, quietly transforms this code
// into a simple iterative process
// The @ annotation is not necessary; it is a compile-time check
// to verify that the function is tail-recursive optimized.

@scala.annotation.tailrec
def factorialTail(n : Int, fact : BigInt) : BigInt = {
  if (n == 1)
    fact
  else
    factorialTail(n - 1, n * fact)
}

// However, there is one disadvantage in this code.
// What it is that we lost?
//    - the simplicity of the function signature.

// To fix that:
// Encapsulate the function in a functional way by
// having the implementation function within the calling function.
def factorial(n : Int) = {
  @scala.annotation.tailrec
  def factorialImpl(n : Int, fact : BigInt) : BigInt = {
    if (n == 1)
      fact
    else
      factorialImpl(n - 1, fact * n)
  }

  factorialImpl(n, BigInt(1))
}
