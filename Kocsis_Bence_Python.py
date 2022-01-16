import random
import time
    
def várás():
    time.sleep(3)

#Történet kezdete
print("Ugh.. Milyen undorító")
várás()
print("Ez egy elég sötét és csendes hely..")
várás()
print("Ez már túl csendes..")
várás()
print("Biztos vagyok benne hogy van itt valaki.. vagy valami!")
várás()
én = input("Szerencsére én vagyok.. <Mi a neved?> ")
print(f"{én}, a titokzatos kardforgató.. aki minden fegyvert halálosan tud használni.. még.. egy vajazó kést is.")
time.sleep(5)
#Akció
print("*BZZ BZZ FSH FSH*")
várás()
print(f"{én}: Mi ez? Valamit hallok onnan.. Mi lehet ez?")
várás()
print("*DMTS*(Megjelenik egy démon)")
várás()
print(f"{én}: ÁÁÁHHHHHH!! Te meg hogy nézel ki?! KI vagy te?!.. vagy inkább.. MI vagy te?!")
várás()
print("*Mnyuhahahhaa*")
várás()
print("-Demon: Én vagyok a dobókockák démonja.. Mi lenne ha avval döntenénk el az életed, hogy kitalálod-e hogy mit dob a kocka?! MUHAHA!!!")
döntés = input("<Próbára teszed a szerencsédet? (Igen/Nem)> ")
#dobókocka
dobás = random.randint(1,6)
if döntés == "Igen":
    print(f"{én}: Najó.. Hát legyen.. Hisz én, {én} a titokzatos kardforgató nagyon is szerencsés!!")
    szám = input("<Tippelj, hányast fog a Démon dobni? (1,2,3,4,5,6)> ")
    print(f"Hát jó.. legyeeeeen... {szám}!")
    if dobás == szám:
        print(f"-Demon: Wow.. pedig.. álltalában nem találják el.. hát jó.. sok sikert a további kalandjaidon! Bátor {én}!")
    else:
        print(f"-Demon: HUH.. Tényleg azthitted hogy ilyen könnyen LEGYŐZHETSZ?! Nyilvánvalóan nem {szám} lett az.. Most.. Pedig.. VÉGED")
        várás()
        print("*FSHLL, (ledöfted a kardoddal)*")
        várás()
        print("-Demon: Ug.. AH. Uh... Ennek nem le.. lehet így vége.. AUGH.....")
        várás()
        print(f"{én}: Hát ez eléggé egyszerű volt..")
else:
    print(f"{én}: Mi lenne, ha inkább befognád és lenyelnéd a kardom?!?")
    várás()
    print("*(neki futsz a démonnak)*")
    várás()
    print("*FSHLJJ (belé szúrod a kardod)*")
    print("..")
    várás()
    print("*(lenyelte a kardod)*")
    várás()
    print("-Démon: Azthitted hogy ez ilyen egyszerű?")
    várás()
    print(f"{én}: Igen..")
    várás()
    print("-Démon: MUHAHAHA.. mégis hány éves vagy te?!")
    kor = input("<Hány éves a titokzatos kardforgató?> ")
    if kor <="18":
        print("-Démon: Oh.. értem.. akkor inkább hozzád sem érek.. azthiszem.. sok szerencsét az utadon bátor harcos!")
        várás()
    else:
        print("-Démon: Áhh.. akkor milenne ha inkább meghívnálak egy kis Démon löttyre?")
        várás()
        print("*VÉGE*")