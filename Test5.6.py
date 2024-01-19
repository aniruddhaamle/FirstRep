
from difflib import SequenceMatcher
string1 = "abcdxyx"
string2 = "xyzabcdpqr"

match = SequenceMatcher(None, string1, string2).find_longest_match()

print(match)  
print(string1[match.a:match.a + match.size])  
print(string2[match.b:match.b + match.size])  