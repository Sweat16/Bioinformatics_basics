#یه رشته DNA بهش میدی تمام جملات n حرفیش رو با تعداد تکرار به ترتیب میده
DNA=input("your DNA is:")
D=len(DNA)
freq={}
for k in range(D):
    L=k+1
    for i in range(D-L+1):
        pattern=DNA[i:i+L]
        freq[pattern]=0
        for j in range(D-L+1):
            if DNA[j:j+L]==pattern:
                freq[pattern]+=1
F=len(freq)
freq=dict(sorted(freq.items(), key=lambda item: item[1],reverse=True))
print("freq=",freq)