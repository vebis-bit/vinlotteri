import random
import sys
import time
import pygame as py
import os
from python_version.button import Button


py.init()
py.mixer.init()
start = 1
stop = 20
length = 2
choises = {
    "Erland": [],
    "Jonas": [],
    "Vebjorn":[],
    "Amund": [],
    "Aslak": [],
    "Andreas": [],
}

ranking = set() # (plass, navn, vinnertall)
antall_spillere = len(choises) # antall spillere
numbers = [] # alle tallene
test = [] # alle tallene

# lager en liste med alle tallene
for i in range(start,stop):
    numbers.append(i)
    test.append(i)

# lager en liste med alle tallene
for key, value in choises.items():
    for i in range(0,length):
        choises[key].append(test.pop(random.randint(0,len(test)-1)))

NUMBERS = 0
# lager en liste med alle tallene
for i in choises.values():
    NUMBERS += len(i)


# velger en vinner og kjører hele greia
def chose_winner(font, screen, bg, width):
    # TODO: fiks alt dette blir for dumt
    global ranking
    global NUMBERS
    winners = 2 
    winner = 0
    teller = 0
    sleep = 1
    long_sleep = 1

    while NUMBERS > 2:
        teller += 1
        lottery_winners = []
        i=0
        text4 = ""

        if teller % 1 == 0:
            remove_one_number(font, screen, bg, width, long_sleep)
            for key, value in choises.items():
                if value == []:
                    text4 = f"{key} er ute av spillet"
                    bli_text_to_screen(text4,font, screen, bg, width, 200)
                    show_tickets(font, screen, bg)
                    py.display.update()
                    time.sleep(sleep)
                    choises.pop(key)
                    break

        if teller % random.randint(3,9) == 0:
            print("joker")
            joker_card(font, screen, bg, width, long_sleep)

        if NUMBERS < 3:
            for i in choises.values():
                if len(i) > 0:
                    for items in i: 
                        lottery_winners.append(items)
            index = random.randint(0,1000)%2
            print(index)
            winner = lottery_winners.pop(index)
            loser = lottery_winners.pop(0)
            print(winner,loser)
            for key, value in choises.items():
                if winner in value:  
                    tvinner = f"1. premie går til {key}"
                if loser in value:
                    taper = f"2. premie går til {key}"
            bli_text_to_screen(tvinner,font, screen, bg, width, 100)
            bli_text_to_screen(taper,font, screen, bg, width, 200)
            show_tickets(font, screen, bg)
            py.display.update()
            time.sleep(10000)
            
        time.sleep(sleep)
        if winner != winners:
            text3 = "EN TIL, EN TIL, VI REKKER EN TIL"
            bli_text_to_screen(text4,font, screen, bg, width, 200)
            show_tickets(font, screen, bg)
            py.display.update()
            print(text4)
            time.sleep(sleep)
            bli_text_to_screen(text3,font, screen, bg, width, 300)
            show_tickets(font, screen, bg)
            py.display.update()
            print(text3)
            time.sleep(long_sleep)


# viser vinneren og alt annet i pygame vinduet
def show_pygame():
    timer = time.time()
    print(os.path.abspath(os.getcwd()))
    py.mixer.music.load(os.path.abspath(os.getcwd())+"/python_version/filer/En_Til.mp3")
    py.mixer.music.set_volume(1)
    py.mixer.music.play(-1)
    teller = 0
    size = width, hight = 3000, 1500
    font = py.font.Font('freesansbold.ttf', 40)
    screen = py.display.set_mode(size)
    bg = py.image.load(os.path.abspath(os.getcwd())+"/python_version/filer/vinbg.jpg")
    has_won = False
    py.display.set_caption('VINLOTTERIET')

    while True:
        for event in py.event.get():
            if event.type == py.QUIT: 
                sys.exit()
            if has_won == False:
                chose_winner(font, screen, bg, width)
                has_won = True
            if teller == 0:
                the_prankster(font, screen, bg, width, hight)
                teller +=1
                print(ranking)
            if teller != 0:
                blit_winner(font,screen,bg,width, hight)
                print(time.time()-timer)
                
            if teller >= 2:
                button = Button("text",(width,hight),font=30,bg="navy")
                button.click2(event)
                button.show()
                py.display.update()
            
# skriver ut tekst på skjermen
def bli_text_to_screen(text,font, screen, bg, width, hight = 0):
    colour1 = (255,255,255)
    colour2 = (0,0,0)
    text = font.render(text, True, colour1, colour2)
    textREct = text.get_rect()
    textREct.center = (width // 2, hight)
    screen.blit(text, textREct)        
            

# skriver ut vinneren til skjermen 
def blit_winner(font, screen, bg, width, hight):
    screen.blit(bg,(0,0))
    for info in ranking:
        text = f"{info[0]}. plass til {info[1].upper()} med vinnertallet {info[2]}"
        bli_text_to_screen(text,font, screen, bg, width, 100*info[0])
    show_tickets(font, screen, bg)
    py.display.update()
    time.sleep(2)

# skriver ut alle loddene til skjermen
def show_tickets(font, screen, bg):
    i = 0
    for key, value in choises.items():
        i+=1
        text = f"{key}: {value}"
        bli_text_to_screen(text,font, screen, bg, 1000, 100*i)

# fjerner et tall fra alle loddene
def remove_one_number(font, screen, bg, width, sleep):
    global NUMBERS
    print(NUMBERS)
    tall1 = numbers[random.randint(0,len(numbers)-1)]
    text1 = f"[{tall1}]"
    for key, value in choises.items():
        if tall1 in value:
            value.remove(tall1)
            NUMBERS -= 1
    screen.blit(bg,(0,0))
    bli_text_to_screen("Nå fjernes ",font, screen, bg, width, 100)
    bli_text_to_screen(text1,font, screen, bg, width, 200)
    show_tickets(font, screen, bg)
    py.display.update()
    numbers.remove(tall1)
    time.sleep(sleep)
    screen.blit(bg,(0,0))
# bytter to lodd med hverandre
def joker_card(font, screen, bg, width, sleep):
    done = False
    text1 = f"Joker runde, vent i spenning på hva som skjer"
    screen.blit(bg,(0,0))
    bli_text_to_screen(text1,font, screen, bg, width+100, 100)
    show_tickets(font, screen, bg)
    py.display.update()
    time.sleep(sleep)
    while not done:
        spiller1, spiller2 = chose_random_player()
        if len(spiller1) > 0 and len(spiller2) > 0:
            numb1 = choises[spiller1]
            choises[spiller1] = choises[spiller2]
            choises[spiller2] = numb1
            text2 = f"{spiller1} sine lodd ble byttet med {spiller2}"
            bli_text_to_screen(text2,font, screen, bg, width, 200)
            show_tickets(font, screen, bg)
            py.display.update()
            time.sleep(sleep)
            screen.blit(bg,(0,0))
            done = True
        else:
            pass

def chose_random_player():
    spiller1 = list(choises.keys())[random.randint(0,len(choises)-1)]
    spiller2 = list(choises.keys())[random.randint(0,len(choises)-1)]
    while spiller1 == spiller2:
        spiller2 = list(choises.keys())[random.randint(0,len(choises)-1)]
    return spiller1, spiller2

# en liten spøk
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
    show_pygame()
    
