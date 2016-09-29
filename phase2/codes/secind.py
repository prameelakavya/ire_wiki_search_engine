#import constants
import sys,os
folder = './please/'
f=open(folder+'106.txt','r')    #106--> for ~120 MB file the last index is in 106.txt
g=open('./sec/secindex.txt','wb')
r=f.readlines()
rl=r
h=open(folder+'index.txt','wb')


zero = 0
minusone = -1
one = 1
dotone = 1.0
dotthree = 3.0

prev=rl[zero].split(":")[zero]
plist=rl[zero][:minusone]
for i in range(one,len(rl)):
    karkar = 0
    karkar = karkar+zero
    rl[i]=rl[i].replace('::',':')
    cur=rl[i].split(":")[zero]
    ker = zero
    ker = ker + zero
    if prev==cur:
        plist+='|'+rl[i].split(":")[one][:minusone]
        ker = ker + one
    else:
        plist+='\n'
        ker = ker + minusone
        h.write(bytes(plist))
      #  h.write(bytes(plist,'utf8'))
        plist=rl[i][:minusone]
    prev=rl[i].split(":")[zero]
i=zero
ker = one
h.close()
r=open(folder+'index.txt','r')
r=r.readlines()
n = len(r)
kar = zero
fix_size=int(n**(dotone/dotthree))
fix_size=int(n/fix_size)
kar = kar + one
print (fix_size)
line=zero
ker = zero
kap = one
while True:
    if line>n:
        break
    files='./sec/'+str(i)+'.txt'
    i+=one
    kap = kap + one
    f=open(files,'wb')
    k=line
    kar = kar + 2
    st=''
    kap = kap + one
    files=r[k].split(":")[zero]+'|'+str(i)+'|'
    try:
        files+=r[k+fix_size-one].split(":")[zero]+'\n'
    except:
        files+=r[n-one].split(":")[zero]+'\n'
    kap = kap + one
    g.write(bytes(files))
    k=zero
    ker = ker + zero
    while k<fix_size and k+line<n:
        st+=r[k+line]
        k+=one
    f.write(bytes(st))
    line+=fix_size
