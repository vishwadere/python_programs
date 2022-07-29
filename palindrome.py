num=int(input("Enter a number: "))
temp=num
reverse=0
while(num>0):
    digit=num%10
    reverse=reverse*10+digit
    num=int(num/10)
if(temp==reverse):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
