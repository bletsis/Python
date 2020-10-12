words = ["Αεροπλανο", "μηλο", "Παραθυρο", "Σιδηροδρομος", "σκουληκομερμηγκοτρυπα",
         "Γαιδαρος", "Φαρασι", "Ανανας","Χριστουγεννα", "υποβρυχιο", "Αβγο",
         "ονειρο", "ωμεγα", "βελος", "Φιλος"]

words1 = []
words2 = []
word1 = []
for word in words:
    words1.append(word.capitalize())

words1.sort()

for i in range(len(words1)):
    for j in range(len(words)):
        if words[j][1:] == words1[i][1:]:
            words2.append(words[j])

print()
print(words2)
print()


for word in words1:
    word1 = []
    for letter in word:
        if letter == "α" or letter == "Α":
            num = 1
            word1.append(num)
        elif letter == "β" or letter == "Β":
            num = 2
            word1.append(num)
        elif letter == "γ" or letter == "Γ":
            num = 3
            word1.append(num)
        elif letter == "δ" or letter == "Δ":
            num = 4
            word1.append(num)
        elif letter == "ε" or letter == "Ε":
            num = 5
            word1.append(num)
        elif letter == "ζ" or letter == "Ζ":
            num = 6
            word1.append(num)
        elif letter == "η" or letter == "Η":
            num = 7
            word1.append(num)
        elif letter == "θ" or letter == "Θ":
            num = 8
            word1.append(num)
        elif letter == "ι" or letter == "Ι":
            num = 9
            word1.append(num)
        elif letter == "κ" or letter == "Κ":
            num = 10
            word1.append(num)
        elif letter == "λ" or letter == "Λ":
            num = 11
            word1.append(num)
        elif letter == "μ" or letter == "Μ":
            num = 12
            word1.append(num)
        elif letter == "ν" or letter == "Ν":
            num = 13
            word1.append(num)
        elif letter == "ξ" or letter == "Ξ":
            num = 14
            word1.append(num)
        elif letter == "ο" or letter == "Ο":
            num = 15
            word1.append(num)
        elif letter == "π" or letter == "Π":
            num = 16
            word1.append(num)
        elif letter == "ρ" or letter == "Ρ":
            num = 17
            word1.append(num)
        elif letter == "σ" or letter == "Σ":
            num = 18
            word1.append(num)
        elif letter == "τ" or letter == "Τ":
            num = 19
            word1.append(num)
        elif letter == "υ" or letter == "Υ":
            num = 20
            word1.append(num)
        elif letter == "φ" or letter == "Φ":
            num = 21
            word1.append(num)
        elif letter == "χ" or letter == "Χ":
            num = 22
            word1.append(num)
        elif letter == "ψ" or letter == "Ψ":
            num = 23
            word1.append(num)
        elif letter == "ω" or letter == "Ω":
            num = 24
            word1.append(num)
        elif letter == "ς":
            num = 25
            word1.append(num)
    print(word, word1)
