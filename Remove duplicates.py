li=[]
n= int(input("Enter the number of elements in list: "))
for x in range(0,n):
    element=int(input("Enter elements " + str(x+1) + ":"))
    li.append(element)
temp = set()
new = []
for x in li:
    if x not in temp:
        new.append(x)
        temp.add(x)
print("list is :",new)
