l = []
while True:
    c = int(input(''' 
            1 Push Elements
            2 Pop Elements
            3 Peek Elements
            4 Display Elements
            5 Exits
    '''))
    if c==1:
        n = input("Enter the value:")
        l.append(n)
        print(l)
    elif c==2:
        if len(l) == 0:
            print("Empty List")
        else:
            p = l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l) == 0:
            print("Empty List")
        else:
            print("The last element is:",l[-1])
            print(l)
    elif c==4:
        print("Display List",l)
    elif c==5:
        break
    else:
        print("invalide choice")
      


