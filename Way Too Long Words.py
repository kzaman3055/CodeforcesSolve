n = int(input())
while(n>0):
    n-=1
    word = str(input())
    L = ""
    if(len(word)<=10):
        print (word)
    else:
        L+=word[0]
        L+=str(len(word)-2)
        L+=word[len(word)-1]
        print (L)