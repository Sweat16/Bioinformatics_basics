#یه رشته DNA بهش میدی تمام جملات  با تعداد حرف وارد شدهحرفیش رو با تعداد دلخواهت به ترتیب تکرار میده
DNA=input("your DNA is:")
D=len(DNA)
freq={}
L=int(input("Enter the lenght:"))
for i in range(D-L+1):
    pattern=DNA[i:i+L]
    freq[pattern]=0
    for j in range(D-L+1):
        if DNA[j:j+L]==pattern:
            freq[pattern]+=1
freq=dict(sorted(freq.items(), key=lambda item: item[1],reverse=True))
print("freq=",freq)