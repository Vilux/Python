#Author: Mathias Schneider
#Student no. 301190020
#Dec. 03, 2017

def read_string_list_from_file(the_file):
    '''
    GENERIC READING OF TEXT FILE
    USE AS TEMPLATE, INCORPORATE IN YOUR FILE
    GENERATES A LIST OF STRINGS, ONE STRING PER ELEMENT
    AUTHOR: Diana Cukierman

    Assumptions:
    1) the_file is in the same directory (folder) as this program 
    2) the_file contains one student per "line"  
    3) lines are separated by "\n", that is, after each "line" (student)
       in the file  there is a return ("\n") . Also there is (one single)
       return ("\n") after the last line  in the_file
    4) Thhis function returns a list of strings
    '''
    
    fileRef = open(the_file,"r")      # opening file to be read
    localList=[]                      # new list being constructed
    for line in fileRef:
        string = line[0:len(line)-1]  # -1: eliminates trailing '\n'
                                      # of each line 
                                    
        localList.append(string)      # appends a new element
                                      # of type string to the list
        
    fileRef.close()  
        
    #........
    print ("\n JUST TO TRACE, the local list of strings is:\n")
    for element in localList:
        print (element)  # element is a string for one student
    #........
        
    return localList

    
    
def write_result_to_file(lres,the_file):
    '''
    Creates a text output file from a list of strings
    AUTHOR: Diana Cukierman
    
    Assumptions:
    1) lres is a list of strings, where each string
       will be one line in the output file
    2) the_file will contain the name fo the output file.
       for this porgram it shoudl be a name with .csv extension
    3) it is assumed that each string in lres already includes
       the character "\n" at the end
    4) the resulting file will be in the same directory (folder) as this program 
    5) the resulting file will  contain one student data per line 
    '''
    
    fileRef = open(the_file,"w") # opening file to be written
    for line in lres:
        fileRef.write(line)
                                    
    fileRef.close()
    return

import re

alphanum=["A","B","C","D","E"]  #used to convert the answer key to letters
           
key=read_string_list_from_file("IN_key+pts.txt")
points=read_string_list_from_file("IN_data_studs.txt")

for element in range(len(key)):  #answers and weights are
    answers=key[0]               #global variables representing the 
    weights=key[1]               #answer key and how many points each problem is worth


stud_responses=points[0:]       #This is a list with all students and answers
stud_responses_b=stud_responses #in case list is modified

def answerKey(n):
    ak=""                       #this function will give the answer key
    for i in n:           #in letter form
        ak+=(alphanum[int(i)-1])+" "    #(use answers)
    return ak

def usableWeights(k):    #this function converts the weights of each question
    n=[]                #into a list
    buffer=0
    dec=False
    for i in k:
        if i.isdigit() and dec==False:
            buffer=float(i)
        if i.isdigit() and dec==True:
            buffer+=(float(i)/10)
            dec=False
        if i==("."):
            dec=True
        if i==(" "):
            n.append(buffer)
            buffer=0
    n.append(buffer)
    return n
list_of_weights=usableWeights(weights) #so I can index the weight values

def maxScore(k): #this function will give the maximum score possible
    n=sum(k(weights))
    return n
max_score_flt=maxScore(usableWeights) #for indexing purposes

def numbr_of_questions(k):
    n=(len(k))
    return n

def numbr_of_studs(k):
    n=len(k)
    return n
numbr_studs=numbr_of_studs(points)

def pure_responses(): #this will give a list containing only student's responses
    n=[]            #(without names)
    a=stud_responses_b
    for i in range(len(a)):
        n.append(stud_responses_b[i].split()[1])
    return n
pure=pure_responses()

def pure_names():
    n=[]
    a=stud_responses_b
    for i in range(len(a)):
        n.append(stud_responses_b[i].split()[0])
    return n
pure_name=pure_names()


def all_students():  #process data for all students
    n=[]
    j=0.0
    k=0
    m=0
    q=""
    for i in stud_responses_b:        
        q+=(stud_responses_b[k].split()[0])
        while m<=numbr_of_questions(answers)-1:
            if ((stud_responses_b[k].split()[1])[m])==answers[m]:
                j+=list_of_weights[m]
            m+=1
        q+=","+str(j)+","+str((j/max_score_flt)*100)+"\n"
        m=0
        j=0
        k+=1
    n.append(q)
    return n
all_studs=all_students()

def sel_students(t): #t = name
    n=[]
    j=0.0           #Process data for selected students
    m=0
    q=""
    q+=t
    k=pure_name.index(t)
    while m<=numbr_of_questions(answers)-1:
        if ((stud_responses[k].split()[1])[m])==answers[m]:
            j+=list_of_weights[m]
        m+=1
    q+=","+str(j)+","+str((j/max_score_flt)*100)+"\n"
    n.append(q)
    return n

