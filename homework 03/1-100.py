a=1
for i in range(1,100):
    if i%2==1:
        print(i)
        if i<=50:
            a*=i
print(a)