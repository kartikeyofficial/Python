items=input("Input comma-separated sequence of words\n")
words=[word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))