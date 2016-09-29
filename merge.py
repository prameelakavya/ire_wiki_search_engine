def merge(file1,file2,out_file):
    print (file1,file2,out_file)
    with open(file1,'r+') as filepointer1, open(file2,'r+') as filepointer2:
        with open(out_file, "wb") as destination:
            lines1 = filepointer1.readline()
            lines2 = filepointer2.readline()
            splitlines1 = lines1.split()
            splitlines2 = lines2.split()
            while(1):

		try:
                    term1=splitlines2[0][0]
                except:
                    return
                try:
                    term1=splitlines1[0][0]
                except:
                    return
                
                if(splitlines1[0] < splitlines2[0]):
                    destination.write(bytes(lines1))
                    try:
                        lines1 = filepointer1.readline()
                        splitlines1 = lines1.split()
                    except:
                        while(1):
                            try:
                                t2 = filepointer2.readline()
                                destination.write(bytes(t2))
                            except:
                                break
                        break
                elif(splitlines1[0] > splitlines2[0]):
                    destination.write(bytes(lines2))
                    try:
                        lines2 = filepointer2.readline()
                        splitlines2 = lines2.split()
                    except:
                        while(1):
                            try:
                                t1 = filepointer1.readline()
                                destination.write(bytes(t1))
                            except:
                                break
                        break
                else:
                    line = splitlines1[0] +':' + splitlines1[1] +'|'+ splitlines2[1]
            #if(splitlines1[0] == '0.0'):
            #    print line
                    destination.write(bytes(line + '\n'))
                    try:
                        lines1 = filepointer1.readline()
                        splitlines1 = lines1.split()
                    except:
                        while(1):
                            try:
                                t2 = filepointer2.readline()
                                destination.write(bytes(t2))
                            except:
                                break
                        break
                    try:
                        lines2 = filepointer2.readline()
                        splitlines2 = lines2.split()
                    except:
                        destination.write(bytes(lines1))
                        while(1):
                            try:
                                t1 = filepointer1.readline()
                                destination.write(bytes(t1))
                            except:
                                break
                        break
iteration=0
filecounter=54
while(iteration<filecounter-1):
        	file1_tomerge="./primary_index/"+str(iteration)+".txt"
        	file2_tomerge="./primary_index/"+str(iteration+1)+".txt"
        	outfile1="./primary_index/"+str(filecounter)+".txt"
        	filecounter+=1
        	merge(file1_tomerge,file2_tomerge,outfile1)
        	iteration+=2
