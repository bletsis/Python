# load additional module pickle
import pickle
list1 = []
text1 = ""
text = input("\nType a text to encode: ")
for letter in text:
    list1.append(ord(letter))
# open a data file (code) to wb (write binary)
with open('code', 'wb') as f:
    # with dump method store the data as binary data stream
    pickle.dump(list1, f)
