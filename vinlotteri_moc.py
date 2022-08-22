import random
import sys
import time
import pygame as py
import math

py.init()
py.mixer.init()

start = 1
stop = 101
choises = {
    "Erland": [11,90],
    "Simon": [44,4],
    "Jonas": [13,69],
    "Vebjørn":[3,27],
    "Marit": [22,58],
    "Noah": [23,25],
    "Øyvind": [31,41],
    "Tale": [26,36],
    "Marius": [40,42],
    "Tobias": [9,99]
}

ranking = set()
antall_spillere = len(choises)
numbers = []

for i in range(start,stop):
    numbers.append(i)

""" def get_ready():
    global antall_spillere
    global choises
    
    chosen_tickets = []

    choise = " "
    while antall_spillere == 0:
        try:
            antall_spillere = int(input("hvor mange spillere? "))
        except ValueError:
            print("Hei du må bruke et tall da!!")
    i=0
    print(antall_spillere)

    while i < antall_spillere:
        i+=1
        try:
            name = str(input("Skriv navnet ditt: "))
        except ValueError:
            print("")
        choises[name] = []
        lodd = []
        choise = -1
        while choise != 0:
            try:
                choise = int(input(f"Velg et tall mellom {start} og {stop}: "))
            except ValueError:
                print("wow wow wow det må være et tall")
            if (choise not in chosen_tickets) & (choise !=0) & (choise < stop) & (choise > start):
                print(f"{name} har kjøpt et lodd")
                choises[name].append(choise)
                chosen_tickets.append(choise)
                print(choises)
            elif choise in chosen_tickets:
                print("Allerede valgt, prøv igjen")

            if choise == 0:
                print("ferdig valgt")

            elif (choise > stop or choise < start):
                print(f"loddene må være mellom {start} og {stop}") """


def chose_winner(font, screen, bg, width):
    global ranking
    winners = 1 #math.ceil(antall_spillere/2)
    winner = 0
    teller = 0
    for i in range(21):
        remove_one_number(font, screen, bg, width, 1)

    while winner < winners:
        teller += 1
        lottery_winners = []
        i=0
        text4 = ""

        while i < winners:
            i+=1
            tall = random.randint(1,len(numbers)-1)
            lottery_winners.append(numbers[tall])
            numbers.remove(numbers[tall])


        if teller % 5 == 0:
            remove_one_number(font, screen, bg, width, 1)
        
        elif teller == 3 or teller == 6:
            joker_card(font, screen, bg, width, 1)
            
        else:    
            print(f"vinnertallene er {lottery_winners}")
            for key, value in choises.items():
                for w in lottery_winners:
                    if w in choises.get(key):
                        winner +=1
                        print(f"{winner}. plass er {key} med vinnertallet {w}")
                        info = (winner, key, w)
                        print(key)
                        ranking.add(info)
                        print("inne")
                            
                    else:
                        text4 = " Ingen hadde det loddet"
                        screen.blit(bg,(0,0))
                        text2 = f"Vinnertallene er: {lottery_winners}"
                        bli_text_to_screen(text2,font, screen, bg, width, 100)
                        show_tickets(font, screen, bg)
                        py.display.update()
        time.sleep(1)
        if winner != winners:
            text3 = "EN TIL, EN TIL, VI REKKER EN TIL"
            bli_text_to_screen(text4,font, screen, bg, width, 200)
            py.display.update()
            time.sleep(1)
            bli_text_to_screen(text3,font, screen, bg, width, 300)
            show_tickets(font, screen, bg)
            py.display.update()
            print(text3)
            time.sleep(1)



def show_pygame():
    py.mixer.music.load("python_version/filer/En_Til.mp3")
    py.mixer.music.set_volume(1)
    py.mixer.music.play()
    teller = 0
    size = width, hight = 1500, 1000
    font = py.font.Font('freesansbold.ttf', 40)
    screen = py.display.set_mode(size)
    bg = py.image.load("python_version/filer/vinbg.jpg")
    has_won = False
    py.display.set_caption('VINLOTTERIET')

    while True:
        for event in py.event.get():
            if event.type == py.QUIT: sys.exit()
            if has_won == False:
                chose_winner(font, screen, bg, width)
                has_won = True
            if teller == 0:
                the_prankster(font, screen, bg, width, hight)
                teller +=1
                print(ranking)
            if teller != 0:
                blit_winner(font,screen,bg,width, hight)
                
            
            
def bli_text_to_screen(text,font, screen, bg, width, hight = 0):
    colour1 = (255,255,255)
    colour2 = (0,0,0)
    text = font.render(text, True, colour1, colour2)
    textREct = text.get_rect()
    textREct.center = (width // 2, hight)
    #screen.blit(bg,(0,0))
    screen.blit(text, textREct)        
            

        
def blit_winner(font, screen, bg, width, hight):
    screen.blit(bg,(0,0))
    for info in ranking:
        text = f"{info[0]}. plass til {info[1].upper()} med vinnertallet {info[2]}"
        bli_text_to_screen(text,font, screen, bg, width, 100*info[0])
    show_tickets(font, screen, bg)
    py.display.update()
    #time.sleep(2)

def show_tickets(font, screen, bg):
    i = 0
    for key, value in choises.items():
        i+=1
        text = f"{key}: {value}"
        bli_text_to_screen(text,font, screen, bg, 350, 100*i)

def remove_one_number(font, screen, bg, width, sleep):
    tall1 = random.randint(0,len(numbers)-1)
    text1 = f"[{tall1}]"
    for key, value in choises.items():
        if tall1 in value:
            value.remove(tall1)
    screen.blit(bg,(0,0))
    bli_text_to_screen("Nå fjernes ",font, screen, bg, width, 100)
    bli_text_to_screen(text1,font, screen, bg, width, 200)
    show_tickets(font, screen, bg)
    py.display.update()
    numbers.remove(numbers[tall1])
    time.sleep(sleep)
    screen.blit(bg,(0,0))

def joker_card(font, screen, bg, width, sleep):
    text1 = f"Joker runde, vent i spenning på hva som skjer"
    screen.blit(bg,(0,0))
    bli_text_to_screen(text1,font, screen, bg, width+100, 100)
    show_tickets(font, screen, bg)
    py.display.update()
    time.sleep(10)
    spiller1 = list(choises.keys())[random.randint(0,len(choises)-1)]
    spiller2 = list(choises.keys())[random.randint(0,len(choises)-1)]
    while spiller1 == spiller2:
        spiller2 = list(choises.keys())[random.randint(0,len(choises)-1)]
    numb1 = choises[spiller1]
    choises[spiller1] = choises[spiller2]
    choises[spiller2] = numb1
    text2 = f"{spiller1} sine lodd ble byttet med {spiller2}"
    bli_text_to_screen(text2,font, screen, bg, width, 200)
    show_tickets(font, screen, bg)
    py.display.update()
    time.sleep(sleep)
    screen.blit(bg,(0,0))
    
    

def the_prankster(font, screen, bg, width, hight):
    text1 = "1. plass til VEBJØRN selvfølgelig!!!"
    text2 = "HAHAHAHA LURTE DERE, JEG TAR VINEN SELV"
    screen.blit(bg,(0,0))
    bli_text_to_screen(text1,font, screen, bg, width, hight//2)
    bli_text_to_screen(text2,font, screen, bg, width, (hight//2)+100)
    show_tickets(font, screen, bg)
    py.display.update()
    time.sleep(1)

if __name__ == "__main__":
    #get_ready()
    show_pygame()
    
