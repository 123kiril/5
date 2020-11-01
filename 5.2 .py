import stdiomask

alphabet = "abcdefghijklmnopqrstuvwxyz"
firstw = input("Input first word: ")
secondw = input("Input second word: ")
thirdw = input("Input third word: ")
passw=""
passw+=alphabet[(alphabet.index(secondw[0]) + 1 % (len(alphabet) - 1))]
passw+=alphabet[(alphabet.index(secondw[0]) + 2 % (len(alphabet) - 1))]
passw+=alphabet[(alphabet.index(secondw[4]) - 1 % (len(alphabet) - 1))]
if len(thirdw)% 2 != 0:
    passw+=alphabet[(alphabet.index(thirdw[2]) + 1 % (len(alphabet) - 1))]
else:
    if alphabet.index(thirdw[len(thirdw)//2])>alphabet.index(thirdw[len(thirdw)//2-1]):
        passw+=alphabet[(alphabet.index(thirdw[len(thirdw)//2]) - 1 % (len(alphabet) - 1))]
    else:
        passw+=alphabet[(alphabet.index(thirdw[len(thirdw)//2-1]) - 1 % (len(alphabet) - 1))]
passw+=alphabet[((len(firstw)+len(secondw)-4)% 26)]
print(passw)
userPassw=stdiomask.getpass()
if userPassw==passw:
    print("Access allow")
else:
    print("Access denied")
