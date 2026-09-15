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
varosok = []

lefutars = 0
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
        varosok.append(adatok)
print("[1] Megye adatai")
print("[2] Telepules tipusa")
print("[3]")
print("[4]")
menupont = int(input("Valaszon egy opciot:"))
if menupont == 1:
    megyekod_betu = input("Valaszon egy megyekodot (BUD/BAC/BAR/BEK/BOR/CSO/FEJ/GYO/HAJ/HEV/KOM/NOG/PES/SOM/SZA/SZO/TOL/VAS/VES/ZAL)")
    for varos in varosok:
            if varos["megyekod"] == megyekod_betu:
                print(varos["telepules"],end=";")
                print(varos["tipus"],end=";")
                nepesseg = varos["ferfi"] + varos["no"]               
                print(nepesseg)
                lefutars += 1
            if lefutars == 12:
                lefutars = 0
                break
    for i in range(12):
        del varosok[0]
                

    while True:
        tovabb = input("Sokozzel tovabb/x -szel kilep")
        if tovabb == " ":
                for varos in varosok:
                    if varos["megyekod"] == megyekod_betu:
                        print(varos["telepules"],end=";")
                        print(varos["tipus"],end=";")
                        nepesseg = varos["ferfi"] + varos["no"]
                        print(nepesseg)
                        lefutars += 1
                    if lefutars == 12:
                        lefutars = 0
                        break
                for i in range(12):
                    del varosok[0]
                        
        elif tovabb == "x":
            break
        else:
            tovabb = input("Sokozzel tovabb/x -szel kilep")
