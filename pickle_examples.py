import pickle


data = {
        'a': [1, 2.0, 3, 4+6j],
        'b': ("character string", "string"),
        'c': {None, True, False}
 }

# Serialization (saving) any object to file
with open('data.pickle', 'wb') as f:
     pickle.dump(data, f)
# OR
pickle.dump(data, open("data.pickle", "wb"))

# Loading object from file
with open('data.pickle', 'rb') as f:
    data_new = pickle.load(f)
# OR
data_new = pickle.load(open("data.pickle", "rb"))
