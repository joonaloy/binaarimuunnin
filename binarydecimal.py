numero=str(input("anna binääri numero: ")) #01000101 = 69 = e
numeroyl=[]
laskuri=1
while laskuri<len(numero):
    #lisää numeroyl listaan numeron 2 potenssiin numeron pituus-laskuri
    numeroyl.append(2**(len(numero)-laskuri))
    laskuri+=1
#lisää listan loppuun ykkösen
numeroyl.append(1)
laskuri=0
lasku=[]
while laskuri<len(numero):
    #menee numeroyl listan läpi ja tarkistaa onko numero "päällä" eli onko sama index 1 vai 0 alkuperäisessä numerossa
    # [128, 64, 32, 16, 8, 4, 2, 1]
    #   0   1   0   0   0  1  0  1
    #       64             4     1
    #jos sama index on 1 eli numero on "päällä", lisätään listaan lasku
    if numero[laskuri]=="1":
        lasku.append(numeroyl[laskuri])
    laskuri+=1
final=0
laskuri=0
while laskuri<len(lasku):
    #loppu numeroon lisätään kaikki "päällä" olevat numerot ja saadaan lopullinen desimaali numero
    final+=lasku[laskuri]
    laskuri+=1
print(final)
    
