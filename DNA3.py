#رشته DNA رو رونویسی و مکملش رو میگه
DNA=list(input("DNA is:"))
K=["A","T","C","G"]
L=len(DNA)
for i in range(L):
    if DNA[i] == "T" :
        DNA[i]=K[0]
    elif DNA[i]=="A":
        DNA[i]=K[1]
    elif DNA[i]=="G":
        DNA[i]=K[2]
    elif DNA[i]=="C":
        DNA[i]=K[3]
complement=''.join(DNA)
print("your DNA complement is:",complement)    