num=int(input("Enter a number to add:"))

def total(num):
    sum=0
    for i in range(1,num):
        sum=sum+i
    return sum
answer=total(num)
print(answer)