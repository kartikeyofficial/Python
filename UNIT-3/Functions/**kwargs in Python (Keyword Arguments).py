def myprg(**kwargs):
    for key, value in kwargs.items():
        print(key,"==",value)
myprg(first="Hello",mid="Welcome",last="Kartikey")