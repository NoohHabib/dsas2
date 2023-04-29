strings = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_strings = sorted(strings)
print(sorted_strings)


strings = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_strings = sorted(strings, key=len)
print(sorted_strings)

strings = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_strings = sorted(strings, key=lambda x: -len(x))
print(sorted_strings)

