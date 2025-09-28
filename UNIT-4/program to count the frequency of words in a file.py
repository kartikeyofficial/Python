from collections import counter
def word_count (fname):
    with open(fname) as f:
        return counter(f.read().split())
print("Numbers of words in the file: ",word_count("karthik.txt"))