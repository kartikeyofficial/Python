def find_longest_word(filename):
    with open(filename,"r") as file:
        content = file.read()
    words = content.split()
    longest_word = max(words, key= len)
    return longest_word
filename = "karthik.txt"
longest_word = find_longest_word(filename)
print(f"The Longest word in The File '{filename}' is: {longest_word}")