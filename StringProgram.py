s=input("Enter String : ")

ch=0
w=1
sp=0
n=0

for i in s:
    if i.isalpha():
        ch=ch+1
    elif i.isspace():
        w=w+1
        sp=sp+1
    elif i.isnumeric():
        n=n+1

print("Total Character : ",ch)
print("Total Word : ",w)
print("Total Space : ",sp)
print("Total Numeric : ",n)
