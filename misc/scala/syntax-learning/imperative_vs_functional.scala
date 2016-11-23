
/*
  Imperative style
*/

def total(numbers: List[Int]) = {
  var sum = 0
  for (e <- numbers) {
    sum += e
  }

  sum
}

val test = List(1,2,3,4,5)
println("In imperative style...")
println(total(test))

/*
  Functional style
*/
println("Doing it funcy!")

def totalFunctional(numbers: List[Int]) = {
  numbers.foldLeft(0) {
    (c, e) => c + e
  }
}

println(totalFunctional(List(1,2,3,4,5)))

/*
  And again...
*/

def doubleFunctional(numbers: List[Int]) = {
  numbers.map { e => e * 2 }
}

println("A little bit more...")
println(doubleFunctional(List(1,2,3,4,5)))

