
phrase = "Pygame includes a higher level sprite module to help organize games. \
The sprite module includes several classes that help manage details found in almost all games types. \
The Sprite classes are a bit more advanced than the regular pygame modules, \
and need more understanding to be properly used."

l = list(phrase)
d = {}
for char in l:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1
print()
print(d)
maximum = (max(set(d.values())))
print()
for key, value in d.items():
    if value == maximum:
        if key == " ":
            print("The most used character is blank: ", value)
        else:
            print(key, value)
