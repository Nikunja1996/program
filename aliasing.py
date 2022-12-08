#for existing function we can use another naem, which is nothing but function aliasing.
def wish (name):
    print("good morning :", name) #commented
greeting = wish
print(id(wish))
print(id(greeting))
greeting("durga")
wish("durga")
# in the above above example only one function is available but we call that function by using either wish name or greeting name .

