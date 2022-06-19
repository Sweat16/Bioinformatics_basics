 #نمودار و مقادیر اختلاف C و G را در رشته DNA دلخواه می دهد
Genome= input("Genome is:")
def SkewArray(Genome):
    Skew = {}
    n = len(Genome)
    Skew[0] = 0
    for i in range(n):
        if Genome[i] == "C":
           Skew[i+1] = Skew[i] - 1
        elif Genome[i] == "G":
            Skew[i+1] = Skew[i] + 1
        else:
            Skew[i+1] = Skew[i]
    return Skew.values()
print(SkewArray(Genome))
from matplotlib.pyplot import*
plot(SkewArray(Genome))