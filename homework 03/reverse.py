l=[1,2,3,4,5]
s=[0,0,0,0,0]
for i in range(0,5):
    s[4-i]=l[i]
for i in range (0,5):
    print(s[i])
l=[1,2,3,4,5]
k=4
while k>=0:
    print(l[k])
    k=k-1
l=[1,2,3,4,5]
print(l[::-1])