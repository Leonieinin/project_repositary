hp = "C:\\Users\\USER\\Documents\\自然語言\\報告\\harry potter.txt"
f_hp = open(hp,"r",encoding="utf-8")
hp_info = f_hp.read()
#print(f_hp.read())
f_hp.close()

hpspell = "C:\\Users\\USER\\Documents\\自然語言\\報告\\哈利波特咒語全集.txt"
f_hpspell = open(hpspell,"r",encoding="utf-8")
hps=f_hpspell.read()
#print(hps.split("\n"))
hps_split = hps.split("\n")
f_hpspell.close()
#print(len(hps_split))
num_spell = len(hps_split)

#import re
#import collections

print(type(hp))
print(type(hpspell))
for i in  range(len(hps_split)):
    print(hps_split[i],end=' ')
    print(hp_info.upper().count(hps_split[i].upper()))

#print(info.upper())
    


