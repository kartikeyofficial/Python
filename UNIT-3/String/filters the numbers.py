def filter_number(text):
    return[word for word in text if word.isdigit()]
text=["apple","123","Agra","Banana","Ramesh","1234","Patna","Orange"]
print(filter_number(text))