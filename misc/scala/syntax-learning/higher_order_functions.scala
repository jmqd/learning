// Quitely implementing a Strategy Pattern via
// creating a higher order function.
// Higher-order functions take function(s) as parameters.

def totalPrices(prices : List[Int],
  selector : Int => Boolean) = {
  var total = 0
  for (price <- prices) {
    if (selector(price))
      total += price
  }
  total
}

val prices = List(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

// Total all prices in the list:
println("All prices in the list: " + totalPrices(prices, { prices => true }))

// Total prices less than 50:
println("Prices less than 50: " + totalPrices(prices, { prices => prices < 50 }))

// Prices divisible by 20:
println("Prices divisible by 20: " + totalPrices(prices, { prices => prices % 20 == 0 }))
