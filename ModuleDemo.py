import UDF

while True:
    print("*"*20)
    print("1.OddEven")
    print("2.MaxOfTwo")
    print("3.MaxOfThree")
    print("4.Fibonacci")
    print("5.Prime")
    print("6.Pattern")
    print("7.Exit")
    print("*"*20)

    choice=int(input("Enter Your Choice : "))
    print("*"*20)

    if choice==1:
        a=int(input("Enter Value : "))
        UDF.oddeven(a)
        print("*"*20)
    elif choice==2:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        UDF.maxoftwo(a,b)
        print("*"*20)
    elif choice==3:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        c=int(input("Enter Value : "))
        UDF.maxofthree(a,b,c)
        print("*"*20)
    elif choice==4:
        a=int(input("Enter Value : "))
        UDF.fibonacci(a)
        print("*"*20)
    elif choice==5:
        a=int(input("Enter Value : "))
        UDF.prime(a)
        print("*"*20)
    elif choice==6:
        a=int(input("Enter Value : "))
        UDF.pattern(a)
        print("*"*20)
    else:
        print("Thank You")
        break
        
