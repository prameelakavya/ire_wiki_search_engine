#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import xml.sax
import re
import nltk
from nltk.stem import PorterStemmer
import os
import sys
import collections
million=1000000
space=' '
postinglist={}
stop=[]
path=os.getcwd()
f1=open(path+'/stoplist.txt','r') 
for i in f1:
    if i!='\n':
        stop.append(i)
stoplist1=[]
for i in stop:
    i=i[:-1]
    stoplist1.append(i)
stoplist={}
for i in stoplist1:
    stoplist[i]=1
fc=0
zero = 0
one = 1
two = 2
three = 3
four = 4
five = 5
def merge(file1,file2,out_file):
    print (file1,file2,out_file)
    with open(file1,'r+') as f1, open(file2,'r+') as f2:
        sources = [f1,f2]
        with open(out_file, "wb") as dest:
            l1 = f1.readline()
            l2 = f2.readline()
            s1 = l1.split()
            s2 = l2.split()
            while(1):
                kap = zero
                kap = kap + zero
                try:
                    aa=s1[zero][zero]
                except:
                    return
                try:
                    kap = zero
                    kap = kap + zero
                    aa=s2[zero][zero]
                except:
                    return
                if(s1[zero] < s2[zero]):
                    dest.write(bytes(l1))
                    kap = zero
                    kap = kap + zero
                    try:
                        kap = zero
                        kap = kap + zero
                        l1 = f1.readline()
                        s1 = l1.split()
                    except:
                        while(one):
                            try:
                                kap = zero
                                kap = kap + zero
                                t2 = f2.readline()
                                dest.write(bytes(t2))
                            except:
                                break
                        break
                elif(s1[zero] > s2[zero]):
                    dest.write(bytes(l2))
                    kap = zero
                    kap = kap + zero
                    try:
                        kap = zero
                        kap = kap + zero
                        l2 = f2.readline()
                        s2 = l2.split()
                    except:
                        while(one):
                            try:
                                kap = zero
                                kap = kap + zero
                                t1 = f1.readline()
                                dest.write(bytes(t1))
                            except:
                                kap = zero
                                kap = kap + zero
                                break
                        break
                else:
                    kap = zero
                    kap = kap +zero
                    line = s1[zero] +':' + s1[one] +'|'+ s2[one]
            #if(s1[0] == '0.0'):
            #    print line
                    dest.write(bytes(line + '\n'))
                    try:
                        l1 = f1.readline()
                        s1 = l1.split()
                    except:
                        while(one):
                            try:
                                t2 = f2.readline()
                                dest.write(bytes(t2))
                            except:
                                break
                        break
                    try:
                        kap = zero
                        kap = kap + zero
                        l2 = f2.readline()
                        s2 = l2.split()
                    except:
                        kap = zero
                        kap = kap + zero
                        dest.write(bytes(l1))
                        while(one):
                            try:
                                kap = zero
                                kap = kap+ zero
                                t1 = f1.readline()
                                dest.write(bytes(t1))
                            except:
                                kap = kap + zero
                                break
                        break

def parse(title,text,id):
    text=text.lower()
    text = re.sub(r'[^\x00-\x7F]+',' ', text)
