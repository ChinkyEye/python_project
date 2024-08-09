import pickle

f = open("writedata.py","rb")
l = pickle.load(f)
print(l)