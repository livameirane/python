from random import randint, shuffle



def uzmini_skaitli():
    print("Sveiki! Esmu iedomājies skaitli no 1 līdz 100.")
        skaitlis = random.randint( 1, 100)
        mēģinājumi = 0
    
    
while True:
        if minējums < skaitlis:
            print("Tavs minējums ir par zemu!😥 Mēģini vēlreiz!🤩")
            
        elif minējums > skaitlis:
            print("Tavs minējums ir par augstu!😪 Mēģini vēlreiz!🤗")
        else:
            print(f"Apsveicu!😜 Tu uzminēji {skaitlis} ar {mēģinājumi} mēģinājumiem")
        minējums = int(input("Mēģini uzminēt skaitli: "))
           mēģinājumi += 1 

uzmini_skaitli()
