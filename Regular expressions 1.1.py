import re

# Your first regex in Python

text = "The cat sat on the mat"

pattern = r"cat"

# Find the pattern

match = re.search(pattern, text)

if match:
    print(f"Found: {match.group()}")
# Output: Found: cat
