num=int(input("Enter nnumber to calculate the square"))
def square(num):
    sum=0
    for i in range(1,num+1):
      
        sq=i*i
        sum=sum+sq
        
    return(sum)
ans=square(num)
print(ans)
        
    