plugs = []

 
while True:
    num = input("enter: ")
    for set in plugs:
        if len(set) == 2:
            continue
        else:
            set.append(num)
            break
    else:
        plugs.append([num])
    
    
    for pair in plugs:
        if len(pair) == 2:
            if pair[0] == num:
                print(pair[1])
                break
            elif pair[1] == num :
                print(pair[0])
                break
            else:
                print(num)
                break
    else:
        print(num)