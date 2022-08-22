from ast import In
import random
import sys
import time
import pygame as py
from button import Button
from chose_winner import ChoseWinner
from input_box import InputBox

py.init()
py.mixer.init()
py.mixer.music.load("python_version/filer/En_Til.mp3")
py.mixer.music.set_volume(1)
py.display.set_caption('VINLOTTERIET')

class MainWindow():
    def __init__(self, width=1200, height=1000):
        self.size = self.width, self.height = width, height
        self.font = py.font.Font('freesansbold.ttf', 40)
        self.screen = py.display.set_mode(self.size)
        self.bg = py.image.load("python_version/filer/vinbg.jpg")
        self.has_won = False

        self.start = 1
        self.stop = 101
        self.numbers = []
        self.make_list(self.start, self.stop)

        self.choises = {
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
        self.ranking = set()
        self.number_of_players = len(self.choises)
        self.list_of_tickets = []


        self.ch_w = ChoseWinner(self,1)
        self.person = ""
        
        
    def run_pygame(self):
        self.input_box()
        button1 = self.make_button(" Start ", 600, 100)
        while True:
            for event in py.event.get():
                if event.type == py.QUIT: sys.exit()
                button1.click2(event)
                button1.show()
                py.display.update()


    def make_button(self, text,width=10,height=100, color="navy", starting="Starting"):
        return Button(
                self,
                text,
                (width,height),
                font=30,
                bg="navy",
                feedback=starting)
    
    def add_person(self,person):
        self.person = person
        
    def add_ticket(self,ticket):
        for key in self.choises.keys():
            if (self.person.lower() == key.lower()) and (self.check_if_valid(ticket)):
                self.choises[key].append(ticket)
                self.list_of_tickets.append(ticket)
        if self.person.lower() not in self.choises.keys():
            self.choises[self.person] = [ticket]

    def input_box(self):
        clock = py.time.Clock()
        input_box1 = InputBox(self,600, 200, 140, 32, "p")
        input_box2 = InputBox(self,600, 300, 140, 32, "t")
        input_boxes = [input_box1, input_box2]
        done = False

        while not done:
            for event in py.event.get():
                if event.type == py.QUIT:
                    done = True
                if event.type == py.K_ESCAPE:
                    done = True
                for box in input_boxes:
                    box.handle_event(event)
            for box in input_boxes:
                box.update()

            self.screen.fill((30, 30, 30))
            for box in input_boxes:
                box.draw(self.screen)

            py.display.flip()
            clock.tick(30)


    def chose_the_winner(self):
        py.mixer.music.play()
        self.ch_w.run_chose_winner()
    
    def make_list(self, start, stop):
        for i in range(start,stop):
            self.numbers.append(i)

    def check_if_valid(self, number):
        if (number in self.numbers) and (number not in self.list_of_tickets):
            return True
        return False

    def bli_text_to_screen(self,text, height):
        colour1 = (255,255,255)
        colour2 = (0,0,0)
        text = self.font.render(text, True, colour1, colour2)
        textREct = text.get_rect()
        textREct.center = (self.width // 2, height)
        #self.screen.blit(self.bg,(0,0)) 
        self.screen.blit(text, textREct)



if __name__ == "__main__":
    main_window = MainWindow()
    main_window.run_pygame()