numero=str(input("anna binääri numero: ")) #01000101 = 69 = e
numeroy=1
numeroyl=[]
#(len(numero))
#(numero[1])
laskuri=1
while laskuri<len(numero):
    #print(laskuri)
    numeroy*=2
    numeroyl.append(2**(len(numero)-laskuri))
    laskuri+=1
numeroyl.append(1)
#print(numeroyl)
#print(numeroy)
laskuri=0
lasku=[]
while laskuri<len(numero):
    if numero[laskuri]=="1":
        #print(numero[laskuri])
        lasku.append(numeroyl[laskuri])
    laskuri+=1
final=0
laskuri=0
while laskuri<len(lasku):
    final+=lasku[laskuri]
    laskuri+=1
print(final)
    