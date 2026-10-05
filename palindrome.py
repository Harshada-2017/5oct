num=int(input("Enter a number:"))
def reverseNumber(num: int) -> int:
    reversed_num = 0
    while num > 0:
        digit = num % 10 #45%10=4
        reversed_num = reversed_num * 10 + digit #0*10+4=4
        num = num // 10 #45//10=5 
    return reversed_num
answer=reverseNumber(num)
if answer==num:
    print("Palindrome")
else:
    print("Not palindrome")
