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



def trekk(valg):
    global box11
    if valg==11 and box11==fri:
        box11=spiller
        spille_brett = f"{box11}{box12}{box13}\n{box21}{box22}{box23}\n{box31}{box32}{box33}"
        print(spille_brett)


        
    
        



print (f"nå skal vi spille 3 på rad! \n{spille_brett} \nfor å velge ruta øverst til høyre må du skrive rad så rute \nrad(1) rute(3) så da blir det 13") 

trekk (11)

