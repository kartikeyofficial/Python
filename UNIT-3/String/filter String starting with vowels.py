def filter_number(text):
    vowels={"a","e","i","o","u","A","E","I","O","U"}
    return[word for word in text if word[0] in vowels]
text=["Apple","123","Agra","Banana","Ramesh","1234","Patna","Orange"]
print(filter_number(text))