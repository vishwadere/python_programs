def length(inp):    #function to calculate the length of individual words
    tmplist=inp.split(" ")    #list to store the words
    l=[]  #list to store lengths of each word
    print("the list of individual strings is: ",inp.split(" "))
    for i in tmplist:
        l.append((len(i)))
    print("the length of each word is:",l)

inp=str(input("enter a string: "))    #input from thr user
length(inp)    #calling the function length
