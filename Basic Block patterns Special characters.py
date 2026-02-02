import re

# Match "bat", "cat", "hat", etc.


text = "The cat and the bat sat"

pattern = r".at"

# Find the pattern

match = re.findall(pattern, text)
print(match)
# Output: Found: [ 'cat', 'bat', 'sat']
