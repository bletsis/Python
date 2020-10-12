import random

print()
zari = {}

for i in range(1, 6+1):
    zari[i] = 0
n = 1000000
for _ in range(n):
    x = random.randint(1,6)
    zari[x] += 1

print("Επαναλήψεις των τιμών σε " + str(n) + " ρίψεις του ζαριού:\n" + str(zari) + "\n")
m = n/100
for i in range(1, 6+1):
    zari[i] /= m
print("Ποσοστά % επαναλήψεων των τιμών σε " + str(n) + " ρίψεις του ζαριού:\n" + str(zari))
