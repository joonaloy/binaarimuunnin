numero=str(input("anna binääri numero: ")) #01000101 = 69 = e
numeroy=1
numeroyl=[]
laskuri=1
while laskuri<len(numero):
    numeroy*=2
    numeroyl.append(2**(len(numero)-laskuri))
    laskuri+=1
numeroyl.append(1)
laskuri=0
lasku=[]
while laskuri<len(numero):
    if numero[laskuri]=="1":
        lasku.append(numeroyl[laskuri])
    laskuri+=1
final=0
laskuri=0
while laskuri<len(lasku):
    final+=lasku[laskuri]
    laskuri+=1
print(final)
    
