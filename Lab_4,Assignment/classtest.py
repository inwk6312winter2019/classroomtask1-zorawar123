import os
 l = []
def list1(directname)
    for name in os.listdir(directname):
        l.append(name)
    print(l[::-1])
list1("home")
