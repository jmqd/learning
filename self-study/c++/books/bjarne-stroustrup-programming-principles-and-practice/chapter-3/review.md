# Review for Chapter 2.

1. The term prompt means to query the user for input.
2. The operator used to read into a variable is called the input operation, 
    '>>'. It is read as "get from".
3. Two lines of code: read an `integer` from user input to a `number` variable:

    ```
    int number = 0;
    std::cin >> number;
    ```
4. `'\n'` is the newline character. It puts a newline on the screen.
5. Whitespace terminates input into a string.
6. Non-integer characters terminate input into an integer, I suppose.
7. Here is that code written in a single line:

    ```
    std::cout << "Hello, " << first_name << "!\n";
     ```
8. An object is some memory that holds a value of a given type.
9. A literal is the actual value &mdash; a set of bits in memory interpreted
    according to its type.
10. Here are some of the different types:
    - `int` integer numbers
    - `char` effectively a number between 0 and 255 which maps to a character
    - `string` an array of chars (e.g. "Hello, world!")
    - `double` a floating point number. (e.g. 12.55)
    - `bool` a boolean value. either 1 or 0; true or false. (e.g. true)

11. A variable is a named object.
12. Typical sizes for:
    - `char` 255 possible values. [-127:127] 1 byte.
    - `int` 4 bytes. [-32767:32767], signed.
    - `double` 8 bytes

13. Measures for small entities in memory such as strings and ints are measured
    in bytes.
14. `=` is the assignment operator. It assigns the value of the right side to
    the left side. `==` is the 'equal to' operator. It is a comparison operator
    and returns a boolean value. It returns true if and only if the left and
    right sides are exactly equal. Otherwise, it returns false.
15. A definition is a declaration that sets aside memory for an object.
16. Initialization is the process of giving a variable its initial value.
    Although initialization and assignment are similar, and indeed even use the
    same operator, `=`, they are logically distinct. Initialization always
    finds the variable empty. On the other hand, in principle, assignment must
    first clear out the old value from the variable before putting in the new
    one.

    
    Furthermore, one must declare a type during initialization.
17. String concatenation is the act of taking two strings and appending one to
    the other.
    
    e.g. `"abc" + "def" == "abcdef"` returns `true`
18. A name in C++ must start with a letter and contain only letters, numbers,
    or underscores.
19. Five examples of bad names:
    
    ```
    int g00gle = 1337; // confusing: '0' and 'O' aren't so visually distinct
    int _special = 0;   // potential clash: _* names are used by the system
    string ftf = 'jon'; // bad name: non-mainstream aliases are to be discarded
    int the_first_to_finish_in_time_by_5_minutes_or_less = 1; // too damn long
    ```
20. Good rules for names:
    
    1. Descriptive as possible, within reason.
    2. Avoid abbreviations that are ambiguous or unfamiliar.
    3. Type names have each word capitalized. e.g. GraphNode
    4. Variable and data members are all lowercase, with underscores between
        words. Member names have a trailing underscore.
    5. Constants may begin with 'k'. e.g. const int kDaysInAWeek = 7;
    6. Functions are to have Pascal case.
    7. Exceptionally cheap functions may be lower underscore named.

21. Type safety is all about objects only being used according to the rules for
    their type. Type safety is important because without it, we can get many
    errors and even undefined behaviors that produce unreasonable results.
22. `double` to `int` conversion can be a bad thing because it's a
    `narrowing conversion`. That is, a double can potentially hold much more
    than an int, so it is possible that the conversion loses information. This
    can cause undefined behavior and problems.
23. Define a rule to help decide if conversion from one type to another is bad:

    1. Order all of your types from smallest to largest.
    2. Beginning with the smallest type, create a bucket labeled with the size
        of that type.
    3. Put that type into that bucket.
    4. Continuing putting types into that bucket until you encounter a type
        of a greater size.
    5. `while(not all types are bucketed) { do steps 2:5; }`
    6. A type conversion from a -> b is to be considered OK if and only if
        these conditions are met:
        
        1. (size of a) >= (size of b)
        2. data format of a can be converted to b.

    
