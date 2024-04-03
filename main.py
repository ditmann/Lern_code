from random import randrange as tilfeldig


#variabler for boksene
fri = "|_|"
spiller = "|X|"
pc = "|O|"
#første rad
box11=fri
box12=fri
box13=fri
#Andre rad
box21=fri
box22=fri
box23=fri
#Tredeie rad
box31=fri
box32=fri
box33=fri
#hele spillebrettet satt sammen
spille_brett = f"{box11}{box12}{box13}\n{box21}{box22}{box23}\n{box31}{box32}{box33}"
#lager liste av de forskjellige trekkene man kan gjøre (blir brukt av PC)
mulige_trekk = [11,12,13,21,22,23,31,32,33]




#endrer statusen til boksene basert på tall fra brukeren
def trekk(valg):
    global box11
    global box12
    global box13  
    global box21
    global box22
    global box23
    global box31
    global box32
    global box33
    if valg==11 and box11==fri:
        box11=spiller
        rob_trekk(mulige_trekk[tilfeldig(0,8)])
        spille_brett = f"{box11}{box12}{box13}\n{box21}{box22}{box23}\n{box31}{box32}{box33}"
        print(spille_brett)
        print("bra jobba nå er det bare neste trekk")
        trekk(int(input()))
    elif valg==12 and box12==fri:
        box12=spiller
        rob_trekk(mulige_trekk[tilfeldig(0,8)])
        spille_brett = f"{box11}{box12}{box13}\n{box21}{box22}{box23}\n{box31}{box32}{box33}"
        print(spille_brett)
        print("bra jobba nå er det bare neste trekk")
        trekk(int(input()))
    elif valg==13 and box13==fri:
        box13=spiller
        rob_trekk(mulige_trekk[tilfeldig(0,8)])
        spille_brett = f"{box11}{box12}{box13}\n{box21}{box22}{box23}\n{box31}{box32}{box33}"
        print(spille_brett)
        print("bra jobba nå er det bare neste trekk")
        trekk(int(input()))
    elif valg==21 and box21==fri:
        box21=spiller
        rob_trekk(mulige_trekk[tilfeldig(0,8)])
        spille_brett = f"{box11}{box12}{box13}\n{box21}{box22}{box23}\n{box31}{box32}{box33}"
        print(spille_brett)
        print("bra jobba nå er det bare neste trekk")
        trekk(int(input()))
    elif valg==22 and box22==fri:
        box22=spiller
        rob_trekk(mulige_trekk[tilfeldig(0,8)])
        spille_brett = f"{box11}{box12}{box13}\n{box21}{box22}{box23}\n{box31}{box32}{box33}"
        print(spille_brett)
        print("bra jobba nå er det bare neste trekk")
        trekk(int(input()))        
    elif valg==23 and box23==fri:
        box23=spiller
        rob_trekk(mulige_trekk[tilfeldig(0,8)])
        spille_brett = f"{box11}{box12}{box13}\n{box21}{box22}{box23}\n{box31}{box32}{box33}"
        print(spille_brett)
        print("bra jobba nå er det bare neste trekk")
        trekk(int(input()))
    elif valg==31 and box31==fri:
        box31=spiller
        rob_trekk(mulige_trekk[tilfeldig(0,8)])
        spille_brett = f"{box11}{box12}{box13}\n{box21}{box22}{box23}\n{box31}{box32}{box33}"
        print(spille_brett)
        print("bra jobba nå er det bare neste trekk")
        trekk(int(input()))
    elif valg==32 and box32==fri:
        box32=spiller
        rob_trekk(mulige_trekk[tilfeldig(0,8)])
        spille_brett = f"{box11}{box12}{box13}\n{box21}{box22}{box23}\n{box31}{box32}{box33}"
        print(spille_brett)
        print("bra jobba nå er det bare neste trekk")
        trekk(int(input()))
    elif valg==32 and box32==fri:
        box32=spiller
        rob_trekk(mulige_trekk[tilfeldig(0,8)])
        spille_brett = f"{box11}{box12}{box13}\n{box21}{box22}{box23}\n{box31}{box32}{box33}"
        print(spille_brett)
        print("bra jobba nå er det bare neste trekk")
        trekk(int(input()))
    elif valg==33 and box33==fri:
        box33=spiller
        rob_trekk(mulige_trekk[tilfeldig(0,8)])
        spille_brett = f"{box11}{box12}{box13}\n{box21}{box22}{box23}\n{box31}{box32}{box33}"
        print(spille_brett)
        print("bra jobba nå er det bare neste trekk")
        trekk(int(input()))
    else:
        print("slutt å tull da \nprøv igjen")
        trekk(int(input()))



def rob_trekk(valg):
    global box11
    global box12
    global box13  
    global box21
    global box22
    global box23
    global box31
    global box32
    global box33
    if valg==11 and box11==fri:
        box11=pc
    elif valg==12 and box12==fri:
        box12=pc
    elif valg==13 and box13==fri:
        box13=pc
    elif valg==21 and box21==fri:
        box21=pc
    elif valg==22 and box22==fri:
        box22=pc
    elif valg==23 and box23==fri:
        box23=pc
    elif valg==31 and box31==fri:
        box31=pc
    elif valg==32 and box32==fri:
        box32=pc
    elif valg==32 and box32==fri:
        box32=pc
    elif valg==33 and box33==fri:
        box33=pc
    else:
        rob_trekk(mulige_trekk[tilfeldig(0,8)])





        


#introduksjon til spillet
print (f"nå skal vi spille 3 på rad! \n{spille_brett} \nfor å velge ruta øverst til høyre må du skrive rad så rute \nrad(1) rute(3) så da blir det 13") 
trekk (11)