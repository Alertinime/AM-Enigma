
rotor_1 = ["A","Q","W","Z","S","X","E","D","C","R","F","V","T","G","B","Y","H","N","U","J","I","K","O","L","P","M"]
rotor_2 = ["P","O","I","U","Y","T","R","E","Z","A","M","L","K","J","H","G","F","D","S","Q","N","B","V","C","X","W"]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def choice():
    choice = input("choice: code(c)/uncode(u)")
    if choice == "c":
        let = input("parametre for rotor 1? ")
        parametre(let,rotor_1)
        let = input("parametre for rotor 2? ")
        parametre(let,rotor_2)
        code()
    elif choice == "u":
        let = input("parametre for rotor 1? ")
        parametre(let,rotor_1)
        let = input("parametre for rotor 2? ")
        parametre(let,rotor_2)
        uncode()
def code():
    message = list(input("message? "))
    msg = ""
    for let in message:
        if let != " ":
            numlet = rotor(let, alphabet)
            futur = rotor_1[numlet]
            numle = rotor(futur, alphabet2)
            futu = rotor_2[numle]
            msg = msg + futu
            lettre = rotor_1[0]
            rotor_1.remove(lettre)
            rotor_1.append(lettre)
            lettre = rotor_2[0]
            rotor_2.remove(lettre)
            rotor_2.append(lettre)
        else:
            msg = msg + " "
    print(msg)

def parametre(let, rotor):
    a = 0
    while a == 0:
        one  = rotor[0]
        if one == let:
            a = 1
        else:
            rotor.remove(one)
            rotor.append(one)
    print(rotor)
        


def rotor(let, alph):
    i2 = 0
    for x in alph:
        if x == let:
            numlet = i2
        else:
            i2 += 1
    i2 = 0
    return numlet

def unrote(num, alph):
    i = 0
    for x in alph:
        if num == i:
            return x
        else:
            i += 1
    i = 0
def uncode():
    message = list(input("message? "))
    msg = ""
    for let in message:
        if let != " ":
            numlet = rotor(let, rotor_2)
            let = unrote(numlet, alphabet2)
            numle = rotor(let, rotor_1)
            let = unrote(numlet, alphabet2)
            futu = alphabet[numle]
            msg = msg + futu

            lettre = rotor_1[0]
            rotor_1.remove(lettre)
            rotor_1.append(lettre)
            lettre = rotor_2[0]
            rotor_2.remove(lettre)
            rotor_2.append(lettre)
        else:
            msg = msg + " "
    print(msg)

choice()
