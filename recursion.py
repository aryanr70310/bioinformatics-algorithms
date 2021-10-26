import time
import sys
f=['------------','------------']#global variable
g=-48#global variable
def count(a,b,c):
    if a==b and a=='A':
        c+=3
    elif a==b and a=='C':
        c+=2
    elif a==b and a=='G':
        c+=1
    elif a==b and a=='T':
        c+=2
    elif a=='-'or b=='-':
        c-=4
    else:
        c-=3
    return c
def alignment(a,b,c,d,e,l,k):#recursive function
    global f
    global g
    if a==""and b=="":
        l.append([c,d])
        k.append(e)
        if g<e:
            g=e
            f=[c,d]
        e=0
    else:
        if len(a)>=1 and len(b)>=1:
            alignment(a[0:len(a)-1],b[0:len(b)-1],a[len(a)-1]+c,b[len(b)-1]+d,count(a[len(a)-1],b[len(b)-1],e),l,k)#Remove last character of both sequence
        if len(b)>=1:
            alignment(a,b[0:len(b)-1],'-'+c,b[len(b)-1]+d,count('-',b[len(b)-1],e),l,k)#Remove last character of sequence 2
        if len(a)>=1:
            alignment(a[0:len(a)-1],b,a[len(a)-1]+c,'-'+d,count(a[len(a)-1],'-',e),l,k)#Remove last character of sequence 1
    return g,f,len(k)#highest score,best alignments and no. of sequences checked
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

bruh=alignment(seq1,seq2,"","",0,[],[])
best_score=bruh[0]
best_alignment=bruh[1]
num_alignments=bruh[2]

stop = time.time()
time_taken=stop-start

print('Alignments generated: '+str(num_alignments))
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

