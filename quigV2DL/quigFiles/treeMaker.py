import random
num = int(input())
trees = ["tree1","tree2","tree3"]
string = ""
for i in range(0,num):
    for i in range(0,num):
        string = string+"["+str(random.choice(trees))+",("+str(random.randint(200,1000))+","+str(random.randint(0,200))+")],"
    string = string[:-1]
print(string)

