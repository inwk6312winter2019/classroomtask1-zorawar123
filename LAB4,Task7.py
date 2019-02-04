import string
def new_pattern(word):
    punc = string.punctuation
    string1 = " " # sting variable
    for p in punc:
        string1 = word.strip()
        string1 = word.replace(p,'')
    return(string1)
def sed(f1,f2):
     try:
        father = open(f1,"r")
        child = open(f2,"w")
        for i in father:
            new = removepattern(i)
            child.write(i)
        print("Write operations performed")
     except:
        print("Error")
f1 = input("Enter father file:")
f2 = input("Enter child file:")
sed(x,y)
