import re


text = "apple orange ice under black zoo"

pattern = r"\b[aeiou]\w*"

# Finding the vowels in the sentence

match = re.findall(pattern, text)
print(match)

#picks out the vowels
