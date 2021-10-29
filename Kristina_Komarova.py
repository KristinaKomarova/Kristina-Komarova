from keyboard import*
print("kivi, käärid, paber")
while True:
    try:
        if read_key()=='k':
            print("oli valitud kivi")
            break
    except:
            ValueError
m=3
while m not in [1,2]:
    try:
        m=int(input("kellega mängime? \n1-inimesega \n2-robotiga"))
    except:
        ValueError
v1=(["kivi","käärid","paber"])
v2=(["kivi","käärid","paber"])
if m==1:   
    while True:
        print(" kas mängime? esc-välja, enter- mängime")
        if read_key()=='esc':
            break
        elif read_key()=='enter':
            p1=choice(v1)
            print("esimene bot:",p1)
            p2=choice(v2)
            print("teine bot:",p2)
            if p1==p2:
                print("viik")
            elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
                print("võitis 1")
            else:
                print("võitis 2")