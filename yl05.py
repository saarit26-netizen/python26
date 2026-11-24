# 24.11.26 Richard

import random
valik = input("Kull või kiri: ")
suv = random.randint(0,1)
if suv == 1:
    avalik = "kiri"
else:
    avalik = "kull"
    
if valik == avalik:
    print("palju õnne!")
else:
    print("hale oled hahahhahaha!")

# Ilmaennustuse rakendus (and)
# Sinu ülesanne on luua lihtne Pythoni programm, mis aitab kasutajal valida sobiva riietuse vastavalt ilmale.
# Kasutaja sisestab temperatuuri (Celsius). Kui temperatuur on alla 0 kraadi, peab programm väljastama soovituse kanda talveriideid. Kui temperatuur on vahemikus 0 kuni 15 kraadi, peaks programm soovitama kanda kevad-sügis rõivaid. Kui temperatuur on üle 15 kraadi, soovitab programm kanda suveriideid.
# Kasuta if, elif ja else lauseid selle ülesande lahendamiseks.

temp = int(input("sisesta temp: "))
if temp < 0:
    print("Talveriided")
elif temp >= 0 and temp <= 15:
    print("Sügisriided")
else:
    print("Suveriided")