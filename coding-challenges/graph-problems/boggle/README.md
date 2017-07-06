# boggle question

### You're given:
---
- an NxN grid of characters
- a helper function, is_word, which returns true if a given string is a word

### The rules:
---
You can create a word by starting at any given point in the grid and moving in
any direction (up, right, left, down, and any diaganol), appending each
character that you visit to form a word. Once you've started a chain, you can
not revist any given position in the grid.

### Example:
---

__Grid:__
```
c r
a x
```

In this simple 2x2 grid, you can make the following words:

`'a', 'ax', 'car', 'x', 'ca', 'ac', 'arc', 'c', 'r'`

- * This result is according to the en_US dictionary shipped w/ the python enchant library.

### The ask
---
Find all valid words in the grid.
