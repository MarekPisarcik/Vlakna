# importujeme kniznice

import threading
import random
import time



# vytvorime zoznam 
nahodne_cisla = []

# objekt ktory, oznami, ze je zoznam pripraveny
zoznam_hotovy = threading.Event()

# Funkcia, ktora naplni zoznam nahodnymi cislami
def napln_zoznam():
    global nahodne_cisla
    for i in range(10):
        nahodne_cisla.append(random.randint(1,100))
        time.sleep(0.1) # Program sa zastavi na 0.1 sekundy
    zoznam_hotovy.set() # oznamujeme, ze zoznam je hotovy
    
# Funkcia na vypocet suctu
def sucet_cisel():
    zoznam_hotovy.wait()  # cakame kym bude zoznam spraveny
    sucet = sum(nahodne_cisla)
    print("Sucet cisel je: ",sucet)
    
# Funkcia na vypocet priemeru
def priemer_cisel():
    zoznam_hotovy.wait() # cakame kym bude zoznam spraveny
    priemer = sum(nahodne_cisla) / len(nahodne_cisla)
    print("Priemer cisel je: ",priemer)
# Spustenie vlakien
vlakno1 = threading.Thread(target=napln_zoznam)
vlakno2 = threading.Thread(target=sucet_cisel)
vlakno3 = threading.Thread(target=priemer_cisel)


vlakno1.start()
vlakno2.start()
vlakno3.start()


vlakno1.join()
vlakno2.join()
vlakno3.join()


print("Zoznam:", nahodne_cisla)