import numpy as np
import sys
def NJ(filnam):
    filines=[]
    with open(filnam) as fil:
        filines=list(fil)
    for i in range(len(filines)):
        filines[i]=filines[i].strip()
    return filines
def rowsum(m,l,rs):#calculates rowsums
    for i in range(l):
        rs.append(0)
        for j in range(l):
            rs[i]+=m[i][j]
    print("Rowsums:","\n",rs,"\n")
    return rs
def qscore(m,l,rs,qs,minqs,x,y):#calculates qscores
    for i in range(l):
        for j in range(l):
            if m[i][j]==0:
                qs[i][j]=0
            else:
                qs[i][j]=((l-1)*m[i,j])-rs[i]-rs[j]
            if minqs>qs[i][j]:
                minqs=qs[i][j]
                x=i
                y=j
    print("Qscores:","\n",qs)
    return qs,minqs,x,y
def clustarr(m,l,x,y,ca):#finds clustered array
    b=False
    for i in range(l):
        for j in range(l):
            if i==x:
                if m[i][j]==0.0 or m[y][j]==0.0:
                    if b==False:
                        ca.append(0.0)
                        b=True
                else:
                    ca.append((m[i][j]+m[y][j]-m[x,y])/2)
    return ca
def newmat(m,l,x,y,ca):#builds new matrix
    t=0
    if x>y:
        t=x
        x=y
        y=t
    m=np.delete(m,y,0)
    m=np.delete(m,y,1)
    m=np.insert(m,x,ca,0)
    m=np.delete(m,x+1,0)
    m=np.insert(m,x,ca,1)
    m=np.delete(m,x+1,1)
    return m
filines=NJ("matrix2.txt")#Change test file here
co=0
m=[[]]
temp=''
b=True
l=len(filines)-1
for i in range(l-1):
    m.append([])
for i in range(1,len(filines)):#gets original matrix
    j=2
    b=True
    while b==True:
        if filines[i][j]==" ":
            m[co].append(float(temp))
            temp=''
        else:
            temp+=filines[i][j]
        if j==len(filines[i])-1:
            m[co].append(float(temp))
            temp=''
            b=False
        j+=1
    co+=1
m=np.array(m)
while l>1:
    print("Matrix:","\n",m,"\n")
    bruh=qscore(m,l,rowsum(m,l,[]),np.zeros((l,l)),0,0,0)
    m=newmat(m,l,bruh[2],bruh[3],clustarr(m,l,bruh[2],bruh[3],[]))
    print("------------------------------------------------------------------------------------------------------------")
    l-=1