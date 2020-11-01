import math
import random
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
P = math.pow(10, -4)
V = 10
T = 5/7
passwordsPerWeek = V * 7
S = (passwordsPerWeek * T) / P
A = len(alphabet)
L = 0
while math.pow(A, L) <= S:
    L += 1
password=''
for i in range(L):
    password=password+alphabet[random.randint(0, A-1)]
print("passwordord : \n",password)
print("passwordord hacking time",(A**L*P)/passwordsPerWeek)
