n,b=input().split()
n=n.upper()
b=b.upper()
d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17
   ,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,
   'Y':34,'Z':35}
ma=0
for i in n:
    r=d[i]
    if r>ma:
        ma=r
lb=ma+1
N=0
w=0
for i in range(-1,-(len(n)+1),-1):
    N=N+d[n[i]]*lb**w
    w=w+1
for i in d.keys():
    if i==b:
        b1=d[i]
        b2=b1+1
        break
def prime(p):
    cnt=0
    if p>1:
        for i in range(2,p):
            if(p%i)==0:
                break
        else:
            cnt=1
    else:
        cnt=0
    return(cnt)
s=0
flag=1
while(flag):
    if s==0:
        v=b1
    else:
        v=b1
        po=1
        t=s
        while(t>0):
            r=t%10
            v=v+(r*(b2**po))
            t=t//10
            po=po+1
    c=prime(v)
    if(c==1 and v>=N):
        if s==0:
            print(b)
        else:
            print(str(s)+b)
        flag=0
    s=s+1
        

