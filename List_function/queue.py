l = []
while True:
    c = int(input(''' 
                1 Push Elements
                2 Pop First Element
                3 Front Element
                4 Last Element
                5 Display Elements
                6 Exits
        '''))
    if c==1:
        n = input("Enter the value:")
        l.append(n)
        print(l)
    elif c==2:
        if len(l) == 0:
            print("Empty Queue")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("The First element is:",l[0])
            print(l)
    elif c==4:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("The Last element is:",l[-1])
            print(l)
    elif c==5:
        print("Display Queue",l)
    elif c==6:
        break
    else:
        print("invalide choice")