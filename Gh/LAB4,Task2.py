
import string
 
def small_latters(): 
    dic = dict()
    list1 =[]
    count = 0
    book = 'file.txt'
    with open(book, 'r') as fd:
        words = fd.read().split()
        for i in words:
            words1 = i.strip(string.whitespace + string.punctuation)
            word = words1.lower()
            list1.append(word)
            count += 1
        for j in list1:
            dic[j] =dic.get(j,0) + 1
            val = dic[j]
            dic.setdefault(j,val)
        print(dic)
        for j in dic:
           if dic[j] ==13:
               print(j)
        print(count)
small_latters()


