from settings import *
import enigma_bare

# 25 4 1 || ka ti || aaditya => WNRLDXK

enc_text = "aaditya"
plugs = "ka ti"
rotors = [25,4,1]
txt = enigma_bare.Enigma.encrypt(rotors[0],rotors[1],rotors[2],plugs,enc_text)
print(txt)