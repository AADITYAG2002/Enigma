import pygame as pg
from settings import *

class Enigma:
    
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1080,600))
        self.clock = pg.time.Clock()

        rotor_1 = Rotor(self,ROTOR_1,0,580,20)
        rotor_2 = Rotor(self,ROTOR_2,0,540,20)
        rotor_3 = Rotor(self,ROTOR_3,0,500,20)

        shift_1 = True
        shift_2 = False
        shift_3 = False

        LETTERS = [
                Letter(self,"A",120,150),
                Letter(self,"B",586,200),
                Letter(self,"C",382,200),
                Letter(self,"D",324,150),
                Letter(self,"E",266,100),
                Letter(self,"F",426,150),
                Letter(self,"G",528,150),
                Letter(self,"H",630,150),
                Letter(self,"I",776,100),
                Letter(self,"J",732,150),
                Letter(self,"K",834,150),
                Letter(self,"L",936,150),
                Letter(self,"M",790,200),
                Letter(self,"N",688,200),
                Letter(self,"O",878,100),
                Letter(self,"P",980,100),
                Letter(self,"Q", 62,100),
                Letter(self,"R",368,100),
                Letter(self,"S",222,150),
                Letter(self,"T",470,100),
                Letter(self,"U",674,100),
                Letter(self,"V",484,200),
                Letter(self,"W",164,100),
                Letter(self,"X",280,200),
                Letter(self,"Y",572,100),
                Letter(self,"Z",178,200),
        ]

        PLUGBOARD = [
                Plug_Port(self,"A",120,400),
                Plug_Port(self,"B",586,500),
                Plug_Port(self,"C",382,500),
                Plug_Port(self,"D",324,400),
                Plug_Port(self,"E",266,300),
                Plug_Port(self,"F",426,400),
                Plug_Port(self,"G",528,400),
                Plug_Port(self,"H",630,400),
                Plug_Port(self,"I",776,300),
                Plug_Port(self,"J",732,400),
                Plug_Port(self,"K",834,400),
                Plug_Port(self,"L",936,400),
                Plug_Port(self,"M",790,500),
                Plug_Port(self,"N",688,500),
                Plug_Port(self,"O",878,300),
                Plug_Port(self,"P",980,300),
                Plug_Port(self,"Q", 62,300),
                Plug_Port(self,"R",368,300),
                Plug_Port(self,"S",222,400),
                Plug_Port(self,"T",470,300),
                Plug_Port(self,"U",674,300),
                Plug_Port(self,"V",484,500),
                Plug_Port(self,"W",164,300),
                Plug_Port(self,"X",280,500),
                Plug_Port(self,"Y",572,300),
                Plug_Port(self,"Z",178,500),
        ]
        PLUGS = []

        while True:
            mouse_pos = pg.mouse.get_pos()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if 900 <= mouse_pos[0] <= 950 and 500 <= mouse_pos[1] <= 520:
                        PLUGS = []

                    rotor_1.setting(mouse_pos,True)
                    rotor_2.setting(mouse_pos,True)
                    rotor_3.setting(mouse_pos,True)
                    for port in PLUGBOARD:
                        if port.corner[0][0] <= mouse_pos[0] <= port.corner[1][0] and port.corner[0][1] <= mouse_pos[1] <= port.corner[1][1]:
                            plug = Plug(self,port.letter,port.corner[0][0],port.corner[0][1])
                            for pair in PLUGS:
                                if len(pair) == 2:
                                    continue
                                else:
                                    pair.append(plug)
                                    break
                            else:
                                PLUGS.append([plug])

                if event.type == pg.KEYDOWN:
                    input = pg.key.name(event.key).upper()

                    for pair in PLUGS:
                        if pair[0].letter == input:
                            enc_0 = pair[1].letter
                            break
                        elif pair[1].letter == input:
                            enc_0 = pair[0].letter
                            break
                        else:
                            enc_0 = input
                            break
                    else:
                        enc_0 = input

                    enc_1 = rotor_1.run_through(enc_0,True)
                    enc_2 = rotor_2.run_through(enc_1,True)
                    enc_3 = rotor_3.run_through(enc_2,True)
                    enc_4 = REFLECTOR[ord(enc_3)-ord('A')]
                    enc_5 = rotor_3.run_through(enc_4,False)
                    enc_6 = rotor_2.run_through(enc_5,False)
                    enc_7 = rotor_1.run_through(enc_6,False)
                    for pair in PLUGS:
                        if pair[0].letter == enc_7:
                            enc_8 = pair[1].letter
                            break
                        elif pair[1].letter == enc_7:
                            enc_8 = pair[0].letter
                            break
                        else:
                            enc_8 = enc_7
                            break
                    else:
                        enc_8 = enc_7

                    light = ord(enc_8)-ord('A')
                    
                    print(input,enc_0,enc_7,enc_8)
                    # print(enc_8,end='')
                    LETTERS[light].draw(True)

                    shift_2 = True if rotor_1.value == 25 else False
                    shift_3 = True if rotor_2.value == 25 and rotor_1.value == 25 else False
                    rotor_1.update(shift_1)
                    rotor_2.update(shift_2)
                    rotor_3.update(shift_3)
        
            pg.display.flip()
            self.clock.tick(10)
            self.screen.fill((0,0,0))

            rotor_1.draw()
            rotor_2.draw()
            rotor_3.draw()

            for i in range(26):
                LETTERS[i].draw(False)
            for port in PLUGBOARD:
                port.draw()
            for pair in PLUGS:
                if len(pair) == 2:
                    pair[0].draw()
                    pair[1].draw()
                    pg.draw.line(self.screen,(255,0,0),(pair[0].x,pair[0].y),(pair[1].x,pair[1].y))
                else:
                    pair[0].draw()
            
            pg.draw.rect(self.screen,(255,255,255),pg.Rect(900,500,50,20))
            font = pg.font.SysFont(None,30)
            label = font.render(str("clear"),1,(0,0,0))
            self.screen.blit(label, (900,500))



