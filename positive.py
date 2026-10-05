num=int(input("Enter a number to check if even or odd:"))

def checknumber(num):
    if num>0:
        return("positive")
    elif num<0:
        return("negative")
    else:
        return("Number is equal to zero")
ans=checknumber(num)
print(ans)   