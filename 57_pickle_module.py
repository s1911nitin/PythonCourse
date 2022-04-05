import pickle

List = ["Audi","BMW","Volksvogan","Mercedez"]

# byte_stream = pickle.dumps(List)
# print(type(byte_stream))
# print(byte_stream)

# python_list = pickle.loads(byte_stream)
# print(type(python_list))
# print(python_list)

with open("pickle_data","wb") as f:
    pickle.dump(List,f)

with open("pickle_data","rb") as f:
    python_list = pickle.load(f)
print(python_list)

