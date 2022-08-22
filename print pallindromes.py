a=200
for i in range(1,a+1):
    temp = i
    sum = 0;
    while(temp >0):
        rem = temp % 10
        sum = sum * 10 +rem
        temp = temp//10
    if i == sum:
        print(i)