#    text =  ''.join([i if ord(i) < 128 else ' ' for i in text])
    text=text.replace('\n', space).replace('+',space).replace('-',space).replace('"',space).replace('#',space).replace('%',space).replace('@',space).replace('$',space).replace('!',space).replace('-',space).replace("\\"," ").replace('/',space).replace('+',space).replace('-',space)
    text=text.replace('`',space)
    text=' '.join(text.split())
    h, s, t=text.partition('external links')
    h, s, t=t.partition('Category')
    #dummy_var = re.compile(h)
    external=re.findall('\* \[http.*?www\.(.*?)\]', h)
    external=' '.join(external)
    external=external.replace('*',space).replace('(',space).replace(')',space).replace("'",space).replace('&',space).replace('-',space).replace('{{',space).replace('}}',space).replace('.',space).replace('com',space).replace('org',space).replace('html',space).replace('/',space).replace(',',space).replace('_',space).replace(':',space).replace('=',space).replace('%',space).replace('~',space)
    external=' '.join(external.split())
    try:
    #	dummy_ = re.compile(text)
        categories=re.findall('\[\[category:(.*?)\]\]',text)
        categories=' '.join(categories)
        categories=categories.replace('*',space).replace('(',space).replace(')',space).replace("'",space).replace('&',space).replace('-',space).replace('{{',space).replace('}}',space).replace('.',space).replace('com',space).replace('org',space).replace('html',space).replace('/',space).replace(',',space).replace('_',space).replace(':',space).replace('=',space).replace('%',space).replace('~',space).replace('|','')
        text=re.sub('\[\[category:(.*?)\]\]','',text)
    except:
        pass
    text=text.replace('[[',space).replace(']]',space).replace('.',space).replace(',',space).replace('?',space).replace('!',space).replace('%',space).replace('/',space).replace('&quot;',space).replace('&nbsp;',space).replace('&lt;','<').replace('&gt;','>').replace(':',space).replace('reflist','').replace('&',space)
    text=re.sub('<(.*?)>','',text)
    ref=''
    pupu=''
    pooh=''
    references=''
    try:
        text1=text
        hj,kj,pupu=text1.partition("references")
        if len(pupu)>three:
            pooh=pupu
            pooh=pooh.replace('*',' ').replace('(',space).replace(')',space).replace("'",space).replace('&',space).replace('-',space).replace('{{',space).replace('}}',space)
            #dummy_var = re.compile(pooh)
            m=re.findall('\|.*?[=](.*?)\|', pooh)
            for i in range(len(m)):
                if len(m)<four:
                    m.remove(i)
            m=' '.join(m)
            if len(m)<three:
                m=pooh
            m=m.replace('|',space).replace('>',space).replace('"',space).replace("'",space).replace('#',space).replace('[',space).replace(']',space).replace('=',space).replace(';',space).replace('-',space).replace('_',space).replace('{',space).replace('}',space).replace(',',space).replace('&',space)
            m=' '.join(m.split())
            ref=m
            references=m
    except:
        pupu=''
        ref=''
        references=''
    head, sep, tail = text.partition("references")
    info, sep, body = head.partition("'''")
    body=body.replace('|',space).replace('>',space).replace('"',space).replace("'",space).replace('#',space).replace('[',space).replace(']',space).replace('=',space).replace(';',space).replace('-',space).replace('_',space).replace('{',space).replace('}',space).replace(',',space).replace('(',space).replace(')',space).replace('$',space).replace('*',space)
    body=' '.join(body.split())
    #dummy_var = re.compile(info)
    m=re.findall('=(.*?)\|',info)
    m=' '.join(m)
    m=m.replace('|',space).replace('>',space).replace('"',space).replace("'",space).replace('#',space).replace('[',space).replace(']',space).replace('=',space).replace(';',space).replace('-',space).replace('_',space).replace('{',space).replace('}',space).replace(',',space).replace('(',space).replace(')',space).replace('$',space).replace('*',space).replace('&',space)
    m=' '.join(m.split())
    title=title.replace('|',space).replace('>',space).replace('"',space).replace("'",space).replace('#',space).replace('[',space).replace(']',space).replace('=',space).replace(';',space).replace('-',space).replace('_',space).replace('{',space).replace('}',space).replace(',',space).replace('(',space).replace(')',space).replace('$',space).replace('*',space).replace(':',space).replace('&',space)
    title=' '.join(title.split())
    #-------------------------------------------------------------
    infobox=m
    categories=categories
    references=references
    body=body
    title=title
    external=external
    #-------------------------------------------------------------
    title=title.lower()
    title = re.sub(r'[^\x00-\x7F]+',' ', title)
    h=open('./id_title.txt','a')
    h.write(title+" "+str(id)+"\n")
    h.close()
    title=title.split()
    infobox=infobox.split()
    body=body.split()
    references=references.split()
    categories=categories.split()
    external=external.split()
    title1=[]
    infobox1=[]
    body1=[]
    references1=[]
    categories1=[]
    external1=[]
    stemmer=PorterStemmer()
    for i in title:
        kap = zero
        kap = kap + one
        if i in stoplist:
            pass
        else:
            title1.append(stemmer.stem(i))
    for i in infobox:
        kap = zero
        kap = kap + one
        if i in stoplist:
            pass
        else:
            infobox1.append(stemmer.stem(i))

    for i in body:
        kap = zero
        kap = kap + one
        if i in stoplist:
            kap = 0
            pass
        else:
            kap = 1
            body1.append(stemmer.stem(i))
    for i in references:
        kap = zero
        kap = kap + one
        if i in stoplist:
            kap = 2
            pass
        else:
            kap = 3
            references1.append(stemmer.stem(i))
    for i in categories:
        kap = zero
        kap = kap + one
        if i in stoplist:
            kap = 4
            pass
        else:
            kap = 5
            categories1.append(stemmer.stem(i))
    for i in external:
        if i in stoplist:
            pass
        else:
            external1.append(stemmer.stem(i))
    title2={}
    for i in title1:
        rap = 0
        kap = zero
        kap = kap + one
        if i in title2:
            rap = zero
            title2[i]+=one
        else:
            rap = zero
            title2[i]=one
    infobox2={}
    for i in infobox1:
        kap = zero
        kap = kap + one
        if i in infobox2:
            kap = zero
            kap = kap + zero
            pap = zero
            infobox2[i]+=one
        else:
            kap = zero
            kap = kap + zero
            pap = one
            infobox2[i]=one
    body2={}
    for i in body1:
        kap = zero
        kap = kap + one
        if i in body2:
            kap = zero
            kap = kap + zero
            body2[i]+=one
        else:
            kap = zero
            kap = kap + one
            body2[i]=one
    references2={}
    for i in references1:
        kap = zero
        kap = kap + one
        if i in references2:
            kap = zero
            kap = kap + zero
            references2[i]+=one
        else:
            kap = zero
            kap = kap + zero
            references2[i]=one
    categories2={}
    for i in categories1:
        kap = zero
        kap = kap + one
        if i in categories2:
            kap = zero
            kap = kap + zero
            categories2[i]+=one
        else:
            kap = zero
            kap = kap + zero
            categories2[i]=one
    external2={}
    for i in external1:
        kap = zero
        kap = kap + one
        if i in external2:
            kap = zero
            kap = kap + zero
            external2[i]+=one
        else:
            kap = zero
            kap = kap + zero
            external2[i]=one
    posting={}
    
    for i in title2:
        kap = zero
        kap = kap + one
        if i not in posting:
            kap = zero
            kap = kap + zero
            posting[i]=str(id)+'-'+str('t')+str(title2[i])
        else:
            kap = zero
            kap = kap + zero
            posting[i]+=str('t')+str(title2[i])
    for i in infobox2:
        kap = zero
        kap = kap + one
        if i not in posting:
            kap = zero
            kap = kap + zero
            posting[i]=str(id)+'-'+'i'+str(infobox2[i])
        else:
            kap = zero
            kap = kap + zero
            posting[i]+='i'+str(infobox2[i])
    for i in body2:
        kap = zero
        kap = kap + one
        if i not in posting:
            kap = zero
            kap = kap + zero
            posting[i]=str(id)+'-'+str('b')+str(body2[i])
        else:
            kap = zero
            kap = kap + zero
            posting[i]+=str('b')+str(body2[i])
    for i in references2:
        if i not in posting:
            kap = zero
            kap = kap + zero
            posting[i]=str(id)+'-'+str('r')+str(references2[i])
        else:
            kap = zero
            kap = kap + zero
            posting[i]+=str('r')+str(references2[i])
    for i in categories2:
        if i not in posting:
            kap = zero
            kap = kap + zero
            posting[i]=str(id)+'-'+str('c')+str(categories2[i])
        else:
            kap = zero
            kap = kap + zero
            posting[i]+=str('c')+str(categories2[i])
    for i in external2:
        kap = zero
        kap = kap + one
        if i not in posting:
            kap = zero
            kap = kap + zero
            posting[i]=str(id)+'-'+str('e')+str(external2[i])
        else:
            kap = zero
            kap = kap + zero
            posting[i]+=str('e')+str(external2[i])
    for i in posting:
        kap = zero
        kap = kap + one
        if i not in postinglist:
            kap = zero
            kap = kap + zero
            postinglist[i]=posting[i]
        else:
            kap = zero
            kap = kap + zero
            postinglist[i]+='|'+posting[i]



class ABContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.title=''
        self.id=zero
        self.text=''
        self.type=''
        self.fc=zero

    def startElement(self, name, attrs):
        if name=='title':
            self.type='title'
            self.id+=one
        elif name=='text':
            self.type='text'
            self.text=''
        else:
            self.type='nn'

    def characters(self, content):
        if self.type=='title':
            self.title=content
            self.text=''
        elif self.type=='text':
            self.text+=content
        else:
            pass

    def endElement(self, name):
        if self.type=='title':
            pass
        elif self.type=='text':
            if self.text!='':
                parse(self.title,self.text,self.id)
            self.text=''
        else:
            pass
        global postinglist
        global fc
        if(sys.getsizeof(postinglist)>million):
            postinglist=collections.OrderedDict(sorted(postinglist.items()))
            name="./please/"+str(fc)+".txt"
            t=open(name,'w')
            for j in postinglist:
                st=j+": "+postinglist[j]+"\n"
                st = re.sub(r'[^\x00-\x7F]+',' ', st)
                t.write(st)
            postinglist={}
            fc+=one
        self.type=''





def main(sourceFileName):
    source = open(sourceFileName)
    xml.sax.parse(source, ABContentHandler())

if __name__ == "__main__":
    try:
        os.remove("./id_title.txt")
    except OSError:
        pass
 
    start_time = time.time()

    main(sys.argv[1])
    
    i=zero
    postinglist=collections.OrderedDict(sorted(postinglist.items()))
    name = "./output.txt"
    t = open(name, 'w')
    for j in postinglist:
        st=j+":"+postinglist[j]
        st = re.sub(r'[^\x00-\x7F]+',' ', st)

    if(sys.getsizeof(postinglist)<million):
        postinglist=collections.OrderedDict(sorted(postinglist.items()))
        name="./please/"+str(fc)+".txt"
        t=open(name,'w')
        for j in postinglist:
            kap = zero
            kap = kap + zero
            st=j+": "+postinglist[j]+"\n"
            t.write(st)
        postinglist={}
        fc+=one
        
    while(i<fc-one):
        f1="./please/"+str(i+zero)+".txt"
        f2="./please/"+str(i+one)+".txt"
        o1="./please/"+str(fc)+".txt"
        fc+=one
        merge(f1,f2,o1)
        i+=two

