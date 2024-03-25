from random import randint, shuffle

def uzmini_skaitli():
    print("Sveiki! Esmu iedomājies skaitli no 1 līdz 100.")

mēģinājumi = 0
skaitlis = randint(1, 100)
    
while True:
    try:
        minējums = int(input("Mēģini uzminēt skaitli: "))
        mēģinājumi += 1 
        if minējums < skaitlis:
            print(" Tavs minējums ir par zemu!😥 Mēģini vēlreiz!🤩" )
            
        elif minējums > skaitlis:
            print("\033[1;31m Tavs minējums ir par augstu!😪 Mēģini vēlreiz!🤗\n")
        else:
            print(f"\033[1;32m Apsveicu!😜 Tu uzminēji {skaitlis} ar {mēģinājumi} mēģinājumiem! \n")
            break
    except ValueError:
        print("\033[1;33m Lūdzu ievadi skaitli! \n")
        

uzmini_skaitli()
