a=123
sum =0
rev = a
while a>0:
    rem = a % 10
    sum = sum*10 + rem
    a = a//10
if rev == sum:
    print("pallindrome\n")
else:
    print("Notpallindrome\n")