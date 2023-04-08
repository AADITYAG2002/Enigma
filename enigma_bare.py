from settings import *

class Enigma:
    def __init__(self):
        shift_1 = True
        shift_2 = False
        shift_3 = False      
        rotor_settings = input("enter values: ").upper().split(' ')
        rotor_settings = [int(x) for x in rotor_settings]

        print("rotor setting: ", rotor_settings)

        rotor_1 = Rotor(self,ROTOR_1,rotor_settings[2])
        rotor_2 = Rotor(self,ROTOR_2,rotor_settings[1])
        rotor_3 = Rotor(self,ROTOR_3,rotor_settings[0])

        PLUGS = input("enter plug pairs: ").upper()
        PLUGS = [] if PLUGS == '' else PLUGS.split()

        txt = input("enter text: ").upper()

        for x in txt:
            for pair in PLUGS:
                if pair[0]== x:
                    enc_0 = pair[1]
                    break
                elif pair[1] == x:
                    enc_0 = pair[0]
                    break
                else:
                    enc_0 = x
                    break
            else:
                enc_0 = x

            enc_1 = rotor_1.run_through(enc_0,True)
            enc_2 = rotor_2.run_through(enc_1,True)
            enc_3 = rotor_3.run_through(enc_2,True)
            enc_4 = REFLECTOR[ord(enc_3)-ord('A')]
            enc_5 = rotor_3.run_through(enc_4,False)
            enc_6 = rotor_2.run_through(enc_5,False)
            enc_7 = rotor_1.run_through(enc_6,False)
            for pair in PLUGS:
                if pair[0] == enc_7:
                    enc_8 = pair[1]
                    break
                elif pair[1] == enc_7:
                    enc_8 = pair[0]
                    break
                else:
                    enc_8 = enc_7
                    break
            else:
                enc_8 = enc_7
            
            # print(input,enc_0,enc_1,enc_2,enc_3,enc_4,enc_5,enc_6,enc_7,enc_8)
            print(enc_8,end='')

            shift_2 = True if rotor_1.value == 25 else False
            shift_3 = True if rotor_2.value == 25 and rotor_1.value == 25 else False
            rotor_1.update(shift_1)
            rotor_2.update(shift_2)
            rotor_3.update(shift_3)

class Letter:
    def __init__(self,enigma,letter):
        self.enigma = enigma
        self.letter = letter

class Rotor:
    def __init__(self,enigma,rotor,value):
        self.enigma = enigma
        self.rotor = rotor
        self.value = value

    def update(self,shift):
        if shift:
            self.value += 1
            self.value %= 26

    def setting(self,mouse_pos,click):
        pass

    def run_through(self,letter,forward):
        if forward:
            rotorshift = ((ord(letter) - ord('A')) + self.value) % 26
            return self.rotor[rotorshift]
        
        else:
            rotorshift = chr((self.rotor.find(letter) - self.value) % 26 + ord('A'))
            return rotorshift

class Plug_Port:
    def __init__(self,enigma,letter):
        self.enigma = enigma
        self.letter = letter



# TODO add plugs
class Plug:
    def __init__(self,enigma,letter):
        self.enigma = enigma
        self.letter = letter

if __name__ == '__main__':
    Enigma()