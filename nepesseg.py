'''
[1]megye adatai | megye kod/telepulesek szama/ossz lakos varos/ossz lakos
[2]telepules tipusai |  a/kozseg
                        b/fovarosi kerulet
                        c/varmegyejogu varos
                        d/nagykosseg
                        e/varos
[3]
[4]
'''
with open("nepesseg/repository/lakossag_2025.csv","r",encoding="UTF-8") as fajl:
    fajl.readline()
    for sor in fajl:
        adat_sor = sor.strip().split(";")
        adatok = {
            "megyekod" : adat_sor[0],
            "telepules" : adat_sor[1],
            "tipus" : adat_sor[2],
            "ferfi" : int(adat_sor[3].replace(" ","")),
            "no" : int(adat_sor[4].replace(" ",""))
        }

print("[1] Megye adatai")
print("[2] Telepules tipusa")
print("[3]")
print("[4]")
menupont = int(input("Valaszon egy opciot:"))
if menupont == 1:
    megyekod_betu = input("Valaszon egy megyekodot (BUD/BAC/BAR/BEK/BOR/CSO/FEJ/GYO/HAJ/HEV/KOM/NOG/PES/SOM/SZA/SZO/TOL/VAS/VES/ZAL)")
    for adat in adatok:
  
