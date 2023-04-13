txt = ""

enc_text = "WNRLDXK"

plug_set = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for t in enc_text:
    for s in plug_set:
        if s != ' ':
            txt += t + s + ' '