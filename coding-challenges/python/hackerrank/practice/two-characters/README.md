# two character strings

String t always consists of two distinct alternating characters.
For example, if string t's two distinct characters are x and y,
then it could be xyxyx or yxyxy but not xxyy or xyyx.

You can convert some string t to string s by deleting characters from t.
When you delete a character from t, you must delete all occurrences of it in t.
For example, if t = abaacdabd and you delete the character a, then the string
becomes bcdbd.

Given t, convert it to the longest possible string s. Then print the length of
string s on a new line; if no string s can be formed from t, print 0 instead.
