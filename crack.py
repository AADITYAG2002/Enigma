import enigma_bare

# 25 4 1 || ka ti || aaditya => WNRLDXK

enc_text = "WNRLDXK"
pln_text = "AADITYA"
plugs = ""
initial_rotors = [0,0,0]
rotors = [0,0,0]

def check_plugs(plugs):
    plugs = plugs.split()
    for i in range(len(plugs)):
        for j in range(i+1,len(plugs)):
            if plugs[j].find(plugs[i][0]) != -1 or plugs[j].find(plugs[i][1]) != -1:
                return False
    return True

def rotor_shift(rotors):
    shift_2 = True if rotors[2] == 25 else False
    shift_3 = True if rotors[2] == rotors[1] == 25 else False
    rotors[2] += 1
    rotors[2] %= 26
    if shift_2:
        rotors[1] += 1
        rotors[1] %= 26
    if shift_3:
        rotors[0] += 1
        rotors[0] %= 26


i = 0
while i < len(enc_text):
    converted_letter = enigma_bare.Enigma.encrypt(rotors[0],rotors[1],rotors[2],plugs,enc_text[i])
    if converted_letter != pln_text[i]:
        plugs += converted_letter + pln_text[i] + ' '
        if check_plugs(plugs):
            rotor_shift(rotors)
            print(rotors,plugs) 
            i += 1
        else : 
            rotor_shift(initial_rotors)
            rotors = initial_rotors
            print(rotors, plugs)
            plugs = ''
# TODO: add the plug settings
            i = 0

print("plugs: ",plugs)
print(rotors)