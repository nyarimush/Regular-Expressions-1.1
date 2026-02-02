import re

# Your first regex in Python

text = "I love Python"

pattern = r"Python"

# Find the pattern

match = re.search(pattern, text)

if match:
    print(f"Found: {match.group()}")
# Output: Found: Python








# Match exact word

re.search(r"Python", "I love Python")

# Returns match object
