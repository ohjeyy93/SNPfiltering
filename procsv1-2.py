import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

Druglist1 = ["Chloroquine", "Piperaquine", "Piperaquine", "Chloroquine", "Mefloquine", "Pyrimethamine", "Proguanil", "Sulfadoxine", "Artemisinin and its derivatives"]
Genelist1 = ["Pfcrt", "Pfcrt", "Pfcrt", "Pfmdr1 (in combination with Pfcrt mutations only)", "Pfmdr1", "Pfdhfr", "Pfdhfr", "Pfdhps","PfK13"]
Mutationlist1 = ["K76T + different sets of mutations at other codons (including C72S, M74I, N75E, A220S, Q271E, N326S, I356T and R371I)", "Detected in vivo: T93S, H97Y, F145I, I218F and C350R", "Detected in vitro: T93S, H97Y, F145I, I218F, M343L and G353V", "N51I, C59R, S108N and I164L", "N86Y, Y184F, S1034C, N1042D and D1246Y", "Pfmdr1 increased copy number", "A16V, N51I, C59R, S108N and I164L", "S436A/F, A437G, K540E, A581G and A613T/S",  "P441L, G449A, C469F/Y, A481V, R515K, P527H, N537I/D, G538V, V568G, R622I, A675V"] 
#print(len(Druglist1))
#print(len(Genelist1))
#print(len(Mutationlist1))
d= {'Gene':Genelist1,'Drug':Druglist1, "Mutation":Mutationlist1}
df = pd.DataFrame(data=d)
df.to_csv('report1-3-2.csv', index=False)

Genelist2 = ["Pfdhps", "Pfdhfr", "Pfmdr1", "PfK13", "Pfcrt"]
Distancelist1 = [1487,1827, 2157,  2181, 2586]
Pfcrtgene1=['K76T', "C72S", "M74I", "N75E", "T93S", "H97Y", "F145I", "I218F", "A220S", "Q271E", "N326S", "M343L","C350R", "G353V", "I356T", "R371I"]
Pfcrtlist1=[76,72,74,75,93,97, 145,218, 220,271,326, 343, 350,353, 356,371,]
Pfmdr1gene1=['N51I', "C59R", "N86Y", "S108N", "I164L", "Y184F", "S1034C", "N1042D", "D1246Y"]
Pfmdr1=[51,59,86, 108, 164, 184, 1034, 1042, 1246]
Pfk13gene1=["P441L", "G449A", "C469F/Y", "A481V", "R515K", "P527H", "N537I/D", "G538V", "V568G", "R622I", "A675V"]
Pfk13=[441,449,469,481,515,527,537,538,568,622,675]
Pfdhfrgene1=["A16V", "N51I", "C59R", "S108N","I164L"]
Pfdhfr=[16, 51, 59, 108, 164]
Pfdhpsgene1=["S436A/F", "A437G", "K540E", "A581G", "A613T/S"]
Pfdhps=[436,437,540,581,613]

d2= {'Gene': Genelist2, 'Distance': Distancelist1}
d3= {'Pfcrt': Pfcrtgene1, 'Distance': Pfcrtlist1}
d4= {'Pfmdr1': Pfmdr1gene1, 'Distance': Pfmdr1}
d5= {'Pfk13': Pfk13gene1, 'Distance': Pfk13}
d6= {'Pfdhfr': Pfdhfrgene1, 'Distance': Pfdhfr}
d7= {'Pfdhps': Pfdhpsgene1, 'Distance': Pfdhps}


#df2 = pd.DataFrame(data=d2)
df3 = pd.DataFrame(data=d3)
df4 = pd.DataFrame(data=d4)
df5 = pd.DataFrame(data=d5)
df6 = pd.DataFrame(data=d6)
df7 = pd.DataFrame(data=d7)

#sns.catplot(x="Distance", y="Gene", kind= "point", data=df2)
sns.catplot(x="Distance", y="Pfcrt", kind= "point", data=df3)
plt.savefig("Pfcrt.png")
sns.catplot(x="Distance", y="Pfmdr1", kind= "point", data=df4)
plt.savefig("Pfmdr1.png")
sns.catplot(x="Distance", y="Pfk13", kind= "point", data=df5)
plt.savefig("Pfk13.png")
sns.catplot(x="Distance", y="Pfdhfr", kind= "point", data=df6)
plt.savefig("Pfdhfr.png")
sns.catplot(x="Distance", y="Pfdhps", kind= "point", data=df7)
plt.savefig("Pfdhps.png")