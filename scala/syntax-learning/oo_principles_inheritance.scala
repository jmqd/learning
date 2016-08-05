trait Friend {
  val name: String
  def listen() = println("I'm " + name + " listening")
}

class Human (val name: String) extends Friend

class Animal (val name: String)

class Dog (override val name: String) extends
  Animal (name) with Friend

class Cat (override val name: String) extends
  Animal (name)

val sam = new Human("Sam")
sam.listen()

val soda = new Dog("Soda")
soda.listen()

// val polly = new Cat("Polly")
// polly.listen()
// Does not work, of course.

// WOW! Look at this.
// Amazing, mixing in to make a one-of-a-kind instance.
val fionaghal = new Cat("Fionaghal") with Friend
fionaghal.listen()


def seekHelp(friend : Friend) {
  friend.listen()
}

// Yes, it counts as a Friend!
seekHelp(fionaghal)

