#نمودار پراکندگی در DNA دلخواه
Genome=input("Genome is:")
symbol=input("symbol is:")
def FasterSymbolArray(Genome, symbol):
    array = {}
    l=len(Genome)
    ExtendedGenome=Genome+Genome[0:l//2]
    array[0]=PatternCount(ExtendedGenome[0:l//2],symbol)
    for i in range(1,l):
        array[i]=array[i-1]
        if ExtendedGenome[i-1]==symbol:
            array[i]-=1
        if ExtendedGenome[i+l//2-1]==symbol:
            array[i]+=1
    return array
def PatternCount(Pattern, Text):
    count = 0 
    k=len(Text)
    n=len(Pattern)
    for i in range(n-k+1):
        if Pattern[i:i+k]==Text:
            count+=1
    return count
X=FasterSymbolArray(Genome, symbol)
from matplotlib.pyplot import*
Genome_Position = list(X.keys())
Counts= list(X.values())
plot(Genome_Position,Counts)
print(X)