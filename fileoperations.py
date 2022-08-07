def read_only():
    fn=open(file_name+".txt",'r')
    print("file content: ",fn.read())
    fn.close()

def write_only():
    fn=open(file_name+".txt",'w')
    string1=input("enter the string to write in the file: ")
    fn.write(string1)
    fn.close()

def append_mode():
    fn=open(file_name+".txt",'a')
    string2=input("enter the string you want to append: ")
    fn.write(string2)
    fn.close()

file_name=input("enter the name of file: ")
while True:
    print("1 to write\n2 to append a string\n3 to read the file")
    choice=int(input("enter your choice: "))
    if (choice==1):
        write_only()
    elif (choice==2):
        append_mode()
    elif (choice==3):
        read_only()
    else:
        print("enter a valid input")
    ans=input("enter y to continue and n to end the program: ")
    if ans!='y':
        break
