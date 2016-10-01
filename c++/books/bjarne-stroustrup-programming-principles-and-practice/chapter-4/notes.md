Our job as programmers is to express computations:

1. Correctly
2. Simply
3. Efficiently

_In that order._


---

### Constants

C++ offers the notion of a symbolic constant, that is, a named object to which
you cannot give a new value after it has been initialized.

Ex: `constexpr double pi = 3.14159265358979`


### _Avoid literals. Use constants with descriptive names._


## Operators

- `f(a)`: function call | _pass a to f as an argument_
- `++lval`: pre-increment | _increment and use the incremented value_
- `--lval`: pre-decrement | _decrement and use the decremented value_
- `!a`: not | _result is bool_
- `-a`: unary minus
- `a * b`: multiply
- `a / b`: divide
- `a % b`: modulo (remainder) | _only for integer types_
- `a + b`: add
- `a - b`: subtract
- `out << b`: write b to out | _where out is an ostream_
- `in >> b`: read from in into b | _where in is an osteam_
- `a < b`: less than | _result is bool_
- `a <= b`: less than or equal | _result is bool_
- `a > b`: greater than | _result is bool_
- `a >= b`: greater than or equal | _result is bool_
- `a == b`: equal | _not to be confused with `=`, assignment_
- `a != b`: not equal | _result is bool_
- `a && b`: logical and | _result is bool_
-  `a || b`: logical or | _result is bool_
- `lval = a`: assignment | _not to be confused with ==_
- `lval *= a`: compound assignment | _`lval = lval * a`; also for `/`,`%`,`+`,`-`
