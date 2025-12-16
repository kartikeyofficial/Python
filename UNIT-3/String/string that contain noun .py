def filter_number(text):
    noun={"Agra","Banana","Ramesh","Patna"}
    return[word for word in text if any(noun in word for noun in noun)]

text=["Apple","123","Agra","Banana","Ramesh","1234","Patna","Orange"]
print(filter_number(text))