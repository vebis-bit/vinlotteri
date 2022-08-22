import random
import time
import pygame as py

class ChoseWinner():
    def __init__(self, parent, winners=1,):
        self.parent = parent
        self.short_sleep = 1
        self.long_sleep = 1

        self.ranking = self.parent.ranking
        self.number_of_winners = winners
        self.counter = 0
        self.fun_twist = 0
    
    def run_chose_winner(self):
        for i in range(21):
            self.remove_one_number(self.parent.font, self.parent.screen, self.parent.bg, self.parent.width, self.short_sleep)

        while self.counter < self.number_of_winners:
            self.fun_twist += 1
            lottery_winners = []
            i=0
            text4 = ""
            while i < self.number_of_winners:
                i+=1
                tall = random.randint(1,len(self.parent.numbers)-1)
                lottery_winners.append(self.parent.numbers[tall])
                self.parent.numbers.remove(self.parent.numbers[tall])


            if self.fun_twist % 5 == 0:
                self.remove_one_number(self.parent.font, self.parent.screen, self.parent.bg, self.parent.width, self.short_sleep)
            
            elif self.fun_twist == 3 or self.fun_twist == 6:
                self.joker_card(self.parent.font, self.parent.screen, self.parent.bg, self.parent.width, self.long_sleep)
                
            else:    
                print(f"vinnertallene er {lottery_winners}")
                for key, value in self.parent.choises.items():
                    for w in lottery_winners:
                        if w in self.parent.choises.get(key):
                            self.counter +=1
                            print(f"{self.counter}. plass er {key} med vinnertallet {w}")
                            info = (self.counter, key, w)
                            print(key)
                            self.parent.ranking.add(info)
                            print("inne")
                                
                        else:
                            text4 = " Ingen hadde det loddet"
                            self.parent.screen.blit(self.parent.bg,(0,0))
                            text2 = f"Vinnertallene er: {lottery_winners}"
                            self.bli_text_to_screen(text2,self.parent.font, self.parent.screen, self.parent.bg, self.parent.width, 100)
                            self.show_tickets(self.parent.font, self.parent.screen, self.parent.bg)
                            py.display.update()
            time.sleep(self.short_sleep)
            if self.counter != self.number_of_winners:
                text3 = "EN TIL, EN TIL, VI REKKER EN TIL"
                self.bli_text_to_screen(text4,self.parent.font, self.parent.screen, self.parent.bg, self.parent.width, 200)
                py.display.update()
                time.sleep(self.short_sleep)
                self.bli_text_to_screen(text3,self.parent.font, self.parent.screen, self.parent.bg, self.parent.width, 300)
                self.show_tickets(self.parent.font, self.parent.screen, self.parent.bg)
                py.display.update()
                print(text3)
                time.sleep(self.long_sleep)
    
    def remove_one_number(self,font, screen, bg, width, sleep):
        tall1 = random.randint(0,len(self.parent.numbers)-1)
        text1 = f"[{tall1}]"
        for key, value in self.parent.choises.items():
            if tall1 in value:
                value.remove(tall1)
        screen.blit(bg,(0,0))
        self.bli_text_to_screen("Nå fjernes ",font, screen, bg, width, 100)
        self.bli_text_to_screen(text1,font, screen, bg, width, 200)
        self.show_tickets(font, screen, bg)
        py.display.update()
        self.parent.numbers.remove(self.parent.numbers[tall1])
        time.sleep(sleep)
        screen.blit(self.parent.bg,(0,0))
    
    def bli_text_to_screen(self,text,font, screen, bg, width, hight):
        colour1 = (255,255,255)
        colour2 = (0,0,0)
        text = font.render(text, True, colour1, colour2)
        textREct = text.get_rect()
        textREct.center = (width // 2, hight)
        #screen.blit(bg,(0,0))
        screen.blit(text, textREct)
    
    def show_tickets(self,font, screen, bg):
        i = 0
        for key, value in self.parent.choises.items():
            i+=1
            text = f"{key}: {value}"
            self.bli_text_to_screen(text,font, screen, bg, 350, 100*i)

    def joker_card(self,font, screen, bg, width, sleep):
        text1 = f"Joker runde, vent i spenning på hva som skjer"
        screen.blit(bg,(0,0))
        self.bli_text_to_screen(text1,font, screen, bg, width+100, 100)
        self.show_tickets(font, screen, bg)
        py.display.update()
        time.sleep(2*sleep)
        spiller1 = list(self.parent.choises.keys())[random.randint(0,len(self.parent.choises)-1)]
        spiller2 = list(self.parent.choises.keys())[random.randint(0,len(self.parent.choises)-1)]
        while spiller1 == spiller2:
            spiller2 = list(self.parent.choises.keys())[random.randint(0,len(self.parent.choises)-1)]
        numb1 = self.parent.choises[spiller1]
        self.parent.choises[spiller1] = self.parent.choises[spiller2]
        self.parent.choises[spiller2] = numb1
        text2 = f"{spiller1} sine lodd ble byttet med {spiller2}"
        self.bli_text_to_screen(text2,font, screen, bg, width, 200)
        self.show_tickets(font, screen, bg)
        py.display.update()
        time.sleep(sleep)
        screen.blit(bg,(0,0))
