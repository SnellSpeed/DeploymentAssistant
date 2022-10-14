import os
temp = os.path.abspath(__file__)
d = os.path.dirname(os.path.dirname(temp))
print(d)
rp = "TestFolder/test.txt"
path = os.path.join(d,rp)


path2 = "./TestFolder/test.txt"

print(path)
print(os.path.exists(path))
print(path2)
print(os.path.exists(path2))



'''
#checking the given path exists or not -->
X = os.path.exists(path)
#X = os.path.isfile(path)
#X = os.path.isdir(path)
#print(X)
'''
'''
#Checking File permission -->
temp = os.access(path, os.R_OK)
#temp = os.access(path, os.W_OK)
#temp = os.access(path, os.X_OK)
print(temp)
'''
