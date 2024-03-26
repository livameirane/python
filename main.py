from random import randint


def uzmini_skaitli():
    print(f" \033[1;35m Sveiki! Esmu iedomājies skaitli no 1 līdz 100. \n")
    skaitlis = randint(1, 100)  
    mēģinājumi = 0
   


    while True:
        try:
            minējums = int(input("Mēģini uzminēt skaitli: "))  
            mēģinājumi += 1
            

            if minējums < skaitlis:
                print(f" \033[1;31m Tavs minējums ir par zemu!😥 Mēģini vēlreiz!🤩 \n")
            elif minējums > skaitlis:
                print(f" \033[1;31m Tavs minējums ir par augstu!😪 Mēģini vēlreiz!🤗 \n")
            else:
                print(f" \033[1;32m Apsveicu!😜 Tu uzminēji skaitli {skaitlis} ar {mēģinājumi} mēģinājumiem! \n")
                break  # lai izietu no cikla, kad uzminēts skaitlis
        except ValueError:
            print("Lūdzu, ievadi skaitli!")
    

uzmini_skaitli()


import time
symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
i = 0
while True:
    i = (i + 1) % len(symbols)
    print('\r\033[K%s loading...' % symbols[i], flush=True, end='')
    time.sleep(0.1)
