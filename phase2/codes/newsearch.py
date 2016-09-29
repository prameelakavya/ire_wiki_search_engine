import math
#from stemming.porter2 import stem
import operator
import re
from nltk import PorterStemmer as stem
from collections import Counter, OrderedDict

h=open("./id_title.txt",'r')
N= len(h.readlines())
h.close()
f1=open('../stoplist.txt','r')
stop=[]
stop_words={}
for i in f1:
	if i!='\n':
		stop.append(i)
for i in stop:
	i=i[:-1]
	stop_words[i]=1;

s = open('./sec/secindex.txt')
r=s.readlines()
lines=[]
for line in r:
	line=line.split('|')
	lines.append(line)
first=[]
second=[]
doc_no=[]

for i in lines:
	first.append(i[0])
	second.append(i[2][:-1])
	doc_no.append(i[1])
len_secind=len(first)
#N=len(R)

def get_string(word):
	for i in range(len_secind):
		if first[i]<=word and second[i]>=word:
		#	print 'hey'
			f=open("./sec/"+str(int(doc_no[i])-1)+".txt")
			r=f.readlines()
			for j in r:
				j=j.split(":")
			#	print j[0]
				if j[0] == word:
				#	print j[1]
					return j[1].lstrip()
					break
					

def square_rooted(x):
	return round(math.sqrt(sum([a*a for a in x])),3)
 
def cos_similarity(x,y):
	#print x,y
	numerator = sum(a*b for a,b in zip(x,y))
	denominator = square_rooted(x)*square_rooted(y)
	if denominator !=0:
	    return round(numerator/float(denominator),3)
	else:
	    return 1


def score(flag,postinglist):
	
	n=len(postinglist)
	
	result={}
	idf = N/n
	#print idf
	#print postinglist
	result['idf']=math.log(idf)
	for i in postinglist:
		y=i.split('-')
		y_id=y[0]
		match = re.findall(r"([a-z])([0-9]+)", y[1] , re.I)
		
		if flag=='a':
			count=0
			for j in match:
				if j[0] == 't':
					count+= int(j[1])*20
				elif j[0] == 'i':
					count+= int(j[1])*7
				elif j[0] == 'b':
					count+= int(j[1])*4
				elif j[0] == 'r':
					count+= int(j[1])*10
				elif j[0] == 'e':
					count+= int(j[1])*10
				elif j[0] == 'c':
					count+= int(j[1])*10
		else:
			count=0
			#print match, y_id
			for j in match: 
				if j[0] == flag:
					count+=int(j[1])
					break
		if count !=0:
			result[y_id]=(math.log(idf))+(math.log(count))
	return result



while(1):
    try:
	line=raw_input()
	line=line.split()
	rank={}
	final=[]
	mapping=[]
	flag = "a"
	
	for j in range(len(line)):
		temp=[]
		if(len(line[j])>1 and line[j][1]==':'):
			temp.append(line[j][0])
			temp.append(line[j][2:])
			flag = line[j][0]
		else:
			temp.append(flag)
			temp.append(line[j])
		mapping.append(temp)
	#print mapping
	for j in range(len(mapping)):
		mapping[j][1]=stem().stem_word(mapping[j][1]).lower()
	for j in range(len(mapping)):
		try:
			stop_words[mapping[j][1]]
		except:
			final.append(mapping[j])
	mapping=final
	#print mapping
	qlist=[]
	for i in mapping:
		qlist.append(i[1])
	counts = Counter(qlist)
	#print counts	
	max_freq=counts[list(counts)[0]]
	final_result={}
	query_vector=[]
	for j in range(len(mapping)):
		data=get_string(mapping[j][1])
		
		lists=data.split('|')
		temp=score(mapping[j][0],lists)

		term_idf=temp['idf']
		#print term_idf
		query_vector.append((counts[mapping[j][1]]/max_freq)*(term_idf))
		final_result[mapping[j][1]]=OrderedDict(sorted(temp.items(), key=operator.itemgetter(1), reverse=True))
	#print final_result
	keys_list=[]
	for term in final_result:
		count=0
		for j in final_result[term]:
			if j != 'idf':			
				count+=1
				keys_list.append(j.lstrip())
				
				if count>=10:
					break
	keys_list=list(set(keys_list))	
	#print keys_list	
	doc_vecs={}
	for doc in keys_list:
		dummy=[]
		for i in final_result:
			if doc in final_result[i]:
				dummy.append(final_result[i][doc])
			else:
				dummy.append(0)
		doc_vecs[doc]=dummy
	#print doc_vecs
	
	''' finding cosine similarity'''
	final_dic={}
	y=query_vector
	for i in doc_vecs:
		x=doc_vecs[i]
		final_dic[i]=cos_similarity(x,y)

	'''answer'''
	answer=OrderedDict(sorted(final_dic.items(), key=operator.itemgetter(1), reverse=True))
#	print answer
	top=10
	for i in answer:
		if top <=0:
			break
		#print i
		h=open("./id_title.txt",'r')
		l=h.readlines()
		for j in l:
			line=j.split(' ')
		#	print line
			if line[len(line)-1][:-1]==i:
				print j[:-1]
				break
    except IOError:
    	print "Entered query not found. Please try another query"
    except AttributeError:
        print "Entered query not found. Please try another query"
    except IndexError:
    	print "Entered query not found. Please try another query"
      
