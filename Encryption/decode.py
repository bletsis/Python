    # load additional module
import pickle
# open a data file (code) to rb (read binary)
with open('code', 'rb') as f:
    # read the data as binary data stream
    list1 = pickle.load(f)

text1 = ""
for num in list1:
    text1 += chr(num)
print("\n" + text1)
