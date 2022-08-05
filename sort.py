def add_word():
    w=input("enter the word: ")
    m=input("enter the meaning of the word: ")
    dict.update({w:m})
    print(dict)

def delete_word():
    d=input("enter the word you want to delete: ")
    if d in dict:
        print("word deleted!")
        dict.pop(d)
        print(dict)
    else:
        print("entered word is not present in the dictionary")

def search_word():
    s=input("enter the word you want to search: ")
    if s in dict:
        print("word found!")
        print("meaning of the word is: ",dict.get(s))
    else:
        print("entered word is not present in the dictionary")

def display_order():
    k=dict.keys()
    print(sorted(k))

def same_meaning():
    sm=input("enter the word: ")
    for key,value in dict.items():
        if value==sm:
            print("the word with same meaning are: ",key)

def display_contents():
    print("dictionary items are:\n", dict.items())

dict={'Answer': 'Reply', 'Explain': 'Elaborate', 'Dangerous': 'Hazardous', 'Huge': 'Big', 'Respond':
'Reply', 'Cry': 'Weep'}
print("dictionary:")
print(dict)
i=1

while (i!=0):
    print("1 for adding a word in the dictionary\n2 for deleting a word from dictionary\n3 for searching a word in the dictionary")
    print("4 for displaying words in alphabetical order\n5 for finding words with the same meaning\n6 for displaying dictionary contents")
    a=int(input("enter your choice: "))

    if(a==1):
        add_word()
    elif(a==2):
        delete_word()
    elif(a==3):
        search_word()
    elif(a==4):
        display_order()
    elif(a==5):
        same_meaning()
    elif(a==6):
        display_contents()
    else:
        print("enter a valid input")
    #i=input("enter 1 to continue ")
    if(i>5):
        break;