def max_pts(n):  #n = all_studs or listc
    maximum=0.0        
    lst=''.join(n).split(",")
    for i in range(len(lst)-1):
        if(any(c.isalpha() for c in lst[i])):
           maximum=maximum
        elif float(lst[i])>maximum:
           maximum=float(lst[i])
        else:
           maximum=maximum
    return maximum

def average(n):  #n = all_studs or listc
    lsta=''.join(n).split(",")
    ch=0
    while ch<(len(lsta)-1):
        if(any(c.isalpha() for c in lsta[ch])):
            lsta.remove(lsta[ch])
        ch+=1
    lsta.remove(lsta[ch])
    lsta=[float(i) for i in lsta]
    avg=(sum(lsta))/(len(lsta))
    return avg

def frequency_all(n):  #n = all_studs 
    ans=0
    lst=''.join(n).split(",")   #how many times each q. was answered correctly for all students
    stu=0
    tot=0
    newls=[]
    while ans<=(numbr_of_questions(answers))-1:
        while stu<=(len(lst)/2)-1:
            if (stud_responses[stu].split()[1])[ans]==answers[ans]:
                tot+=1
            stu+=1
        newls.append(tot)
        tot=0
        stu=0
        ans+=1
    return newls

def frequency_sel(n): #n = listc
    ans=0
    lst=''.join(n).split(",")   #how many times each question was answered correctly for selected students
    tot=0
    newls=[]
    finder=0
    while ans<=(numbr_of_questions(answers))-1:
        stu=pure_name.index(listb[finder].split(",",1)[0])
        while finder<(len(lst)//2):
            if (stud_responses[stu].split()[1])[ans]==answers[ans]:
                tot+=1
            finder+=1
            if finder<(len(lst)//2):
                stu=pure_name.index(listb[finder].split(",",1)[0])
        newls.append(tot)
        finder=0
        tot=0
        ans+=1
    return newls
    

def most_dif_all(n): #n = all_studs 
    minim=frequency_all(n)[0]
    elis=[]
    for i in frequency_all(n):
        if i<minim:
            minim=i
    for i in range(len(frequency_all(n))):
        if frequency_all(n)[i]==minim:
            elis.append(int(i)+1)
    return elis

def most_dif_sel(n): #n = listc
    minim=frequency_sel(n)[0]
    elis=[]
    for i in frequency_sel(n):
        if i<minim:
            minim=i
    for i in range(len(frequency_sel(n))):
        if frequency_sel(n)[i]==minim:
            elis.append(int(i)+1)
    return elis
    

def distr_pts(n):
    pure_perc=[]
    lst=''.join(n).split(",")
    del lst[0]
    ch=0
    while ch<(len(lst)-1):
        if not(any(c.isalpha() for c in lst[ch])):
            lst.remove(lst[ch])
        ch+=1
    for i in lst:
        pure_perc.append(re.sub(r'[^\d.]+','',i))
    distr=[]
    studs=0
    k=0
    m=0
    while k<10:
        for i in pure_perc:
            if k==0:
                if 0<=float(i)<=10:
                    studs+=1
            else:
                if 0+m<float(i)<=10+m:
                    studs+=1
        distr.append(studs)
        studs=0
        k+=1
        m+=10
    return distr

def ques_dist(n,n2):    #distance between 2 questions
    n=int(n)
    n2=int(n2)
    k=0
    dist_sum=0
    while k<numbr_studs:
        val1=(stud_responses[k].split()[1][n-1])==answers[n-1]
        val2=(stud_responses[k].split()[1][n2-1])==answers[n2-1]
        if val1==val2:
            dist_val=0
        else:
            dist_val=1
        dist_sum+=dist_val
        print("TRACE: dist for stud",stud_responses[k].split()[0],"is",dist_val)
        k+=1
    print("\nthe distance between questions",n,"and",n2,"is",dist_sum)
    return 
    

def studs_proc(n):
    print("Number of students processed",int((len(''.join(n).split(","))-1)/2))
    return

def welcome():
    print("  Welcome to the CMPT 120 Scantron Processing System!\n  ===================================================")
    return

def choose():
    print("You must choose one of two options:")
    return
       
q1="all"
q2="sel"

print()
welcome()
print("\nThis system will process scantron files in the default folder\nMake sure that the data files do not have extra spaces!")
print()
print("The data file in this folder has",numbr_of_studs(stud_responses),"students")
print("There are",numbr_of_questions(answers),"questions")
print("The answer key is:")
print(answerKey(answers))
print()
print("The points are:")
print(list_of_weights)
print("The maximum points possible are:",max_score_flt)
print()
choose() 
print("Type ALL (not case sensitive) to process the whole class")
print("Type SEL (not case sensitive) to process selected students")
print("     (up to half of the whole class)")
print()

choice=str(input("Type ALL or SEL ==> "))
while choice.lower()!=q1 and choice.lower()!=q2:
    choice=str(input("Please retype, ALL or SEL ==> "))
if choice.lower()==q1:
    write_result_to_file(all_studs,"OUT_results.csv")
    print("\nAll students have been processed!\n")
    print("Here is the output that will be saved in the folder!\n")
    print(''.join(all_studs))
    print()
if choice.lower()==q2:
    print("\nYou chose to process selected students\nYou will be asked to provide the name of the student")
    print()
    count=1
    lista=[]
    cond=False
    half=int(numbr_studs/2)
    name=str(input("Type a name or END to finish ==> "))
    if name=="END":
        cond=True
        count=half
    while not(name in pure_name) and cond==False:
        print("This name is not in the data, type again")
        name=str(input("Type a name or END to finish ==> "))
        if name=="END":
            cond=True
            count=half
    while count<(half) and name in pure_name and cond==False:
        sel_students(name)
        sel_studs=sel_students(name)
        print("Student",name,"got",sel_studs[0].split(",")[1],"points\n")
        name=str(input("Another name or END to finish ==> "))
        count+=1
        lista.append(sel_studs)
        if name=="END":
            cond=True
            count=half
        while not(name in pure_name) and cond==False:
                print("This name is not in the data, type again")
                name=str(input("Type a name or END to finish ==> "))
                if name=="END":
                    cond=True
                    count=half
        if count>=(half) and name in pure_name and cond==False:
            sel_students(name)
            sel_studs=sel_students(name)
            lista.append(sel_studs)
    if count>(half-1) or cond==True:
        listb=[''.join(x) for x in lista]
        listc=[''.join(listb)]
        write_result_to_file(listc,"OUT_results.csv")
        print("All your selected students have been processed!")
        print()
        print("Here is the output that will be saved in the folder!\n")
        print(''.join(listc))


print("HERE ARE THE STATS!")
print("===================")
if choice.lower()==q1:
    print("\nMaximum points: ",max_pts(all_studs))
    print("Average points: ",average(all_studs))
    print("Number of students processed",numbr_studs)
    print("Number of times each question was answered correctly\n",frequency_all(all_studs))
    print("Most difficult questions",most_dif_all(all_studs))
    print("Distribution points",distr_pts(all_studs))
    print("Considering ranges: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]")
if choice.lower()==q2:
    if listc[0]=='':
        print("No students were processed!")
    else:
        print("\nMaximum points: ",max_pts(listc))
        print("Average points: ",average(listc))
        studs_proc(listc)
        print("Number of times each question was answered correctly\n",frequency_sel(listc))
        print("Most difficult questions",most_dif_sel(listc))
        print("Distribution points",distr_pts(listc))
        print("(Considering ranges: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])")
print()
distance=str(input("Would you like to calculate the 'distance' between questions? (Y/N): "))
if distance.lower()=="y":
    print("Special analysis 2 questions\n")
    print("This will provide a 'distance' between two questions\n by accumulating the distance within each student, for all students.")
    print("You can check several pairs of questions. 0 - END")
    end=False
    ques_1=(input("provide q1, starting from 1, or 0 to end: "))
    while end==False:
        while ques_1.isalpha() and end==False:
            print("What you typed is not an integer, please retype")
            ques_1=(input("prove q1, starting from 1, or 0 to end: "))
        while int(ques_1)>numbr_of_questions(answers) or int(ques_1)<0 and end==False:
            print("The value is not within the required range, retype")
            ques_1=(input("prove q1, starting from 1, or 0 to end: "))
        if int(ques_1)==0:
            print("All stats are done! Bye!")
            end=True
        if end==False:
            ques_2=(input("provide q2, starting from 1: "))
            while ques_2.isalpha() and end==False:
                print("What you typed is not an integer, please retype")
                ques_2=(input("prove q2, starting from 1: "))
            while int(ques_2)>numbr_of_questions(answers) or int(ques_2)<=0 and end==False:
                print("The value is not within the required range, retype")
                ques_2=(input("provide q2, starting from 1: "))
            ques_dist(ques_1,ques_2)
            ques_1=input("another q1?, starting from 1, or 0 to end: ")
else:
    print("All stats are done! Bye!")

             
             







                    
        
        
    
    
           

       
       
       
    

    

               
               
    
    
        

        


       

    
    

    


    


            

    




