for i in range(128):
    if i%10 == 0:
        print(f"\n{i}-{i+10}: ", end="")
    print(chr(i), end="")
print()
for i in range(9, 31):
    print(f"{i}: {chr(i)}", end="")
    #print(str(i) +": " + chr(i))