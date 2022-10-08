s=input()
res=1
tem=1
if s==0 or s==1:
    print(len(s))    
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        tem+=1
    else: res=max(res,tem)
print(res)