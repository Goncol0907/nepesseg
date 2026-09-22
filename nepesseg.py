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

FAJLNEV = "lakossag_2025.csv"

# Ezek a típusok számítanak "városnak" a megye városi lakosságának
# összegzésénél (a megyei jogú várost és a megyeszékhelyet is beleértve).
VAROSI_TIPUSOK = {
    "város",
    "vármegyei jogú város",
    "vármegye székhely",
    "fővárosi kerület",
}

ERVENYES_MEGYEKODOK = (
    "BUD BAC BAR BEK BOR CSO FEJ GYO HAJ HEV "
    "KOM NOG PES SOM SZA SZO TOL VAS VES ZAL"
).split()


def adatok_betoltese(fajlnev):
    """Beolvassa a CSV fájlt, és egy listát ad vissza, amelynek elemei
    a településeket leíró szótárak."""
    varosok = []
    with open(fajlnev, "r", encoding="UTF-8") as fajl:
        fajl.readline()  # fejléc sor kihagyása
        for sor in fajl:
            sor = sor.strip()
            if not sor:
                continue
            adat_sor = sor.split(";")
            adatok = {
                "megyekod": adat_sor[0],
                "telepules": adat_sor[1],
                "tipus": adat_sor[2],
                "ferfi": int(adat_sor[3].replace(" ", "")),
                "no": int(adat_sor[4].replace(" ", "")),
            }
            varosok.append(adatok)
    return varosok


def lakossag(varos):
    """Egy település teljes (férfi + nő) lakosságát adja vissza."""
    return varos["ferfi"] + varos["no"]


def megye_adatai(varosok, megyekod):
    """Kiírja egy megye település-számát, összlakosságát és a
    városokban élők számát."""
    telepulesek_szama = 0
    ossz_lakos = 0
    varosi_lakos = 0

    for varos in varosok:
        if varos["megyekod"] == megyekod:
            telepulesek_szama += 1
            ossz_lakos += lakossag(varos)
            if varos["tipus"] in VAROSI_TIPUSOK:
                varosi_lakos += lakossag(varos)

    if telepulesek_szama == 0:
        print("Nincs ilyen megyekód!")
        return

    print(f"\nTelepülések száma a megyében: {telepulesek_szama}")
    print(f"Összlakosság a megyében: {ossz_lakos}")
    print(f"Városokban élők száma: {varosi_lakos}\n")


def megye_menu(varosok):
    """Bekéri a megyekódot, majd kiíratja a megye adatait."""
    megyekod = input(
        f"Válasszon megyekódot ({'/'.join(ERVENYES_MEGYEKODOK)}): "
    ).strip().upper()

    if megyekod not in ERVENYES_MEGYEKODOK:
        print("Nincs ilyen megyekód!")
        return

    megye_adatai(varosok, megyekod)


def lapozo_lista(sorok, laponkent=12):
    """Egy szöveges lista lapozott kiírása.
    Enter = következő lap, x = kilépés a lapozásból."""
    if not sorok:
        print("Nincs megjeleníthető adat.")
        return

    for i in range(0, len(sorok), laponkent):
        lap = sorok[i:i + laponkent]
        for sor in lap:
            print(sor)

        van_meg = i + laponkent < len(sorok)
        if van_meg:
            tovabb = input("\n[Enter] = tovább, [x] = kilépés a listából: ")
            if tovabb.strip().lower() == "x":
                break
        print()


def telepules_tipusai(varosok):
    """Településtípus kiválasztása, majd az adott típusú települések
    lapozott kilistázása névvel és lakosságszámmal."""
    tipusok = sorted({varos["tipus"] for varos in varosok})

    print("\nTelepüléstípusok:")
    for sorszam, tipus in enumerate(tipusok, start=1):
        print(f"[{sorszam}] {tipus}")

    try:
        valasz = int(input("Válasszon egy típust a sorszámával: "))
        if valasz < 1 or valasz > len(tipusok):
            raise ValueError
        valasztott_tipus = tipusok[valasz - 1]
    except ValueError:
        print("Érvénytelen választás!")
        return

    sorok = [
        f"{varos['telepules']:<20}{varos['tipus']:<22}{lakossag(varos):>8} fő"
        for varos in varosok
        if varos["tipus"] == valasztott_tipus
    ]

    print(f"\n{valasztott_tipus} típusú települések ({len(sorok)} db):\n")
    lapozo_lista(sorok)


def fomenu():
    """A program főciklusa: főmenü megjelenítése és a választott
    funkció meghívása, amíg a felhasználó ki nem lép."""
    varosok = adatok_betoltese(FAJLNEV)

    while True:
        print("\n---- FŐMENÜ ----")
        print("[1] Megye adatai")
        print("[2] Település típusai")
        print("[X] Kilépés")
        menupont = input("Válasszon egy opciót: ").strip().upper()

        if menupont == "1":
            megye_menu(varosok)
        elif menupont == "2":
            telepules_tipusai(varosok)
        elif menupont == "X":
            print("Viszlát!")
            break
        else:
            print("Érvénytelen választás, próbálja újra!")


if __name__ == "__main__":
    fomenu()
