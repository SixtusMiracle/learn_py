#!/usr/bin/python3

class RevString(str):
    def __str__(self):
        return self[::-1]


s = "Hello World"
s2 = s.split()
s3 = "--".join(s2)

print(f"In lower: {s.lower()}")
print(f"In upper: {s.upper()}")
print(f"When capitalized: {s.capitalize()}")
print(f"Using casefold: {s.casefold()}")
print(f"Revising the string: {RevString(s)}")

print(f"\nThen I split: {s2}")
print(f"Joining it back with --: {s3}")
