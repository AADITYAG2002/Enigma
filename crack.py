from settings import *
import enigma_bare

x = enigma_bare.Enigma.encrypt(2,6,3,'az bh','testing')
print(x)