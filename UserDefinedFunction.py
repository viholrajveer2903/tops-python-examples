'''
Function: It is a set instruction that perform a specific task.
'''
#Function with No Argument & No Return Value.

def printLine():
    print("*"*50)

printLine()
print("Welcome To User Defined Function In Python.")
printLine()

#Function with Argument & Without Return Value.

def add(a,b):
    print("Addition : ",a+b)

printLine()
x=int(input("Enter Value : "))
y=int(input("Enter Value : "))
add(x,y)
printLine()

#Function with Argument & With Return Value.

def sub(a,b):
    return a-b

printLine()
x=int(input("Enter Value : "))
y=int(input("Enter Value : "))
#ans=sub(x,y)
print("Subtraction : ",sub(x,y))
printLine()
    