class Letter:
    def __init__(self,enigma,letter,x,y):
        self.enigma = enigma
        self.letter = letter
        self.x = x
        self.y = y
    
    def draw(self,light):
        if not light:
            pg.draw.circle(self.enigma.screen,(0,0,0),(self.x,self.y),20)
            font = pg.font.SysFont(None,40)
            bulb = font.render(str(self.letter),1,(255,255,255))
            self.enigma.screen.blit(bulb, (self.x-10,self.y-12))
        else:
            pg.draw.circle(self.enigma.screen,(255,255,255),(self.x,self.y),20)
            font = pg.font.SysFont(None,40)
            bulb = font.render(str(self.letter),1,(0,0,0))
            self.enigma.screen.blit(bulb, (self.x-10,self.y-12))

class Rotor:
    def __init__(self,enigma,rotor,value,x,y):
        self.enigma = enigma
        self.rotor = rotor
        self.value = value
        self.x = x
        self.y = y

    def update(self,shift):
        if shift:
            self.value += 1
            self.value %= 26

    def setting(self,mouse_pos,click):
        if click:
            if (self.x - 5) <= mouse_pos[0] <= (self.x + 15) and (self.y - 10) <= mouse_pos[1] <= (self.y):
                self.value += 1
                self.value %= 26
            elif (self.x - 5) <= mouse_pos[0] <= (self.x + 15) and (self.y + 30) <= mouse_pos[1] <= (self.y + 40):
                self.value -= 1
                self.value %= 26
    
    def draw(self):
        font = pg.font.SysFont(None,40)
        rotortext = font.render(str(self.value),1,(255,255,255))
        self.enigma.screen.blit(rotortext, (self.x,self.y))

        pg.draw.polygon(self.enigma.screen,(255,255,255),[(self.x-5,self.y),
                                            (self.x + 5, self.y - 10),
                                            (self.x + 15, self.y)])
        pg.draw.polygon(self.enigma.screen,(255,255,255),[(self.x-5,self.y+30),
                                            (self.x + 5, self.y + 40),
                                            (self.x + 15, self.y+30)])

    def run_through(self,letter,forward):
        if forward:
            rotorshift = ((ord(letter) - ord('A')) + self.value) % 26
            return self.rotor[rotorshift]
        
        else:
            rotorshift = chr((self.rotor.find(letter) - self.value) % 26 + ord('A'))
            return rotorshift

class Plug_Port:
    def __init__(self,enigma,letter,x,y):
        self.enigma = enigma
        self.letter = letter
        self.x = x
        self.y = y
        self.corner = [(self.x,self.y),(self.x+14, self.y + 60)]

    def draw(self):
        pg.draw.circle(self.enigma.screen,(255,255,255),(self.x+7,self.y+20),5,1)
        pg.draw.circle(self.enigma.screen,(255,255,255),(self.x+7,self.y+40),5,1)
        font = pg.font.SysFont(None,30)
        label = font.render(str(self.letter),1,(255,255,255))
        self.enigma.screen.blit(label, (self.x,self.y-20))


# TODO add plugs
class Plug:
    def __init__(self,enigma,letter,x,y):
        self.enigma = enigma
        self.letter = letter
        self.x = x
        self.y = y

    def draw(self):
        pg.draw.rect(self.enigma.screen,(255,255,255),pg.Rect((self.x,self.y),(14,60)))

if __name__ == '__main__':
    Enigma()