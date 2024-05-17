#Get value from user

num=int(input("Enter your number : "))

#fibonacci circle

fib=[0,1,1]
sum_num2=0

if num<=0 :
    print("error")
elif num==1 :
    print(0,1)
    print(f"sum of number {1}")
elif num==2:
    print(fib)
    print(f"sum of number {1}")
else:
    for i in range(2,num):

        fn=fib[i]+fib[i-1]
        fib.append(fn)
        
   
    print(fib)

    #sum of the sequence

    sum_num=sum(fib)
    print(f"sum of number {sum_num}")
    
    #sum of numbers before enterd by the user
    
    for i in fib :
        if i<num :
            sum_num2+=i 
    print(f"sum of number before enterd by the user : {sum_num2}")  
    

    