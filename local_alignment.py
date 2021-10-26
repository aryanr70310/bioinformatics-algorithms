#!/usr/bin/python
import time
import sys
import numpy as np
def makemat(x,y):
    return np.array(y*[x*[0]])
def makebac(x,y):
    return np.array(y*[x*['E']])
def bruh(a,b):#scoring
    if a!=b:
        return -3
    elif a=='A':
        return 3
    elif a=='C'or a=='T':
        return 2
    else:
        return 1
def align(a,b,m,bac,high,x,y,c,d,e):
    for i in range(1,len(b)+1):
        for j in range(1,len(a)+1):
            e=bruh(a[j-1],b[i-1])
            if m[i-1][j-1]+e>=m[i][j-1]-4 and m[i-1][j-1]+e>=m[i-1][j]-4 and m[i-1][j-1]+e>0:#diagonal
                m[i][j]=m[i-1][j-1]+e
                bac[i][j]='D'
                if m[i][j]>high:
                    high=m[i][j]
                    x=i
                    y=j
            elif m[i][j-1]>=m[i-1][j] and m[i][j-1]-4>0:#left
                m[i][j]=m[i][j-1]-4
                bac[i][j]='L'
            elif m[i-1][j]-4>0:#up
                m[i][j]=m[i-1][j]-4
                bac[i][j]='U'
    while bac[x-1][y-1]!='E':#backtracking
        if bac[x][y]=='D':
            c+=a[y-1]
            d+=b[x-1]
            x-=1
            y-=1
        if bac[x][y]=='U':
            c+='-'
            d+=b[x-1]
            x-=1
        if bac[x][y]=='L':
            c+=a[y-1]
            d+='-'
            y-=1
    c+=a[y-1]
    d+=b[x-1]
    return high,c[::-1],d[::-1]
def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

bru=align(seq1,seq2,makemat(len(seq1)+1,len(seq2)+1),makebac(len(seq1)+1,len(seq2)+1),0,0,0,'','',0)
best_score=bru[0]
best_alignment=[bru[1],bru[2]]

stop = time.time()
time_taken=stop-start


print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

