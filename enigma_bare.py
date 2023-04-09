from settings import *

class Enigma:
    def encrypt(r3,r2,r1,plugs,txt):
        shift_1 = True
        shift_2 = False
        shift_3 = False      

        rotor_1 = Rotor(ROTOR_1,r3)
        rotor_2 = Rotor(ROTOR_2,r2)
        rotor_3 = Rotor(ROTOR_3,r1)

        PLUGS = plugs
        PLUGS = [] if PLUGS == '' else PLUGS.split()

        enc_txt = ""
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
            
            enc_txt += enc_8

            shift_2 = True if rotor_1.value == 25 else False
            shift_3 = True if rotor_2.value == 25 and rotor_1.value == 25 else False
            rotor_1.update(shift_1)
            rotor_2.update(shift_2)
            rotor_3.update(shift_3)

        return enc_txt
        


class Rotor:
    def __init__(self,rotor,value):
        self.rotor = rotor
        self.value = value

    def update(self,shift):
        if shift:
            self.value += 1
            self.value %= 26

    def run_through(self,letter,forward):
        if forward:
            rotorshift = ((ord(letter) - ord('A')) + self.value) % 26
            return self.rotor[rotorshift]
        
        else:
            rotorshift = chr((self.rotor.find(letter) - self.value) % 26 + ord('A'))
            return rotorshift


if __name__ == '__main__':
    Enigma(2,6,3,'az bh','testing')