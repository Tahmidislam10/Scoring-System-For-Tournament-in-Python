print("Welcome to the competition")
print("")
import sys 
T1=0
T2=0
T3=0
T4=0
Person1=0
Person2=0
Person3=0
Person4=0
Person5=0
Person6=0
Person7=0
Person8=0
Person9=0
Person10=0
Person11=0
Person12=0
Person13=0
Person14=0
Person15=0
Person16=0
Person17=0
Person18=0
Person19=0
Person20=0

point1=[]
point2=[]
point3=[]
point4=[]
point5=[]
#place=[]


teams=4

Team=[]
Person=[]

print("Please enter (teams) for Teams and (individual) for Individual")

team_names1=[]
team_names2=[]
team_names3=[]
team_names4=[]
event=[]
event_names1=[]
event_names2=[]
event_names3=[]
event_names4=[]
event_names5=[]
rankings_1=[]
rankings_2=[]
rankings_3=[]
rankings_4=[]
rankings_5=[]
def singlesports():
    waffle=[" 1st place"," 2nd place"," 3rd place"," 4th place"," 5th place"," 6th place"]
    global point1
    global point2
    global point3
    global point4
    global point5
    global Person
    global Person1
    global Person2
    global Person3
    global Person4
    global Person5
    global Person6
    global Person7
    global Person8
    global Person9
    global Person10
    global Person11
    global Person12
    global Person13
    global Person14
    global Person15
    global Person16
    global Person17
    global Person18
    global Person19
    global Person20
    while True:
        for i in range(6):
            try:
            
                point=int(input("Input points for sports event" +waffle[i]))
                if point > 0 and point < 20:
                    print("Score is set to", point)
                    point5.append(point)

                else:
                    print("Enter number between 1 and 20 ")
                    singlesports()
            except ValueError:
                print("Please make sure you enter a number!")
                continue
               

    option=str(input("Input name of individual who came 1st for sports" +waffle[i]))
    if option == Person[0]:
        Person1=Person1+point5[0]

    elif option == Person[1]:
        Person2=Person2+point5[0]

    elif option == Person[2]:
        Person3=Person3+point5[0]
        
    elif option == Person[3]:
        Person4=Person4+point5[0]

    elif option == Person[4]:
        Person5=Person5+point5[0]

    elif option == Person[5]:
        Person6=Person6+point5[0]

    elif option == Person[6]:
        Person7=Person7+point5[0]

    elif option == Person[7]:
        Person8=Person8+point5[0]

    elif option == Person[8]:
        Person3=Person9+point5[0]

    elif option == Person[9]:
        Person10=Person10+point5[0]

    elif option == Person[10]:
        Person11=Person11+point5[0]

    elif option == Person[11]:
        Person12=Person12+point5[0]

    elif option == Person[12]:
        Person13=Person13+point5[0]

    elif option == Person[13]:
        Person14=Person14+point5[0]

    elif option == Person[14]:
        Person15=Person15+point5[0]

    elif option == Person[15]:
        Person16=Person16+point5[0]

    elif option == Person[16]:
        Person17=Person17+point5[0]

    elif option == Person[17]:
        Person18=Person18+point5[0]

    elif option == Person[18]:
        Person19=Person19+point5[0]

    else:
        Person20=Person20+point5[0]

    option=str(input("Input name of individual who came 2nd "))
    if option == Person[0]:
        Person1=Person1+point5[1]

    elif option == Person[1]:
        Person2=Person2+point5[1]

    elif option == Person[2]:
        Person3=Person3+point5[1]
        
    elif option == Person[3]:
        Person4=Person4+point5[1]

    elif option == Person[4]:
        Person5=Person5+point5[1]

    elif option == Person[5]:
        Person6=Person6+point5[1]

    elif option == Person[6]:
        Person7=Person7+point5[1]

    elif option == Person[7]:
        Person8=Person8+point5[1]

    elif option == Person[8]:
        Person3=Person9+point5[1]

    elif option == Person[9]:
        Person10=Person10+point5[1]

    elif option == Person[10]:
        Person11=Person11+point5[1]

    elif option == Person[11]:
        Person12=Person12+point5[1]

    elif option == Person[12]:
        Person13=Person13+point5[1]

    elif option == Person[13]:
        Person14=Person14+point5[1]

    elif option == Person[14]:
        Person15=Person15+point5[1]

    elif option == Person[15]:
        Person16=Person16+point5[1]

    elif option == Person[16]:
        Person17=Person17+point5[1]

    elif option == Person[17]:
        Person18=Person18+point5[1]

    elif option == Person[18]:
        Person19=Person19+point5[1]

    else:
        Person20=Person20+point5[1]

    option=str(input("Input name of individual who came 3rd "))
    if option == Person[0]:
        Person1=Person1+point5[2]

    elif option == Person[1]:
        Person2=Person2+point5[2]

    elif option == Person[2]:
        Person3=Person3+point5[2]
        
    elif option == Person[3]:
        Person4=Person4+point5[2]

    elif option == Person[4]:
        Person5=Person5+point5[2]

    elif option == Person[5]:
        Person6=Person6+point5[2]

    elif option == Person[6]:
        Person7=Person7+point5[2]

    elif option == Person[7]:
        Person8=Person8+point5[2]

    elif option == Person[8]:
        Person3=Person9+point5[2]

    elif option == Person[9]:
        Person10=Person10+point5[2]

    elif option == Person[10]:
        Person11=Person11+point5[2]

    elif option == Person[11]:
        Person12=Person12+point5[2]

    elif option == Person[12]:
        Person13=Person13+point5[2]

    elif option == Person[13]:
        Person14=Person14+point5[2]

    elif option == Person[14]:
        Person15=Person15+point5[2]

    elif option == Person[15]:
        Person16=Person16+point5[2]

    elif option == Person[16]:
        Person17=Person17+point5[2]

    elif option == Person[17]:
        Person18=Person18+point5[2]

    elif option == Person[18]:
        Person19=Person19+point5[2]

    else:
        Person20=Person20+point5[2]
        
    option=str(input("Input name of individual who came 4th "))
    if option == Person[0]:
        Person1=Person1+point5[3]

    elif option == Person[1]:
        Person2=Person2+point5[3]

    elif option == Person[2]:
        Person3=Person3+point5[3]
        
    elif option == Person[3]:
        Person4=Person4+point5[3]

    elif option == Person[4]:
        Person5=Person5+point5[3]

    elif option == Person[5]:
        Person6=Person6+point5[3]

    elif option == Person[6]:
        Person7=Person7+point5[3]

    elif option == Person[7]:
        Person8=Person8+point5[3]

    elif option == Person[8]:
        Person3=Person9+point5[3]

    elif option == Person[9]:
        Person10=Person10+point5[3]

    elif option == Person[10]:
        Person11=Person11+point5[3]

    elif option == Person[11]:
        Person12=Person12+point5[3]

    elif option == Person[12]:
        Person13=Person13+point5[3]

    elif option == Person[13]:
        Person14=Person14+point5[3]

    elif option == Person[14]:
        Person15=Person15+point5[3]

    elif option == Person[15]:
        Person16=Person16+point5[3]

    elif option == Person[16]:
        Person17=Person17+point5[3]

    elif option == Person[17]:
        Person18=Person18+point5[3]

    elif option == Person[18]:
        Person19=Person19+point5[3]

    else:
        Person20=Person20+point5[3]
        

    option=str(input("Input name of individual who came 5th "))
    if option == Person[0]:
        Person1=Person1+point5[4]

    elif option == Person[1]:
        Person2=Person2+point5[4]

    elif option == Person[2]:
        Person3=Person3+point5[4]
        
    elif option == Person[3]:
        Person4=Person4+point5[4]

    elif option == Person[4]:
        Person5=Person5+point5[4]

    elif option == Person[5]:
        Person6=Person6+point5[4]

    elif option == Person[6]:
        Person7=Person7+point5[4]

    elif option == Person[7]:
        Person8=Person8+point5[4]

    elif option == Person[8]:
        Person3=Person9+point5[4]

    elif option == Person[9]:
        Person10=Person10+point5[4]

    elif option == Person[10]:
        Person11=Person11+point5[4]

    elif option == Person[11]:
        Person12=Person12+point5[4]

    elif option == Person[12]:
        Person13=Person13+point5[4]

    elif option == Person[13]:
        Person14=Person14+point5[4]

    elif option == Person[14]:
        Person15=Person15+point5[4]

    elif option == Person[15]:
        Person16=Person16+point5[4]

    elif option == Person[16]:
        Person17=Person17+point5[4]

    elif option == Person[17]:
        Person18=Person18+point5[4]

    elif option == Person[18]:
        Person19=Person19+point5[4]

    else:
        Person20=Person20+point5[4]


    option=str(input("Input name of individual who came 6th "))
    if option == Person[0]:
        Person1=Person1+point5[5]

    elif option == Person[1]:
        Person2=Person2+point5[5]

    elif option == Person[2]:
        Person3=Person3+point5[5]
        
    elif option == Person[3]:
        Person4=Person4+point5[5]

    elif option == Person[4]:
        Person5=Person5+point5[5]

    elif option == Person[5]:
        Person6=Person6+point5[5]

    elif option == Person[6]:
        Person7=Person7+point5[5]

    elif option == Person[7]:
        Person8=Person8+point5[5]

    elif option == Person[8]:
        Person3=Person9+point5[5]

    elif option == Person[9]:
        Person10=Person10+point5[5]

    elif option == Person[10]:
        Person11=Person11+point5[5]

    elif option == Person[11]:
        Person12=Person12+point5[5]

    elif option == Person[12]:
        Person13=Person13+point5[5]

    elif option == Person[13]:
        Person14=Person14+point5[5]

    elif option == Person[14]:
        Person15=Person15+point5[5]

    elif option == Person[15]:
        Person16=Person16+point5[5]

    elif option == Person[16]:
        Person17=Person17+point5[5]

    elif option == Person[17]:
        Person18=Person18+point5[5]

    elif option == Person[18]:
        Person19=Person19+point5[5]

    else:
        Person20=Person20+point5[5]

    print("1st Place for :" ,Person1)
    print("2nd Place for :" ,Person2)
    print("3rd Place for :" ,Person3)
    print("4th Place for :" ,Person4)
    print("5th Place for :" ,Person5)
    print("6th Place for :" ,Person6)
    print("7th Place for :" ,Person7)
    print("8th Place for :" ,Person8)
    print("9th Place for :" ,Person9)
    print("10th Place for :" ,Person10)
    print("11th Place for :" ,Person11)
    print("12th Place for :" ,Person12)
    print("13th Place for :" ,Person13)
    print("14th Place for :" ,Person14)
    print("15th Place for :" ,Person15)
    print("16th Place for :" ,Person16)
    print("17th Place for :" ,Person17)
    print("18th Place for :" ,Person18)
    print("19th Place for :" ,Person19)
    print("20th Place for :" ,Person20)        
    while True:
        option=str(input("enter art, english, science, maths and sports"))
        if option == "art":
            singleart()
            break
        elif option == "english":
            singleenglish()
            break

        elif option == "science":
            singlescience()
            break

        elif option == "maths":
            singlemaths()
            break

        elif option == "sports":
            singlesports()
            break

        else:
            sys.exit()
def singlemaths():
    waffle=[" 1st place"," 2nd place"," 3rd place"," 4th place"," 5th place"," 6th place"]
    global point1
    global point2
    global point3
    global point4
    global point5
    global Person
    global Person1
    global Person2
    global Person3
    global Person4
    global Person5
    global Person6
    global Person7
    global Person8
    global Person9
    global Person10
    global Person11
    global Person12
    global Person13
    global Person14
    global Person15
    global Person16
    global Person17
    global Person18
    global Person19
    global Person20        
    for i in range(6):
        try:
        
            point=int(input("Input points for maths event" +waffle[i]))
            if point > 0 and point < 20:
                print("Score is set to", point)
                point4.append(point)

            else:
                print("Enter a number between 1 and 20")
                singlesports()
        except ValueError:
            print("Please make sure you enter a number!")
            continue

        
    option=str(input("Input name of individual who came 1st for maths"))
    if option == Person[0]:
        Person1=Person1+point4[0]

    elif option == Person[1]:
        Person2=Person2+point4[0]

    elif option == Person[2]:
        Person3=Person3+point4[0]
        
    elif option == Person[3]:
        Person4=Person4+point4[0]

    elif option == Person[4]:
        Person5=Person5+point4[0]

    elif option == Person[5]:
        Person6=Person6+point4[0]

    elif option == Person[6]:
        Person7=Person7+point4[0]

    elif option == Person[7]:
        Person8=Person8+point4[0]

    elif option == Person[8]:
        Person3=Person9+point4[0]

    elif option == Person[9]:
        Person10=Person10+point4[0]

    elif option == Person[10]:
        Person11=Person11+point4[0]

    elif option == Person[11]:
        Person12=Person12+point4[0]

    elif option == Person[12]:
        Person13=Person13+point4[0]

    elif option == Person[13]:
        Person14=Person14+point4[0]

    elif option == Person[14]:
        Person15=Person15+point4[0]

    elif option == Person[15]:
        Person16=Person16+point4[0]

    elif option == Person[16]:
        Person17=Person17+point4[0]

    elif option == Person[17]:
        Person18=Person18+point4[0]

    elif option == Person[18]:
        Person19=Person19+point4[0]

    else:
        Person20=Person20+point4[0]

    option=str(input("Input name of individual who came 2nd "))
    if option == Person[0]:
        Person1=Person1+point4[1]

    elif option == Person[1]:
        Person2=Person2+point4[1]

    elif option == Person[2]:
        Person3=Person3+point4[1]
        
    elif option == Person[3]:
        Person4=Person4+point4[1]

    elif option == Person[4]:
        Person5=Person5+point4[1]

    elif option == Person[5]:
        Person6=Person6+point4[1]

    elif option == Person[6]:
        Person7=Person7+point4[1]

    elif option == Person[7]:
        Person8=Person8+point4[1]

    elif option == Person[8]:
        Person3=Person9+point4[1]

    elif option == Person[9]:
        Person10=Person10+point4[1]

    elif option == Person[10]:
        Person11=Person11+point4[1]

    elif option == Person[11]:
        Person12=Person12+point4[1]

    elif option == Person[12]:
        Person13=Person13+point4[1]

    elif option == Person[13]:
        Person14=Person14+point4[1]

    elif option == Person[14]:
        Person15=Person15+point4[1]

    elif option == Person[15]:
        Person16=Person16+point4[1]

    elif option == Person[16]:
        Person17=Person17+point4[1]

    elif option == Person[17]:
        Person18=Person18+point4[1]

    elif option == Person[18]:
        Person19=Person19+point4[1]

    else:
        Person20=Person20+point4[1]

    option=str(input("Input name of individual who came 3rd "))
    if option == Person[0]:
        Person1=Person1+point4[2]

    elif option == Person[1]:
        Person2=Person2+point4[2]

    elif option == Person[2]:
        Person3=Person3+point4[2]
        
    elif option == Person[3]:
        Person4=Person4+point4[2]

    elif option == Person[4]:
        Person5=Person5+point4[2]

    elif option == Person[5]:
        Person6=Person6+point4[2]

    elif option == Person[6]:
        Person7=Person7+point4[2]

    elif option == Person[7]:
        Person8=Person8+point4[2]

    elif option == Person[8]:
        Person3=Person9+point4[2]

    elif option == Person[9]:
        Person10=Person10+point4[2]

    elif option == Person[10]:
        Person11=Person11+point4[2]

    elif option == Person[11]:
        Person12=Person12+point4[2]

    elif option == Person[12]:
        Person13=Person13+point4[2]

    elif option == Person[13]:
        Person14=Person14+point4[2]

    elif option == Person[14]:
        Person15=Person15+point4[2]

    elif option == Person[15]:
        Person16=Person16+point4[2]

    elif option == Person[16]:
        Person17=Person17+point4[2]

    elif option == Person[17]:
        Person18=Person18+point4[2]

    elif option == Person[18]:
        Person19=Person19+point4[2]

    else:
        Person20=Person20+point4[2]
        
    option=str(input("Input name of individual who came 4th "))
    if option == Person[0]:
        Person1=Person1+point4[3]

    elif option == Person[1]:
        Person2=Person2+point4[3]

    elif option == Person[2]:
        Person3=Person3+point4[3]
        
    elif option == Person[3]:
        Person4=Person4+point4[3]

    elif option == Person[4]:
        Person5=Person5+point4[3]

    elif option == Person[5]:
        Person6=Person6+point4[3]

    elif option == Person[6]:
        Person7=Person7+point4[3]

    elif option == Person[7]:
        Person8=Person8+point4[3]

    elif option == Person[8]:
        Person3=Person9+point4[3]

    elif option == Person[9]:
        Person10=Person10+point4[3]

    elif option == Person[10]:
        Person11=Person11+point4[3]

    elif option == Person[11]:
        Person12=Person12+point4[3]

    elif option == Person[12]:
        Person13=Person13+point4[3]

    elif option == Person[13]:
        Person14=Person14+point4[3]

    elif option == Person[14]:
        Person15=Person15+point4[3]

    elif option == Person[15]:
        Person16=Person16+point4[3]

    elif option == Person[16]:
        Person17=Person17+point4[3]

    elif option == Person[17]:
        Person18=Person18+point4[3]

    elif option == Person[18]:
        Person19=Person19+point4[3]

    else:
        Person20=Person20+point4[3]
        

    option=str(input("Input name of individual who came 5th "))
    if option == Person[0]:
        Person1=Person1+point4[4]

    elif option == Person[1]:
        Person2=Person2+point4[4]

    elif option == Person[2]:
        Person3=Person3+point4[4]
        
    elif option == Person[3]:
        Person4=Person4+point4[4]

    elif option == Person[4]:
        Person5=Person5+point4[4]

    elif option == Person[5]:
        Person6=Person6+point4[4]

    elif option == Person[6]:
        Person7=Person7+point4[4]

    elif option == Person[7]:
        Person8=Person8+point4[4]

    elif option == Person[8]:
        Person3=Person9+point4[4]

    elif option == Person[9]:
        Person10=Person10+point4[4]

    elif option == Person[10]:
        Person11=Person11+point4[4]

    elif option == Person[11]:
        Person12=Person12+point4[4]

    elif option == Person[12]:
        Person13=Person13+point4[4]

    elif option == Person[13]:
        Person14=Person14+point4[4]

    elif option == Person[14]:
        Person15=Person15+point4[4]

    elif option == Person[15]:
        Person16=Person16+point4[4]

    elif option == Person[16]:
        Person17=Person17+point4[4]

    elif option == Person[17]:
        Person18=Person18+point4[4]

    elif option == Person[18]:
        Person19=Person19+point4[4]

    else:
        Person20=Person20+point4[4]


    option=str(input("Input name of individual who came 6th "))
    if option == Person[0]:
        Person1=Person1+point4[5]

    elif option == Person[1]:
        Person2=Person2+point4[5]

    elif option == Person[2]:
        Person3=Person3+point4[5]
        
    elif option == Person[3]:
        Person4=Person4+point4[5]

    elif option == Person[4]:
        Person5=Person5+point4[5]

    elif option == Person[5]:
        Person6=Person6+point4[5]

    elif option == Person[6]:
        Person7=Person7+point4[5]

    elif option == Person[7]:
        Person8=Person8+point4[5]

    elif option == Person[8]:
        Person3=Person9+point4[5]

    elif option == Person[9]:
        Person10=Person10+point4[5]

    elif option == Person[10]:
        Person11=Person11+point4[5]

    elif option == Person[11]:
        Person12=Person12+point4[5]

    elif option == Person[12]:
        Person13=Person13+point4[5]

    elif option == Person[13]:
        Person14=Person14+point4[5]

    elif option == Person[14]:
        Person15=Person15+point4[5]

    elif option == Person[15]:
        Person16=Person16+point4[5]

    elif option == Person[16]:
        Person17=Person17+point4[5]

    elif option == Person[17]:
        Person18=Person18+point4[5]

    elif option == Person[18]:
        Person19=Person19+point4[5]

    else:
        Person20=Person20+point4[5]
    print("1st Place for :" ,Person1)
    print("2nd Place for :" ,Person2)
    print("3rd Place for :" ,Person3)
    print("4th Place for :" ,Person4)
    print("5th Place for :" ,Person5)
    print("6th Place for :" ,Person6)
    print("7th Place for :" ,Person7)
    print("8th Place for :" ,Person8)
    print("9th Place for :" ,Person9)
    print("10th Place for :" ,Person10)
    print("11th Place for :" ,Person11)
    print("12th Place for :" ,Person12)
    print("13th Place for :" ,Person13)
    print("14th Place for :" ,Person14)
    print("15th Place for :" ,Person15)
    print("16th Place for :" ,Person16)
    print("17th Place for :" ,Person17)
    print("18th Place for :" ,Person18)
    print("19th Place for :" ,Person19)
    print("20th Place for :" ,Person20)        
def singlescience():
    waffle=[" 1st place"," 2nd place"," 3rd place"," 4th place"," 5th place"," 6th place"]
    global point1
    global point2
    global point3
    global point4
    global point5
    global Person
    global Person1
    global Person2
    global Person3
    global Person4
    global Person5
    global Person6
    global Person7
    global Person8
    global Person9
    global Person10
    global Person11
    global Person12
    global Person13
    global Person14
    global Person15
    global Person16
    global Person17
    global Person18
    global Person19
    global Person20        
    for i in range(6):
        try:
            point=int(input("Input points for science event" +waffle[i]))
            if point > 0 and point < 20:
                print("Score is set to", point)
                point3.append(point)

            else:
                print("Enter a number between 1 and 20")
                singlescience()
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        
        
    option=str(input("Input name of individual who came 1st for science"))
    if option == Person[0]:
        Person1=Person1+point3[0]

    elif option == Person[1]:
        Person2=Person2+point3[0]

    elif option == Person[2]:
        Person3=Person3+point3[0]
        
    elif option == Person[3]:
        Person4=Person4+point3[0]

    elif option == Person[4]:
        Person5=Person5+point3[0]

    elif option == Person[5]:
        Person6=Person6+point3[0]

    elif option == Person[6]:
        Person7=Person7+point3[0]

    elif option == Person[7]:
        Person8=Person8+point3[0]

    elif option == Person[8]:
        Person3=Person9+point3[0]

    elif option == Person[9]:
        Person10=Person10+point3[0]

    elif option == Person[10]:
        Person11=Person11+point3[0]

    elif option == Person[11]:
        Person12=Person12+point3[0]

    elif option == Person[12]:
        Person13=Person13+point3[0]

    elif option == Person[13]:
        Person14=Person14+point3[0]

    elif option == Person[14]:
        Person15=Person15+point3[0]

    elif option == Person[15]:
        Person16=Person16+point3[0]

    elif option == Person[16]:
        Person17=Person17+point3[0]

    elif option == Person[17]:
        Person18=Person18+point3[0]

    elif option == Person[18]:
        Person19=Person19+point3[0]

    else:
        Person20=Person20+point3[0]

    option=str(input("Input name of individual who came 2nd "))
    if option == Person[0]:
        Person1=Person1+point3[1]

    elif option == Person[1]:
        Person2=Person2+point3[1]

    elif option == Person[2]:
        Person3=Person3+point3[1]
        
    elif option == Person[3]:
        Person4=Person4+point3[1]

    elif option == Person[4]:
        Person5=Person5+point3[1]

    elif option == Person[5]:
        Person6=Person6+point3[1]

    elif option == Person[6]:
        Person7=Person7+point3[1]

    elif option == Person[7]:
        Person8=Person8+point3[1]

    elif option == Person[8]:
        Person3=Person9+point3[1]

    elif option == Person[9]:
        Person10=Person10+point3[1]

    elif option == Person[10]:
        Person11=Person11+point3[1]

    elif option == Person[11]:
        Person12=Person12+point3[1]

    elif option == Person[12]:
        Person13=Person13+point3[1]

    elif option == Person[13]:
        Person14=Person14+point3[1]

    elif option == Person[14]:
        Person15=Person15+point3[1]

    elif option == Person[15]:
        Person16=Person16+point3[1]

    elif option == Person[16]:
        Person17=Person17+point3[1]

    elif option == Person[17]:
        Person18=Person18+point3[1]

    elif option == Person[18]:
        Person19=Person19+point3[1]

    else:
        Person20=Person20+point3[1]

    option=str(input("Input name of individual who came 3rd "))
    if option == Person[0]:
        Person1=Person1+point3[2]

    elif option == Person[1]:
        Person2=Person2+point3[2]

    elif option == Person[2]:
        Person3=Person3+point3[2]
        
    elif option == Person[3]:
        Person4=Person4+point3[2]

    elif option == Person[4]:
        Person5=Person5+point3[2]

    elif option == Person[5]:
        Person6=Person6+point3[2]

    elif option == Person[6]:
        Person7=Person7+point3[2]

    elif option == Person[7]:
        Person8=Person8+point3[2]

    elif option == Person[8]:
        Person3=Person9+point3[2]

    elif option == Person[9]:
        Person10=Person10+point3[2]

    elif option == Person[10]:
        Person11=Person11+point3[2]

    elif option == Person[11]:
        Person12=Person12+point3[2]

    elif option == Person[12]:
        Person13=Person13+point3[2]

    elif option == Person[13]:
        Person14=Person14+point3[2]

    elif option == Person[14]:
        Person15=Person15+point3[2]

    elif option == Person[15]:
        Person16=Person16+point3[2]

    elif option == Person[16]:
        Person17=Person17+point3[2]

    elif option == Person[17]:
        Person18=Person18+point3[2]

    elif option == Person[18]:
        Person19=Person19+point3[2]

    else:
        Person20=Person20+point3[2]
        
    option=str(input("Input name of individual who came 4th "))
    if option == Person[0]:
        Person1=Person1+point3[3]

    elif option == Person[1]:
        Person2=Person2+point3[3]

    elif option == Person[2]:
        Person3=Person3+point3[3]
        
    elif option == Person[3]:
        Person4=Person4+point3[3]

    elif option == Person[4]:
        Person5=Person5+point3[3]

    elif option == Person[5]:
        Person6=Person6+point3[3]

    elif option == Person[6]:
        Person7=Person7+point3[3]

    elif option == Person[7]:
        Person8=Person8+point3[3]

    elif option == Person[8]:
        Person3=Person9+point3[3]

    elif option == Person[9]:
        Person10=Person10+point3[3]

    elif option == Person[10]:
        Person11=Person11+point3[3]

    elif option == Person[11]:
        Person12=Person12+point3[3]

    elif option == Person[12]:
        Person13=Person13+point3[3]

    elif option == Person[13]:
        Person14=Person14+point3[3]

    elif option == Person[14]:
        Person15=Person15+point3[3]

    elif option == Person[15]:
        Person16=Person16+point3[3]

    elif option == Person[16]:
        Person17=Person17+point3[3]

    elif option == Person[17]:
        Person18=Person18+point3[3]

    elif option == Person[18]:
        Person19=Person19+point3[3]

    else:
        Person20=Person20+point3[3]
        

    option=str(input("Input name of individual who came 5th "))
    if option == Person[0]:
        Person1=Person1+point3[4]

    elif option == Person[1]:
        Person2=Person2+point3[4]

    elif option == Person[2]:
        Person3=Person3+point3[4]
        
    elif option == Person[3]:
        Person4=Person4+point3[4]

    elif option == Person[4]:
        Person5=Person5+point3[4]

    elif option == Person[5]:
        Person6=Person6+point3[4]

    elif option == Person[6]:
        Person7=Person7+point3[4]

    elif option == Person[7]:
        Person8=Person8+point3[4]

    elif option == Person[8]:
        Person3=Person9+point3[4]

    elif option == Person[9]:
        Person10=Person10+point3[4]

    elif option == Person[10]:
        Person11=Person11+point3[4]

    elif option == Person[11]:
        Person12=Person12+point3[4]

    elif option == Person[12]:
        Person13=Person13+point3[4]

    elif option == Person[13]:
        Person14=Person14+point3[4]

    elif option == Person[14]:
        Person15=Person15+point3[4]

    elif option == Person[15]:
        Person16=Person16+point3[4]

    elif option == Person[16]:
        Person17=Person17+point3[4]

    elif option == Person[17]:
        Person18=Person18+point3[4]

    elif option == Person[18]:
        Person19=Person19+point3[4]

    else:
        Person20=Person20+point3[4]


    option=str(input("Input name of individual who came 6th "))
    if option == Person[0]:
        Person1=Person1+point3[5]

    elif option == Person[1]:
        Person2=Person2+point3[5]

    elif option == Person[2]:
        Person3=Person3+point3[5]
        
    elif option == Person[3]:
        Person4=Person4+point3[5]

    elif option == Person[4]:
        Person5=Person5+point3[5]

    elif option == Person[5]:
        Person6=Person6+point3[5]

    elif option == Person[6]:
        Person7=Person7+point3[5]

    elif option == Person[7]:
        Person8=Person8+point3[5]

    elif option == Person[8]:
        Person3=Person9+point3[5]

    elif option == Person[9]:
        Person10=Person10+point3[5]

    elif option == Person[10]:
        Person11=Person11+point3[5]

    elif option == Person[11]:
        Person12=Person12+point3[5]

    elif option == Person[12]:
        Person13=Person13+point3[5]

    elif option == Person[13]:
        Person14=Person14+point3[5]

    elif option == Person[14]:
        Person15=Person15+point3[5]

    elif option == Person[15]:
        Person16=Person16+point3[5]

    elif option == Person[16]:
        Person17=Person17+point3[5]

    elif option == Person[17]:
        Person18=Person18+point3[5]

    elif option == Person[18]:
        Person19=Person19+point3[5]

    else:
        Person20=Person20+point3[5]        

    print("1st Place for :" ,Person1)
    print("2nd Place for :" ,Person2)
    print("3rd Place for :" ,Person3)
    print("4th Place for :" ,Person4)
    print("5th Place for :" ,Person5)
    print("6th Place for :" ,Person6)
    print("7th Place for :" ,Person7)
    print("8th Place for :" ,Person8)
    print("9th Place for :" ,Person9)
    print("10th Place for :" ,Person10)
    print("11th Place for :" ,Person11)
    print("12th Place for :" ,Person12)
    print("13th Place for :" ,Person13)
    print("14th Place for :" ,Person14)
    print("15th Place for :" ,Person15)
    print("16th Place for :" ,Person16)
    print("17th Place for :" ,Person17)
    print("18th Place for :" ,Person18)
    print("19th Place for :" ,Person19)
    print("20th Place for :" ,Person20)
    while True:
        option=str(input("enter art, english, science, maths and sports"))
        if option == "art":
            singleart()
            break
        elif option == "english":
            singleenglish()
            break

        elif option == "science":
            singlescience()
            break

        elif option == "maths":
            singlemaths()
            break

        elif option == "sports":
            singlesports()
            break

        else:
            sys.exit()
def singleart():
    waffle=[" 1st place"," 2nd place"," 3rd place"," 4th place"," 5th place"," 6th place"]
    global point1
    global point2
    global point3
    global point4
    global point5
    global Person
    global Person1
    global Person2
    global Person3
    global Person4
    global Person5
    global Person6
    global Person7
    global Person8
    global Person9
    global Person10
    global Person11
    global Person12
    global Person13
    global Person14
    global Person15
    global Person16
    global Person17
    global Person18
    global Person19
    global Person20    
    for i in range(6):
        try:
        
            point=int(input("Input points for art event" +waffle[i]))
            if point > 0 and point < 20:
                print("Score is set to", point)
                point1.append(point)

            else:
                print(" Enter number between 1 and 20")
                singlesports()
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        

    option=str(input("Input name of individual who came 1st for art "))
    if option == Person[0]:
        Person1=Person1+point1[0]

    elif option == Person[1]:
        Person2=Person2+point1[0]

    elif option == Person[2]:
        Person3=Person3+point1[0]
        
    elif option == Person[3]:
        Person4=Person4+point1[0]

    elif option == Person[4]:
        Person5=Person5+point1[0]

    elif option == Person[5]:
        Person6=Person6+point1[0]

    elif option == Person[6]:
        Person7=Person7+point1[0]

    elif option == Person[7]:
        Person8=Person8+point1[0]

    elif option == Person[8]:
        Person3=Person9+point1[0]

    elif option == Person[9]:
        Person10=Person10+point1[0]

    elif option == Person[10]:
        Person11=Person11+point1[0]

    elif option == Person[11]:
        Person12=Person12+point1[0]

    elif option == Person[12]:
        Person13=Person13+point1[0]

    elif option == Person[13]:
        Person14=Person14+point1[0]

    elif option == Person[14]:
        Person15=Person15+point1[0]

    elif option == Person[15]:
        Person16=Person16+point1[0]

    elif option == Person[16]:
        Person17=Person17+point1[0]

    elif option == Person[17]:
        Person18=Person18+point1[0]

    elif option == Person[18]:
        Person19=Person19+point1[0]

    else:
        Person20=Person20+point1[0]

    option=str(input("Input name of individual who came 2nd "))
    if option == Person[0]:
        Person1=Person1+point1[1]

    elif option == Person[1]:
        Person2=Person2+point1[1]

    elif option == Person[2]:
        Person3=Person3+point1[1]
        
    elif option == Person[3]:
        Person4=Person4+point1[1]

    elif option == Person[4]:
        Person5=Person5+point1[1]

    elif option == Person[5]:
        Person6=Person6+point1[1]

    elif option == Person[6]:
        Person7=Person7+point1[1]

    elif option == Person[7]:
        Person8=Person8+point1[1]

    elif option == Person[8]:
        Person3=Person9+point1[1]

    elif option == Person[9]:
        Person10=Person10+point1[1]

    elif option == Person[10]:
        Person11=Person11+point1[1]

    elif option == Person[11]:
        Person12=Person12+point1[1]

    elif option == Person[12]:
        Person13=Person13+point1[1]

    elif option == Person[13]:
        Person14=Person14+point1[1]

    elif option == Person[14]:
        Person15=Person15+point1[1]

    elif option == Person[15]:
        Person16=Person16+point1[1]

    elif option == Person[16]:
        Person17=Person17+point1[1]

    elif option == Person[17]:
        Person18=Person18+point1[1]

    elif option == Person[18]:
        Person19=Person19+point1[1]

    else:
        Person20=Person20+point1[1]

    option=str(input("Input name of individual who came 3rd "))
    if option == Person[0]:
        Person1=Person1+point1[2]

    elif option == Person[1]:
        Person2=Person2+point1[2]

    elif option == Person[2]:
        Person3=Person3+point1[2]
        
    elif option == Person[3]:
        Person4=Person4+point1[2]

    elif option == Person[4]:
        Person5=Person5+point1[2]

    elif option == Person[5]:
        Person6=Person6+point1[2]

    elif option == Person[6]:
        Person7=Person7+point1[2]

    elif option == Person[7]:
        Person8=Person8+point1[2]

    elif option == Person[8]:
        Person3=Person9+point1[2]

    elif option == Person[9]:
        Person10=Person10+point1[2]

    elif option == Person[10]:
        Person11=Person11+point1[2]

    elif option == Person[11]:
        Person12=Person12+point1[2]

    elif option == Person[12]:
        Person13=Person13+point1[2]

    elif option == Person[13]:
        Person14=Person14+point1[2]

    elif option == Person[14]:
        Person15=Person15+point1[2]

    elif option == Person[15]:
        Person16=Person16+point1[2]

    elif option == Person[16]:
        Person17=Person17+point1[2]

    elif option == Person[17]:
        Person18=Person18+point1[2]

    elif option == Person[18]:
        Person19=Person19+point1[2]

    else:
        Person20=Person20+point[2]
        
    option=str(input("Input name of individual who came 4th "))
    if option == Person[0]:
        Person1=Person1+poin1t[3]

    elif option == Person[1]:
        Person2=Person2+point1[3]

    elif option == Person[2]:
        Person3=Person3+point1[3]
        
    elif option == Person[3]:
        Person4=Person4+point1[3]

    elif option == Person[4]:
        Person5=Person5+point1[3]

    elif option == Person[5]:
        Person6=Person6+point1[3]

    elif option == Person[6]:
        Person7=Person7+point1[3]

    elif option == Person[7]:
        Person8=Person8+point1[3]

    elif option == Person[8]:
        Person3=Person9+point1[3]

    elif option == Person[9]:
        Person10=Person10+point1[3]

    elif option == Person[10]:
        Person11=Person11+point1[3]

    elif option == Person[11]:
        Person12=Person12+point1[3]

    elif option == Person[12]:
        Person13=Person13+point1[3]

    elif option == Person[13]:
        Person14=Person14+point1[3]

    elif option == Person[14]:
        Person15=Person15+point1[3]

    elif option == Person[15]:
        Person16=Person16+point1[3]

    elif option == Person[16]:
        Person17=Person17+point1[3]

    elif option == Person[17]:
        Person18=Person18+point1[3]

    elif option == Person[18]:
        Person19=Person19+point1[3]

    else:
        Person20=Person20+point1[3]
        

    option=str(input("Input name of individual who came 5th "))
    if option == Person[0]:
        Person1=Person1+point1[4]

    elif option == Person[1]:
        Person2=Person2+point1[4]

    elif option == Person[2]:
        Person3=Person3+point1[4]
        
    elif option == Person[3]:
        Person4=Person4+point1[4]

    elif option == Person[4]:
        Person5=Person5+point1[4]

    elif option == Person[5]:
        Person6=Person6+point1[4]

    elif option == Person[6]:
        Person7=Person7+point1[4]

    elif option == Person[7]:
        Person8=Person8+point1[4]

    elif option == Person[8]:
        Person3=Person9+point1[4]

    elif option == Person[9]:
        Person10=Person10+point1[4]

    elif option == Person[10]:
        Person11=Person11+point1[4]

    elif option == Person[11]:
        Person12=Person12+point1[4]

    elif option == Person[12]:
        Person13=Person13+point1[4]

    elif option == Person[13]:
        Person14=Person14+point1[4]

    elif option == Person[14]:
        Person15=Person15+point1[4]

    elif option == Person[15]:
        Person16=Person16+point1[4]

    elif option == Person[16]:
        Person17=Person17+point1[4]

    elif option == Person[17]:
        Person18=Person18+point[4]

    elif option == Person[18]:
        Person19=Person19+point1[4]

    else:
        Person20=Person20+point1[4]


    option=str(input("Input name of individual who came 6th "))
    if option == Person[0]:
        Person1=Person1+point1[5]

    elif option == Person[1]:
        Person2=Person2+point1[5]

    elif option == Person[2]:
        Person3=Person3+point1[5]
        
    elif option == Person[3]:
        Person4=Person4+point1[5]

    elif option == Person[4]:
        Person5=Person5+point1[5]

    elif option == Person[5]:
        Person6=Person6+point1[5]

    elif option == Person[6]:
        Person7=Person7+point1[5]

    elif option == Person[7]:
        Person8=Person8+point1[5]

    elif option == Person[8]:
        Person3=Person9+point1[5]

    elif option == Person[9]:
        Person10=Person10+point1[5]

    elif option == Person[10]:
        Person11=Person11+point1[5]

    elif option == Person[11]:
        Person12=Person12+point1[5]

    elif option == Person[12]:
        Person13=Person13+point1[5]

    elif option == Person[13]:
        Person14=Person14+point1[5]

    elif option == Person[14]:
        Person15=Person15+point1[5]

    elif option == Person[15]:
        Person16=Person16+point1[5]

    elif option == Person[16]:
        Person17=Person17+point1[5]

    elif option == Person[17]:
        Person18=Person18+point1[5]

    elif option == Person[18]:
        Person19=Person19+point1[5]

    else:
        Person20=Person20+point1[5]

    print("1st Place for :" ,Person1)
    print("2nd Place for :" ,Person2)
    print("3rd Place for :" ,Person3)
    print("4th Place for :" ,Person4)
    print("5th Place for :" ,Person5)
    print("6th Place for :" ,Person6)
    print("7th Place for :" ,Person7)
    print("8th Place for :" ,Person8)
    print("9th Place for :" ,Person9)
    print("10th Place for :" ,Person10)
    print("11th Place for :" ,Person11)
    print("12th Place for :" ,Person12)
    print("13th Place for :" ,Person13)
    print("14th Place for :" ,Person14)
    print("15th Place for :" ,Person15)
    print("16th Place for :" ,Person16)
    print("17th Place for :" ,Person17)
    print("18th Place for :" ,Person18)
    print("19th Place for :" ,Person19)
    print("20th Place for :" ,Person20)
    while True:
        option=str(input("enter art, english, science, maths and sports"))
        if option == "art":
            singleart()
            break
        elif option == "english":
            singleenglish()
            break

        elif option == "science":
            singlescience()
            break

        elif option == "maths":
            singlemaths()
            break

        elif option == "sports":
            singlesports()
            break

        else:
            sys.exit()
def singleenglish():
    waffle=[" 1st place"," 2nd place"," 3rd place"," 4th place"," 5th place"," 6th place"]
    global point1
    global point2
    global point3
    global point4
    global point5
    global Person
    global Person1
    global Person2
    global Person3
    global Person4
    global Person5
    global Person6
    global Person7
    global Person8
    global Person9
    global Person10
    global Person11
    global Person12
    global Person13
    global Person14
    global Person15
    global Person16
    global Person17
    global Person18
    global Person19
    global Person20            
    for i in range(6):
    
        try:
        
            point=int(input("Input points for english event" +waffle[i]))
            if point > 0 and point < 20:
                print("Score is set to", point)
                point2.append(point)

            else:
                print("Enter number between 1 and 20")
                singlesports()
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        

    option=str(input("Input name of individual who came 1st for english"))
    if option == Person[0]:
        Person1=Person1+point2[0]

    elif option == Person[1]:
        Person2=Person2+point2[0]

    elif option == Person[2]:
        Person3=Person3+point2[0]
        
    elif option == Person[3]:
        Person4=Person4+point2[0]

    elif option == Person[4]:
        Person5=Person5+point2[0]

    elif option == Person[5]:
        Person6=Person6+point2[0]

    elif option == Person[6]:
        Person7=Person7+point2[0]

    elif option == Person[7]:
        Person8=Person8+point2[0]

    elif option == Person[8]:
        Person3=Person9+point2[0]

    elif option == Person[9]:
        Person10=Person10+point2[0]

    elif option == Person[10]:
        Person11=Person11+point2[0]

    elif option == Person[11]:
        Person12=Person12+point2[0]

    elif option == Person[12]:
        Person13=Person13+point2[0]

    elif option == Person[13]:
        Person14=Person14+point2[0]

    elif option == Person[14]:
        Person15=Person15+point2[0]

    elif option == Person[15]:
        Person16=Person16+point2[0]

    elif option == Person[16]:
        Person17=Person17+point2[0]

    elif option == Person[17]:
        Person18=Person18+point2[0]

    elif option == Person[18]:
        Person19=Person19+point2[0]

    else:
        Person20=Person20+point2[0]

    option=str(input("Input name of individual who came 2nd "))
    if option == Person[0]:
        Person1=Person1+point2[1]

    elif option == Person[1]:
        Person2=Person2+point2[1]

    elif option == Person[2]:
        Person3=Person3+point2[1]
        
    elif option == Person[3]:
        Person4=Person4+point2[1]

    elif option == Person[4]:
        Person5=Person5+point2[1]

    elif option == Person[5]:
        Person6=Person6+point2[1]

    elif option == Person[6]:
        Person7=Person7+point2[1]

    elif option == Person[7]:
        Person8=Person8+point2[1]

    elif option == Person[8]:
        Person3=Person9+point2[1]

    elif option == Person[9]:
        Person10=Person10+point2[1]

    elif option == Person[10]:
        Person11=Person11+point2[1]

    elif option == Person[11]:
        Person12=Person12+point2[1]

    elif option == Person[12]:
        Person13=Person13+point2[1]

    elif option == Person[13]:
        Person14=Person14+point2[1]

    elif option == Person[14]:
        Person15=Person15+point2[1]

    elif option == Person[15]:
        Person16=Person16+point2[1]

    elif option == Person[16]:
        Person17=Person17+point2[1]

    elif option == Person[17]:
        Person18=Person18+point2[1]

    elif option == Person[18]:
        Person19=Person19+point2[1]

    else:
        Person20=Person20+point2[1]

    option=str(input("Input name of individual who came 3rd "))
    if option == Person[0]:
        Person1=Person1+point2[2]

    elif option == Person[1]:
        Person2=Person2+point2[2]

    elif option == Person[2]:
        Person3=Person3+point2[2]
        
    elif option == Person[3]:
        Person4=Person4+point2[2]

    elif option == Person[4]:
        Person5=Person5+point2[2]

    elif option == Person[5]:
        Person6=Person6+point2[2]

    elif option == Person[6]:
        Person7=Person7+point2[2]

    elif option == Person[7]:
        Person8=Person8+point2[2]

    elif option == Person[8]:
        Person3=Person9+point2[2]

    elif option == Person[9]:
        Person10=Person10+point2[2]

    elif option == Person[10]:
        Person11=Person11+point2[2]

    elif option == Person[11]:
        Person12=Person12+point2[2]

    elif option == Person[12]:
        Person13=Person13+point2[2]

    elif option == Person[13]:
        Person14=Person14+point2[2]

    elif option == Person[14]:
        Person15=Person15+point2[2]

    elif option == Person[15]:
        Person16=Person16+point2[2]

    elif option == Person[16]:
        Person17=Person17+point2[2]

    elif option == Person[17]:
        Person18=Person18+point2[2]

    elif option == Person[18]:
        Person19=Person19+point2[2]

    else:
        Person20=Person20+point[2]
        
    option=str(input("Input name of individual who came 4th "))
    if option == Person[0]:
        Person1=Person1+point2[3]

    elif option == Person[1]:
        Person2=Person2+point2[3]

    elif option == Person[2]:
        Person3=Person3+point2[3]
        
    elif option == Person[3]:
        Person4=Person4+point2[3]

    elif option == Person[4]:
        Person5=Person5+point2[3]

    elif option == Person[5]:
        Person6=Person6+point2[3]

    elif option == Person[6]:
        Person7=Person7+point2[3]

    elif option == Person[7]:
        Person8=Person8+point2[3]

    elif option == Person[8]:
        Person3=Person9+point2[3]

    elif option == Person[9]:
        Person10=Person10+point2[3]

    elif option == Person[10]:
        Person11=Person11+point2[3]

    elif option == Person[11]:
        Person12=Person12+point2[3]

    elif option == Person[12]:
        Person13=Person13+point2[3]

    elif option == Person[13]:
        Person14=Person14+point2[3]

    elif option == Person[14]:
        Person15=Person15+point2[3]

    elif option == Person[15]:
        Person16=Person16+point2[3]

    elif option == Person[16]:
        Person17=Person17+point2[3]

    elif option == Person[17]:
        Person18=Person18+point2[3]

    elif option == Person[18]:
        Person19=Person19+point2[3]

    else:
        Person20=Person20+point2[3]
        

    option=str(input("Input name of individual who came 5th "))
    if option == Person[0]:
        Person1=Person1+point2[4]

    elif option == Person[1]:
        Person2=Person2+point2[4]

    elif option == Person[2]:
        Person3=Person3+point2[4]
        
    elif option == Person[3]:
        Person4=Person4+point2[4]

    elif option == Person[4]:
        Person5=Person5+point2[4]

    elif option == Person[5]:
        Person6=Person6+point2[4]

    elif option == Person[6]:
        Person7=Person7+point2[4]

    elif option == Person[7]:
        Person8=Person8+point2[4]

    elif option == Person[8]:
        Person3=Person9+point2[4]

    elif option == Person[9]:
        Person10=Person10+point2[4]

    elif option == Person[10]:
        Person11=Person11+point2[4]

    elif option == Person[11]:
        Person12=Person12+point2[4]

    elif option == Person[12]:
        Person13=Person13+point2[4]

    elif option == Person[13]:
        Person14=Person14+point2[4]

    elif option == Person[14]:
        Person15=Person15+point2[4]

    elif option == Person[15]:
        Person16=Person16+point2[4]

    elif option == Person[16]:
        Person17=Person17+point2[4]

    elif option == Person[17]:
        Person18=Person18+point2[4]

    elif option == Person[18]:
        Person19=Person19+point2[4]

    else:
        Person20=Person20+point2[4]


    option=str(input("Input name of individual who came 6th "))
    if option == Person[0]:
        Person1=Person1+point2[5]

    elif option == Person[1]:
        Person2=Person2+point2[5]

    elif option == Person[2]:
        Person3=Person3+point2[5]
        
    elif option == Person[3]:
        Person4=Person4+point2[5]

    elif option == Person[4]:
        Person5=Person5+point2[5]

    elif option == Person[5]:
        Person6=Person6+point2[5]

    elif option == Person[6]:
        Person7=Person7+point2[5]

    elif option == Person[7]:
        Person8=Person8+point2[5]

    elif option == Person[8]:
        Person3=Person9+point2[5]

    elif option == Person[9]:
        Person10=Person10+point2[5]

    elif option == Person[10]:
        Person11=Person11+point2[5]

    elif option == Person[11]:
        Person12=Person12+point2[5]

    elif option == Person[12]:
        Person13=Person13+point2[5]

    elif option == Person[13]:
        Person14=Person14+point2[5]

    elif option == Person[14]:
        Person15=Person15+point2[5]

    elif option == Person[15]:
        Person16=Person16+point2[5]

    elif option == Person[16]:
        Person17=Person17+point2[5]

    elif option == Person[17]:
        Person18=Person18+point2[5]

    elif option == Person[18]:
        Person19=Person19+point2[5]

    else:
        Person20=Person20+point2[5]
    print("1st Place for :" ,Person1)
    print("2nd Place for :" ,Person2)
    print("3rd Place for :" ,Person3)
    print("4th Place for :" ,Person4)
    print("5th Place for :" ,Person5)
    print("6th Place for :" ,Person6)
    print("7th Place for :" ,Person7)
    print("8th Place for :" ,Person8)
    print("9th Place for :" ,Person9)
    print("10th Place for :" ,Person10)
    print("11th Place for :" ,Person11)
    print("12th Place for :" ,Person12)
    print("13th Place for :" ,Person13)
    print("14th Place for :" ,Person14)
    print("15th Place for :" ,Person15)
    print("16th Place for :" ,Person16)
    print("17th Place for :" ,Person17)
    print("18th Place for :" ,Person18)
    print("19th Place for :" ,Person19)
    print("20th Place for :" ,Person20)        
    while True:
        option=str(input("enter art, english, science, maths and sports"))
        if option == "art":
            singleart()
            break
        elif option == "english":
            singleenglish()
            break

        elif option == "science":
            singlescience()
            break

        elif option == "maths":
            singlemaths()
            break

        elif option == "sports":
            singlesports()
            break

        else:
            sys.exit()
def multipleforindividual():
    waffle=[" 1st place"," 2nd place"," 3rd place"," 4th place"," 5th place"," 6th place"]
    global point1
    global point2
    global point3
    global point4
    global point5
    global Person
    global Person1
    global Person2
    global Person3
    global Person4
    global Person5
    global Person6
    global Person7
    global Person8
    global Person9
    global Person10
    global Person11
    global Person12
    global Person13
    global Person14
    global Person15
    global Person16
    global Person17
    global Person18
    global Person19
    global Person20
    print("input points starting from highest to lowest")

    for i in range(6):
        while True:
            try:
             
                point=int(input("Input points for art event "+waffle[i]))
                if point > 0 and point < 20:
                    print("Score is set to", point)
                    point1.append(point)

                else:
                    print("Enter a number between 1 and 20 ")
                    continue 
            except ValueError:
                print("Please make sure you enter a number!")
                continue
            break
                    

    for i in range(6):
        while True:
            try:
            
                point=int(input("Input points for english event "+waffle[i]))
                if point > 0 and point < 20:
                    print("Score is set to", point)
                    point2.append(point)

                else:
                    print("Enter a number between 1 and 20 ")
                    continue 
            except ValueError:
                print("Please make sure you enter a number!")
                continue
            break
            

    for i in range(6):
        while True:
            try:
            
                point=int(input("Input points for science event "+waffle[i]))
                if point > 0 and point < 20:
                    print("Score is set to", point)
                    point3.append(point)

                else:
                    print("Enter a number between 1 and 20 ")
                    continue 
            except ValueError:
                print("Please make sure you enter a number!")
                continue
            break

    for i in range(6):
        while True:
            try:
            
                point=int(input("Input points for maths event "+waffle[i]))
                if point > 0 and point < 20:
                    print("Score is set to", point)
                    point4.append(point)

                else:
                    print("Enter a number between 1 and 20 ")
                    continue 
            except ValueError:
                print("Please make sure you enter a number!")
                continue
            break
        
    for i in range(6):
        while True:
            try:
            
                point=int(input("Input points for sports event "+waffle[i]))
                if point > 0 and point < 20:
                    print("Score is set to", point)
                    point5.append(point)

                else:
                    print("Enter a number between 1 and 20 ")
                    continue 
            except ValueError:
                print("Please make sure you enter a number!")
                continue
            break
        
    option=str(input("Input name of individual who came 1st for art "))
    if option == Person[0]:
        Person1=Person1+point1[0]

    elif option == Person[1]:
        Person2=Person2+point1[0]

    elif option == Person[2]:
        Person3=Person3+point1[0]
        
    elif option == Person[3]:
        Person4=Person4+point1[0]

    elif option == Person[4]:
        Person5=Person5+point1[0]

    elif option == Person[5]:
        Person6=Person6+point1[0]

    elif option == Person[6]:
        Person7=Person7+point1[0]

    elif option == Person[7]:
        Person8=Person8+point1[0]

    elif option == Person[8]:
        Person3=Person9+point1[0]

    elif option == Person[9]:
        Person10=Person10+point1[0]

    elif option == Person[10]:
        Person11=Person11+point1[0]

    elif option == Person[11]:
        Person12=Person12+point1[0]

    elif option == Person[12]:
        Person13=Person13+point1[0]

    elif option == Person[13]:
        Person14=Person14+point1[0]

    elif option == Person[14]:
        Person15=Person15+point1[0]

    elif option == Person[15]:
        Person16=Person16+point1[0]

    elif option == Person[16]:
        Person17=Person17+point1[0]

    elif option == Person[17]:
        Person18=Person18+point1[0]

    elif option == Person[18]:
        Person19=Person19+point1[0]

    else:
        Person20=Person20+point1[0]

    option=str(input("Input name of individual who came 2nd "))
    if option == Person[0]:
        Person1=Person1+point1[1]

    elif option == Person[1]:
        Person2=Person2+point1[1]

    elif option == Person[2]:
        Person3=Person3+point1[1]
        
    elif option == Person[3]:
        Person4=Person4+point1[1]

    elif option == Person[4]:
        Person5=Person5+point1[1]

    elif option == Person[5]:
        Person6=Person6+point1[1]

    elif option == Person[6]:
        Person7=Person7+point1[1]

    elif option == Person[7]:
        Person8=Person8+point1[1]

    elif option == Person[8]:
        Person3=Person9+point1[1]

    elif option == Person[9]:
        Person10=Person10+point1[1]

    elif option == Person[10]:
        Person11=Person11+point1[1]

    elif option == Person[11]:
        Person12=Person12+point1[1]

    elif option == Person[12]:
        Person13=Person13+point1[1]

    elif option == Person[13]:
        Person14=Person14+point1[1]

    elif option == Person[14]:
        Person15=Person15+point1[1]

    elif option == Person[15]:
        Person16=Person16+point1[1]

    elif option == Person[16]:
        Person17=Person17+point1[1]

    elif option == Person[17]:
        Person18=Person18+point1[1]

    elif option == Person[18]:
        Person19=Person19+point1[1]

    else:
        Person20=Person20+point1[1]

    option=str(input("Input name of individual who came 3rd "))
    if option == Person[0]:
        Person1=Person1+point1[2]

    elif option == Person[1]:
        Person2=Person2+point1[2]

    elif option == Person[2]:
        Person3=Person3+point1[2]
        
    elif option == Person[3]:
        Person4=Person4+point1[2]

    elif option == Person[4]:
        Person5=Person5+point1[2]

    elif option == Person[5]:
        Person6=Person6+point1[2]

    elif option == Person[6]:
        Person7=Person7+point1[2]

    elif option == Person[7]:
        Person8=Person8+point1[2]

    elif option == Person[8]:
        Person3=Person9+point1[2]

    elif option == Person[9]:
        Person10=Person10+point1[2]

    elif option == Person[10]:
        Person11=Person11+point1[2]

    elif option == Person[11]:
        Person12=Person12+point1[2]

    elif option == Person[12]:
        Person13=Person13+point1[2]

    elif option == Person[13]:
        Person14=Person14+point1[2]

    elif option == Person[14]:
        Person15=Person15+point1[2]

    elif option == Person[15]:
        Person16=Person16+point1[2]

    elif option == Person[16]:
        Person17=Person17+point1[2]

    elif option == Person[17]:
        Person18=Person18+point1[2]

    elif option == Person[18]:
        Person19=Person19+point1[2]

    else:
        Person20=Person20+point[2]
        
    option=str(input("Input name of individual who came 4th "))
    if option == Person[0]:
        Person1=Person1+poin1t[3]

    elif option == Person[1]:
        Person2=Person2+point1[3]

    elif option == Person[2]:
        Person3=Person3+point1[3]
        
    elif option == Person[3]:
        Person4=Person4+point1[3]

    elif option == Person[4]:
        Person5=Person5+point1[3]

    elif option == Person[5]:
        Person6=Person6+point1[3]

    elif option == Person[6]:
        Person7=Person7+point1[3]

    elif option == Person[7]:
        Person8=Person8+point1[3]

    elif option == Person[8]:
        Person3=Person9+point1[3]

    elif option == Person[9]:
        Person10=Person10+point1[3]

    elif option == Person[10]:
        Person11=Person11+point1[3]

    elif option == Person[11]:
        Person12=Person12+point1[3]

    elif option == Person[12]:
        Person13=Person13+point1[3]

    elif option == Person[13]:
        Person14=Person14+point1[3]

    elif option == Person[14]:
        Person15=Person15+point1[3]

    elif option == Person[15]:
        Person16=Person16+point1[3]

    elif option == Person[16]:
        Person17=Person17+point1[3]

    elif option == Person[17]:
        Person18=Person18+point1[3]

    elif option == Person[18]:
        Person19=Person19+point1[3]

    else:
        Person20=Person20+point1[3]
        

    option=str(input("Input name of individual who came 5th "))
    if option == Person[0]:
        Person1=Person1+point1[4]

    elif option == Person[1]:
        Person2=Person2+point1[4]

    elif option == Person[2]:
        Person3=Person3+point1[4]
        
    elif option == Person[3]:
        Person4=Person4+point1[4]

    elif option == Person[4]:
        Person5=Person5+point1[4]

    elif option == Person[5]:
        Person6=Person6+point1[4]

    elif option == Person[6]:
        Person7=Person7+point1[4]

    elif option == Person[7]:
        Person8=Person8+point1[4]

    elif option == Person[8]:
        Person3=Person9+point1[4]

    elif option == Person[9]:
        Person10=Person10+point1[4]

    elif option == Person[10]:
        Person11=Person11+point1[4]

    elif option == Person[11]:
        Person12=Person12+point1[4]

    elif option == Person[12]:
        Person13=Person13+point1[4]

    elif option == Person[13]:
        Person14=Person14+point1[4]

    elif option == Person[14]:
        Person15=Person15+point1[4]

    elif option == Person[15]:
        Person16=Person16+point1[4]

    elif option == Person[16]:
        Person17=Person17+point1[4]

    elif option == Person[17]:
        Person18=Person18+point[4]

    elif option == Person[18]:
        Person19=Person19+point1[4]

    else:
        Person20=Person20+point1[4]


    option=str(input("Input name of individual who came 6th "))
    if option == Person[0]:
        Person1=Person1+point1[5]

    elif option == Person[1]:
        Person2=Person2+point1[5]

    elif option == Person[2]:
        Person3=Person3+point1[5]
        
    elif option == Person[3]:
        Person4=Person4+point1[5]

    elif option == Person[4]:
        Person5=Person5+point1[5]

    elif option == Person[5]:
        Person6=Person6+point1[5]

    elif option == Person[6]:
        Person7=Person7+point1[5]

    elif option == Person[7]:
        Person8=Person8+point1[5]

    elif option == Person[8]:
        Person3=Person9+point1[5]

    elif option == Person[9]:
        Person10=Person10+point1[5]

    elif option == Person[10]:
        Person11=Person11+point1[5]

    elif option == Person[11]:
        Person12=Person12+point1[5]

    elif option == Person[12]:
        Person13=Person13+point1[5]

    elif option == Person[13]:
        Person14=Person14+point1[5]

    elif option == Person[14]:
        Person15=Person15+point1[5]

    elif option == Person[15]:
        Person16=Person16+point1[5]

    elif option == Person[16]:
        Person17=Person17+point1[5]

    elif option == Person[17]:
        Person18=Person18+point1[5]

    elif option == Person[18]:
        Person19=Person19+point1[5]

    else:
        Person20=Person20+point1[5]


    option=str(input("Input name of individual who came 1st for english"))
    if option == Person[0]:
        Person1=Person1+point2[0]

    elif option == Person[1]:
        Person2=Person2+point2[0]

    elif option == Person[2]:
        Person3=Person3+point2[0]
        
    elif option == Person[3]:
        Person4=Person4+point2[0]

    elif option == Person[4]:
        Person5=Person5+point2[0]

    elif option == Person[5]:
        Person6=Person6+point2[0]

    elif option == Person[6]:
        Person7=Person7+point2[0]

    elif option == Person[7]:
        Person8=Person8+point2[0]

    elif option == Person[8]:
        Person3=Person9+point2[0]

    elif option == Person[9]:
        Person10=Person10+point2[0]

    elif option == Person[10]:
        Person11=Person11+point2[0]

    elif option == Person[11]:
        Person12=Person12+point2[0]

    elif option == Person[12]:
        Person13=Person13+point2[0]

    elif option == Person[13]:
        Person14=Person14+point2[0]

    elif option == Person[14]:
        Person15=Person15+point2[0]

    elif option == Person[15]:
        Person16=Person16+point2[0]

    elif option == Person[16]:
        Person17=Person17+point2[0]

    elif option == Person[17]:
        Person18=Person18+point2[0]

    elif option == Person[18]:
        Person19=Person19+point2[0]

    else:
        Person20=Person20+point2[0]

    option=str(input("Input name of individual who came 2nd "))
    if option == Person[0]:
        Person1=Person1+point2[1]

    elif option == Person[1]:
        Person2=Person2+point2[1]

    elif option == Person[2]:
        Person3=Person3+point2[1]
        
    elif option == Person[3]:
        Person4=Person4+point2[1]

    elif option == Person[4]:
        Person5=Person5+point2[1]

    elif option == Person[5]:
        Person6=Person6+point2[1]

    elif option == Person[6]:
        Person7=Person7+point2[1]

    elif option == Person[7]:
        Person8=Person8+point2[1]

    elif option == Person[8]:
        Person3=Person9+point2[1]

    elif option == Person[9]:
        Person10=Person10+point2[1]

    elif option == Person[10]:
        Person11=Person11+point2[1]

    elif option == Person[11]:
        Person12=Person12+point2[1]

    elif option == Person[12]:
        Person13=Person13+point2[1]

    elif option == Person[13]:
        Person14=Person14+point2[1]

    elif option == Person[14]:
        Person15=Person15+point2[1]

    elif option == Person[15]:
        Person16=Person16+point2[1]

    elif option == Person[16]:
        Person17=Person17+point2[1]

    elif option == Person[17]:
        Person18=Person18+point2[1]

    elif option == Person[18]:
        Person19=Person19+point2[1]

    else:
        Person20=Person20+point2[1]

    option=str(input("Input name of individual who came 3rd "))
    if option == Person[0]:
        Person1=Person1+point2[2]

    elif option == Person[1]:
        Person2=Person2+point2[2]

    elif option == Person[2]:
        Person3=Person3+point2[2]
        
    elif option == Person[3]:
        Person4=Person4+point2[2]

    elif option == Person[4]:
        Person5=Person5+point2[2]

    elif option == Person[5]:
        Person6=Person6+point2[2]

    elif option == Person[6]:
        Person7=Person7+point2[2]

    elif option == Person[7]:
        Person8=Person8+point2[2]

    elif option == Person[8]:
        Person3=Person9+point2[2]

    elif option == Person[9]:
        Person10=Person10+point2[2]

    elif option == Person[10]:
        Person11=Person11+point2[2]

    elif option == Person[11]:
        Person12=Person12+point2[2]

    elif option == Person[12]:
        Person13=Person13+point2[2]

    elif option == Person[13]:
        Person14=Person14+point2[2]

    elif option == Person[14]:
        Person15=Person15+point2[2]

    elif option == Person[15]:
        Person16=Person16+point2[2]

    elif option == Person[16]:
        Person17=Person17+point2[2]

    elif option == Person[17]:
        Person18=Person18+point2[2]

    elif option == Person[18]:
        Person19=Person19+point2[2]

    else:
        Person20=Person20+point[2]
        
    option=str(input("Input name of individual who came 4th "))
    if option == Person[0]:
        Person1=Person1+point2[3]

    elif option == Person[1]:
        Person2=Person2+point2[3]

    elif option == Person[2]:
        Person3=Person3+point2[3]
        
    elif option == Person[3]:
        Person4=Person4+point2[3]

    elif option == Person[4]:
        Person5=Person5+point2[3]

    elif option == Person[5]:
        Person6=Person6+point2[3]

    elif option == Person[6]:
        Person7=Person7+point2[3]

    elif option == Person[7]:
        Person8=Person8+point2[3]

    elif option == Person[8]:
        Person3=Person9+point2[3]

    elif option == Person[9]:
        Person10=Person10+point2[3]

    elif option == Person[10]:
        Person11=Person11+point2[3]

    elif option == Person[11]:
        Person12=Person12+point2[3]

    elif option == Person[12]:
        Person13=Person13+point2[3]

    elif option == Person[13]:
        Person14=Person14+point2[3]

    elif option == Person[14]:
        Person15=Person15+point2[3]

    elif option == Person[15]:
        Person16=Person16+point2[3]

    elif option == Person[16]:
        Person17=Person17+point2[3]

    elif option == Person[17]:
        Person18=Person18+point2[3]

    elif option == Person[18]:
        Person19=Person19+point2[3]

    else:
        Person20=Person20+point2[3]
        

    option=str(input("Input name of individual who came 5th "))
    if option == Person[0]:
        Person1=Person1+point2[4]

    elif option == Person[1]:
        Person2=Person2+point2[4]

    elif option == Person[2]:
        Person3=Person3+point2[4]
        
    elif option == Person[3]:
        Person4=Person4+point2[4]

    elif option == Person[4]:
        Person5=Person5+point2[4]

    elif option == Person[5]:
        Person6=Person6+point2[4]

    elif option == Person[6]:
        Person7=Person7+point2[4]

    elif option == Person[7]:
        Person8=Person8+point2[4]

    elif option == Person[8]:
        Person3=Person9+point2[4]

    elif option == Person[9]:
        Person10=Person10+point2[4]

    elif option == Person[10]:
        Person11=Person11+point2[4]

    elif option == Person[11]:
        Person12=Person12+point2[4]

    elif option == Person[12]:
        Person13=Person13+point2[4]

    elif option == Person[13]:
        Person14=Person14+point2[4]

    elif option == Person[14]:
        Person15=Person15+point2[4]

    elif option == Person[15]:
        Person16=Person16+point2[4]

    elif option == Person[16]:
        Person17=Person17+point2[4]

    elif option == Person[17]:
        Person18=Person18+point2[4]

    elif option == Person[18]:
        Person19=Person19+point2[4]

    else:
        Person20=Person20+point2[4]


    option=str(input("Input name of individual who came 6th "))
    if option == Person[0]:
        Person1=Person1+point2[5]

    elif option == Person[1]:
        Person2=Person2+point2[5]

    elif option == Person[2]:
        Person3=Person3+point2[5]
        
    elif option == Person[3]:
        Person4=Person4+point2[5]

    elif option == Person[4]:
        Person5=Person5+point2[5]

    elif option == Person[5]:
        Person6=Person6+point2[5]

    elif option == Person[6]:
        Person7=Person7+point2[5]

    elif option == Person[7]:
        Person8=Person8+point2[5]

    elif option == Person[8]:
        Person3=Person9+point2[5]

    elif option == Person[9]:
        Person10=Person10+point2[5]

    elif option == Person[10]:
        Person11=Person11+point2[5]

    elif option == Person[11]:
        Person12=Person12+point2[5]

    elif option == Person[12]:
        Person13=Person13+point2[5]

    elif option == Person[13]:
        Person14=Person14+point2[5]

    elif option == Person[14]:
        Person15=Person15+point2[5]

    elif option == Person[15]:
        Person16=Person16+point2[5]

    elif option == Person[16]:
        Person17=Person17+point2[5]

    elif option == Person[17]:
        Person18=Person18+point2[5]

    elif option == Person[18]:
        Person19=Person19+point2[5]

    else:
        Person20=Person20+point2[5]

    option=str(input("Input name of individual who came 1st for science"))
    if option == Person[0]:
        Person1=Person1+point3[0]

    elif option == Person[1]:
        Person2=Person2+point3[0]

    elif option == Person[2]:
        Person3=Person3+point3[0]
        
    elif option == Person[3]:
        Person4=Person4+point3[0]

    elif option == Person[4]:
        Person5=Person5+point3[0]

    elif option == Person[5]:
        Person6=Person6+point3[0]

    elif option == Person[6]:
        Person7=Person7+point3[0]

    elif option == Person[7]:
        Person8=Person8+point3[0]

    elif option == Person[8]:
        Person3=Person9+point3[0]

    elif option == Person[9]:
        Person10=Person10+point3[0]

    elif option == Person[10]:
        Person11=Person11+point3[0]

    elif option == Person[11]:
        Person12=Person12+point3[0]

    elif option == Person[12]:
        Person13=Person13+point3[0]

    elif option == Person[13]:
        Person14=Person14+point3[0]

    elif option == Person[14]:
        Person15=Person15+point3[0]

    elif option == Person[15]:
        Person16=Person16+point3[0]

    elif option == Person[16]:
        Person17=Person17+point3[0]

    elif option == Person[17]:
        Person18=Person18+point3[0]

    elif option == Person[18]:
        Person19=Person19+point3[0]

    else:
        Person20=Person20+point3[0]

    option=str(input("Input name of individual who came 2nd "))
    if option == Person[0]:
        Person1=Person1+point3[1]

    elif option == Person[1]:
        Person2=Person2+point3[1]

    elif option == Person[2]:
        Person3=Person3+point3[1]
        
    elif option == Person[3]:
        Person4=Person4+point3[1]

    elif option == Person[4]:
        Person5=Person5+point3[1]

    elif option == Person[5]:
        Person6=Person6+point3[1]

    elif option == Person[6]:
        Person7=Person7+point3[1]

    elif option == Person[7]:
        Person8=Person8+point3[1]

    elif option == Person[8]:
        Person3=Person9+point3[1]

    elif option == Person[9]:
        Person10=Person10+point3[1]

    elif option == Person[10]:
        Person11=Person11+point3[1]

    elif option == Person[11]:
        Person12=Person12+point3[1]

    elif option == Person[12]:
        Person13=Person13+point3[1]

    elif option == Person[13]:
        Person14=Person14+point3[1]

    elif option == Person[14]:
        Person15=Person15+point3[1]

    elif option == Person[15]:
        Person16=Person16+point3[1]

    elif option == Person[16]:
        Person17=Person17+point3[1]

    elif option == Person[17]:
        Person18=Person18+point3[1]

    elif option == Person[18]:
        Person19=Person19+point3[1]

    else:
        Person20=Person20+point3[1]

    option=str(input("Input name of individual who came 3rd "))
    if option == Person[0]:
        Person1=Person1+point3[2]

    elif option == Person[1]:
        Person2=Person2+point3[2]

    elif option == Person[2]:
        Person3=Person3+point3[2]
        
    elif option == Person[3]:
        Person4=Person4+point3[2]

    elif option == Person[4]:
        Person5=Person5+point3[2]

    elif option == Person[5]:
        Person6=Person6+point3[2]

    elif option == Person[6]:
        Person7=Person7+point3[2]

    elif option == Person[7]:
        Person8=Person8+point3[2]

    elif option == Person[8]:
        Person3=Person9+point3[2]

    elif option == Person[9]:
        Person10=Person10+point3[2]

    elif option == Person[10]:
        Person11=Person11+point3[2]

    elif option == Person[11]:
        Person12=Person12+point3[2]

    elif option == Person[12]:
        Person13=Person13+point3[2]

    elif option == Person[13]:
        Person14=Person14+point3[2]

    elif option == Person[14]:
        Person15=Person15+point3[2]

    elif option == Person[15]:
        Person16=Person16+point3[2]

    elif option == Person[16]:
        Person17=Person17+point3[2]

    elif option == Person[17]:
        Person18=Person18+point3[2]

    elif option == Person[18]:
        Person19=Person19+point3[2]

    else:
        Person20=Person20+point3[2]
        
    option=str(input("Input name of individual who came 4th "))
    if option == Person[0]:
        Person1=Person1+point3[3]

    elif option == Person[1]:
        Person2=Person2+point3[3]

    elif option == Person[2]:
        Person3=Person3+point3[3]
        
    elif option == Person[3]:
        Person4=Person4+point3[3]

    elif option == Person[4]:
        Person5=Person5+point3[3]

    elif option == Person[5]:
        Person6=Person6+point3[3]

    elif option == Person[6]:
        Person7=Person7+point3[3]

    elif option == Person[7]:
        Person8=Person8+point3[3]

    elif option == Person[8]:
        Person3=Person9+point3[3]

    elif option == Person[9]:
        Person10=Person10+point3[3]

    elif option == Person[10]:
        Person11=Person11+point3[3]

    elif option == Person[11]:
        Person12=Person12+point3[3]

    elif option == Person[12]:
        Person13=Person13+point3[3]

    elif option == Person[13]:
        Person14=Person14+point3[3]

    elif option == Person[14]:
        Person15=Person15+point3[3]

    elif option == Person[15]:
        Person16=Person16+point3[3]

    elif option == Person[16]:
        Person17=Person17+point3[3]

    elif option == Person[17]:
        Person18=Person18+point3[3]

    elif option == Person[18]:
        Person19=Person19+point3[3]

    else:
        Person20=Person20+point3[3]
        

    option=str(input("Input name of individual who came 5th "))
    if option == Person[0]:
        Person1=Person1+point3[4]

    elif option == Person[1]:
        Person2=Person2+point3[4]

    elif option == Person[2]:
        Person3=Person3+point3[4]
        
    elif option == Person[3]:
        Person4=Person4+point3[4]

    elif option == Person[4]:
        Person5=Person5+point3[4]

    elif option == Person[5]:
        Person6=Person6+point3[4]

    elif option == Person[6]:
        Person7=Person7+point3[4]

    elif option == Person[7]:
        Person8=Person8+point3[4]

    elif option == Person[8]:
        Person3=Person9+point3[4]

    elif option == Person[9]:
        Person10=Person10+point3[4]

    elif option == Person[10]:
        Person11=Person11+point3[4]

    elif option == Person[11]:
        Person12=Person12+point3[4]

    elif option == Person[12]:
        Person13=Person13+point3[4]

    elif option == Person[13]:
        Person14=Person14+point3[4]

    elif option == Person[14]:
        Person15=Person15+point3[4]

    elif option == Person[15]:
        Person16=Person16+point3[4]

    elif option == Person[16]:
        Person17=Person17+point3[4]

    elif option == Person[17]:
        Person18=Person18+point3[4]

    elif option == Person[18]:
        Person19=Person19+point3[4]

    else:
        Person20=Person20+point3[4]


    option=str(input("Input name of individual who came 6th "))
    if option == Person[0]:
        Person1=Person1+point3[5]

    elif option == Person[1]:
        Person2=Person2+point3[5]

    elif option == Person[2]:
        Person3=Person3+point3[5]
        
    elif option == Person[3]:
        Person4=Person4+point3[5]

    elif option == Person[4]:
        Person5=Person5+point3[5]

    elif option == Person[5]:
        Person6=Person6+point3[5]

    elif option == Person[6]:
        Person7=Person7+point3[5]

    elif option == Person[7]:
        Person8=Person8+point3[5]

    elif option == Person[8]:
        Person3=Person9+point3[5]

    elif option == Person[9]:
        Person10=Person10+point3[5]

    elif option == Person[10]:
        Person11=Person11+point3[5]

    elif option == Person[11]:
        Person12=Person12+point3[5]

    elif option == Person[12]:
        Person13=Person13+point3[5]

    elif option == Person[13]:
        Person14=Person14+point3[5]

    elif option == Person[14]:
        Person15=Person15+point3[5]

    elif option == Person[15]:
        Person16=Person16+point3[5]

    elif option == Person[16]:
        Person17=Person17+point3[5]

    elif option == Person[17]:
        Person18=Person18+point3[5]

    elif option == Person[18]:
        Person19=Person19+point3[5]

    else:
        Person20=Person20+point3[5]

    option=str(input("Input name of individual who came 1st for maths"))
    if option == Person[0]:
        Person1=Person1+point4[0]

    elif option == Person[1]:
        Person2=Person2+point4[0]

    elif option == Person[2]:
        Person3=Person3+point4[0]
        
    elif option == Person[3]:
        Person4=Person4+point4[0]

    elif option == Person[4]:
        Person5=Person5+point4[0]

    elif option == Person[5]:
        Person6=Person6+point4[0]

    elif option == Person[6]:
        Person7=Person7+point4[0]

    elif option == Person[7]:
        Person8=Person8+point4[0]

    elif option == Person[8]:
        Person3=Person9+point4[0]

    elif option == Person[9]:
        Person10=Person10+point4[0]

    elif option == Person[10]:
        Person11=Person11+point4[0]

    elif option == Person[11]:
        Person12=Person12+point4[0]

    elif option == Person[12]:
        Person13=Person13+point4[0]

    elif option == Person[13]:
        Person14=Person14+point4[0]

    elif option == Person[14]:
        Person15=Person15+point4[0]

    elif option == Person[15]:
        Person16=Person16+point4[0]

    elif option == Person[16]:
        Person17=Person17+point4[0]

    elif option == Person[17]:
        Person18=Person18+point4[0]

    elif option == Person[18]:
        Person19=Person19+point4[0]

    else:
        Person20=Person20+point4[0]

    option=str(input("Input name of individual who came 2nd "))
    if option == Person[0]:
        Person1=Person1+point4[1]

    elif option == Person[1]:
        Person2=Person2+point4[1]

    elif option == Person[2]:
        Person3=Person3+point4[1]
        
    elif option == Person[3]:
        Person4=Person4+point4[1]

    elif option == Person[4]:
        Person5=Person5+point4[1]

    elif option == Person[5]:
        Person6=Person6+point4[1]

    elif option == Person[6]:
        Person7=Person7+point4[1]

    elif option == Person[7]:
        Person8=Person8+point4[1]

    elif option == Person[8]:
        Person3=Person9+point4[1]

    elif option == Person[9]:
        Person10=Person10+point4[1]

    elif option == Person[10]:
        Person11=Person11+point4[1]

    elif option == Person[11]:
        Person12=Person12+point4[1]

    elif option == Person[12]:
        Person13=Person13+point4[1]

    elif option == Person[13]:
        Person14=Person14+point4[1]

    elif option == Person[14]:
        Person15=Person15+point4[1]

    elif option == Person[15]:
        Person16=Person16+point4[1]

    elif option == Person[16]:
        Person17=Person17+point4[1]

    elif option == Person[17]:
        Person18=Person18+point4[1]

    elif option == Person[18]:
        Person19=Person19+point4[1]

    else:
        Person20=Person20+point4[1]

    option=str(input("Input name of individual who came 3rd "))
    if option == Person[0]:
        Person1=Person1+point4[2]

    elif option == Person[1]:
        Person2=Person2+point4[2]

    elif option == Person[2]:
        Person3=Person3+point4[2]
        
    elif option == Person[3]:
        Person4=Person4+point4[2]

    elif option == Person[4]:
        Person5=Person5+point4[2]

    elif option == Person[5]:
        Person6=Person6+point4[2]

    elif option == Person[6]:
        Person7=Person7+point4[2]

    elif option == Person[7]:
        Person8=Person8+point4[2]

    elif option == Person[8]:
        Person3=Person9+point4[2]

    elif option == Person[9]:
        Person10=Person10+point4[2]

    elif option == Person[10]:
        Person11=Person11+point4[2]

    elif option == Person[11]:
        Person12=Person12+point4[2]

    elif option == Person[12]:
        Person13=Person13+point4[2]

    elif option == Person[13]:
        Person14=Person14+point4[2]

    elif option == Person[14]:
        Person15=Person15+point4[2]

    elif option == Person[15]:
        Person16=Person16+point4[2]

    elif option == Person[16]:
        Person17=Person17+point4[2]

    elif option == Person[17]:
        Person18=Person18+point4[2]

    elif option == Person[18]:
        Person19=Person19+point4[2]

    else:
        Person20=Person20+point4[2]
        
    option=str(input("Input name of individual who came 4th "))
    if option == Person[0]:
        Person1=Person1+point4[3]

    elif option == Person[1]:
        Person2=Person2+point4[3]

    elif option == Person[2]:
        Person3=Person3+point4[3]
        
    elif option == Person[3]:
        Person4=Person4+point4[3]

    elif option == Person[4]:
        Person5=Person5+point4[3]

    elif option == Person[5]:
        Person6=Person6+point4[3]

    elif option == Person[6]:
        Person7=Person7+point4[3]

    elif option == Person[7]:
        Person8=Person8+point4[3]

    elif option == Person[8]:
        Person3=Person9+point4[3]

    elif option == Person[9]:
        Person10=Person10+point4[3]

    elif option == Person[10]:
        Person11=Person11+point4[3]

    elif option == Person[11]:
        Person12=Person12+point4[3]

    elif option == Person[12]:
        Person13=Person13+point4[3]

    elif option == Person[13]:
        Person14=Person14+point4[3]

    elif option == Person[14]:
        Person15=Person15+point4[3]

    elif option == Person[15]:
        Person16=Person16+point4[3]

    elif option == Person[16]:
        Person17=Person17+point4[3]

    elif option == Person[17]:
        Person18=Person18+point4[3]

    elif option == Person[18]:
        Person19=Person19+point4[3]

    else:
        Person20=Person20+point4[3]
        

    option=str(input("Input name of individual who came 5th "))
    if option == Person[0]:
        Person1=Person1+point4[4]

    elif option == Person[1]:
        Person2=Person2+point4[4]

    elif option == Person[2]:
        Person3=Person3+point4[4]
        
    elif option == Person[3]:
        Person4=Person4+point4[4]

    elif option == Person[4]:
        Person5=Person5+point4[4]

    elif option == Person[5]:
        Person6=Person6+point4[4]

    elif option == Person[6]:
        Person7=Person7+point4[4]

    elif option == Person[7]:
        Person8=Person8+point4[4]

    elif option == Person[8]:
        Person3=Person9+point4[4]

    elif option == Person[9]:
        Person10=Person10+point4[4]

    elif option == Person[10]:
        Person11=Person11+point4[4]

    elif option == Person[11]:
        Person12=Person12+point4[4]

    elif option == Person[12]:
        Person13=Person13+point4[4]

    elif option == Person[13]:
        Person14=Person14+point4[4]

    elif option == Person[14]:
        Person15=Person15+point4[4]

    elif option == Person[15]:
        Person16=Person16+point4[4]

    elif option == Person[16]:
        Person17=Person17+point4[4]

    elif option == Person[17]:
        Person18=Person18+point4[4]

    elif option == Person[18]:
        Person19=Person19+point4[4]

    else:
        Person20=Person20+point4[4]


    option=str(input("Input name of individual who came 6th "))
    if option == Person[0]:
        Person1=Person1+point4[5]

    elif option == Person[1]:
        Person2=Person2+point4[5]

    elif option == Person[2]:
        Person3=Person3+point4[5]
        
    elif option == Person[3]:
        Person4=Person4+point4[5]

    elif option == Person[4]:
        Person5=Person5+point4[5]

    elif option == Person[5]:
        Person6=Person6+point4[5]

    elif option == Person[6]:
        Person7=Person7+point4[5]

    elif option == Person[7]:
        Person8=Person8+point4[5]

    elif option == Person[8]:
        Person3=Person9+point4[5]

    elif option == Person[9]:
        Person10=Person10+point4[5]

    elif option == Person[10]:
        Person11=Person11+point4[5]

    elif option == Person[11]:
        Person12=Person12+point4[5]

    elif option == Person[12]:
        Person13=Person13+point4[5]

    elif option == Person[13]:
        Person14=Person14+point4[5]

    elif option == Person[14]:
        Person15=Person15+point4[5]

    elif option == Person[15]:
        Person16=Person16+point4[5]

    elif option == Person[16]:
        Person17=Person17+point4[5]

    elif option == Person[17]:
        Person18=Person18+point4[5]

    elif option == Person[18]:
        Person19=Person19+point4[5]

    else:
        Person20=Person20+point4[5]

    option=str(input("Input name of individual who came 1st for sports"))
    if option == Person[0]:
        Person1=Person1+point5[0]

    elif option == Person[1]:
        Person2=Person2+point5[0]

    elif option == Person[2]:
        Person3=Person3+point5[0]
        
    elif option == Person[3]:
        Person4=Person4+point5[0]

    elif option == Person[4]:
        Person5=Person5+point5[0]

    elif option == Person[5]:
        Person6=Person6+point5[0]

    elif option == Person[6]:
        Person7=Person7+point5[0]

    elif option == Person[7]:
        Person8=Person8+point5[0]

    elif option == Person[8]:
        Person3=Person9+point5[0]

    elif option == Person[9]:
        Person10=Person10+point5[0]

    elif option == Person[10]:
        Person11=Person11+point5[0]

    elif option == Person[11]:
        Person12=Person12+point5[0]

    elif option == Person[12]:
        Person13=Person13+point5[0]

    elif option == Person[13]:
        Person14=Person14+point5[0]

    elif option == Person[14]:
        Person15=Person15+point5[0]

    elif option == Person[15]:
        Person16=Person16+point5[0]

    elif option == Person[16]:
        Person17=Person17+point5[0]

    elif option == Person[17]:
        Person18=Person18+point5[0]

    elif option == Person[18]:
        Person19=Person19+point5[0]

    else:
        Person20=Person20+point5[0]

    option=str(input("Input name of individual who came 2nd "))
    if option == Person[0]:
        Person1=Person1+point5[1]

    elif option == Person[1]:
        Person2=Person2+point5[1]

    elif option == Person[2]:
        Person3=Person3+point5[1]
        
    elif option == Person[3]:
        Person4=Person4+point5[1]

    elif option == Person[4]:
        Person5=Person5+point5[1]

    elif option == Person[5]:
        Person6=Person6+point5[1]

    elif option == Person[6]:
        Person7=Person7+point5[1]

    elif option == Person[7]:
        Person8=Person8+point5[1]

    elif option == Person[8]:
        Person3=Person9+point5[1]

    elif option == Person[9]:
        Person10=Person10+point5[1]

    elif option == Person[10]:
        Person11=Person11+point5[1]

    elif option == Person[11]:
        Person12=Person12+point5[1]

    elif option == Person[12]:
        Person13=Person13+point5[1]

    elif option == Person[13]:
        Person14=Person14+point5[1]

    elif option == Person[14]:
        Person15=Person15+point5[1]

    elif option == Person[15]:
        Person16=Person16+point5[1]

    elif option == Person[16]:
        Person17=Person17+point5[1]

    elif option == Person[17]:
        Person18=Person18+point5[1]

    elif option == Person[18]:
        Person19=Person19+point5[1]

    else:
        Person20=Person20+point5[1]

    option=str(input("Input name of individual who came 3rd "))
    if option == Person[0]:
        Person1=Person1+point5[2]

    elif option == Person[1]:
        Person2=Person2+point5[2]

    elif option == Person[2]:
        Person3=Person3+point5[2]
        
    elif option == Person[3]:
        Person4=Person4+point5[2]

    elif option == Person[4]:
        Person5=Person5+point5[2]

    elif option == Person[5]:
        Person6=Person6+point5[2]

    elif option == Person[6]:
        Person7=Person7+point5[2]

    elif option == Person[7]:
        Person8=Person8+point5[2]

    elif option == Person[8]:
        Person3=Person9+point5[2]

    elif option == Person[9]:
        Person10=Person10+point5[2]

    elif option == Person[10]:
        Person11=Person11+point5[2]

    elif option == Person[11]:
        Person12=Person12+point5[2]

    elif option == Person[12]:
        Person13=Person13+point5[2]

    elif option == Person[13]:
        Person14=Person14+point5[2]

    elif option == Person[14]:
        Person15=Person15+point5[2]

    elif option == Person[15]:
        Person16=Person16+point5[2]

    elif option == Person[16]:
        Person17=Person17+point5[2]

    elif option == Person[17]:
        Person18=Person18+point5[2]

    elif option == Person[18]:
        Person19=Person19+point5[2]

    else:
        Person20=Person20+point5[2]
        
    option=str(input("Input name of individual who came 4th "))
    if option == Person[0]:
        Person1=Person1+point5[3]

    elif option == Person[1]:
        Person2=Person2+point5[3]

    elif option == Person[2]:
        Person3=Person3+point5[3]
        
    elif option == Person[3]:
        Person4=Person4+point5[3]

    elif option == Person[4]:
        Person5=Person5+point5[3]

    elif option == Person[5]:
        Person6=Person6+point5[3]

    elif option == Person[6]:
        Person7=Person7+point5[3]

    elif option == Person[7]:
        Person8=Person8+point5[3]

    elif option == Person[8]:
        Person3=Person9+point5[3]

    elif option == Person[9]:
        Person10=Person10+point5[3]

    elif option == Person[10]:
        Person11=Person11+point5[3]

    elif option == Person[11]:
        Person12=Person12+point5[3]

    elif option == Person[12]:
        Person13=Person13+point5[3]

    elif option == Person[13]:
        Person14=Person14+point5[3]

    elif option == Person[14]:
        Person15=Person15+point5[3]

    elif option == Person[15]:
        Person16=Person16+point5[3]

    elif option == Person[16]:
        Person17=Person17+point5[3]

    elif option == Person[17]:
        Person18=Person18+point5[3]

    elif option == Person[18]:
        Person19=Person19+point5[3]

    else:
        Person20=Person20+point5[3]
        

    option=str(input("Input name of individual who came 5th "))
    if option == Person[0]:
        Person1=Person1+point5[4]

    elif option == Person[1]:
        Person2=Person2+point5[4]

    elif option == Person[2]:
        Person3=Person3+point5[4]
        
    elif option == Person[3]:
        Person4=Person4+point5[4]

    elif option == Person[4]:
        Person5=Person5+point5[4]

    elif option == Person[5]:
        Person6=Person6+point5[4]

    elif option == Person[6]:
        Person7=Person7+point5[4]

    elif option == Person[7]:
        Person8=Person8+point5[4]

    elif option == Person[8]:
        Person3=Person9+point5[4]

    elif option == Person[9]:
        Person10=Person10+point5[4]

    elif option == Person[10]:
        Person11=Person11+point5[4]

    elif option == Person[11]:
        Person12=Person12+point5[4]

    elif option == Person[12]:
        Person13=Person13+point5[4]

    elif option == Person[13]:
        Person14=Person14+point5[4]

    elif option == Person[14]:
        Person15=Person15+point5[4]

    elif option == Person[15]:
        Person16=Person16+point5[4]

    elif option == Person[16]:
        Person17=Person17+point5[4]

    elif option == Person[17]:
        Person18=Person18+point5[4]

    elif option == Person[18]:
        Person19=Person19+point5[4]

    else:
        Person20=Person20+point5[4]


    option=str(input("Input name of individual who came 6th "))
    if option == Person[0]:
        Person1=Person1+point5[5]

    elif option == Person[1]:
        Person2=Person2+point5[5]

    elif option == Person[2]:
        Person3=Person3+point5[5]
        
    elif option == Person[3]:
        Person4=Person4+point5[5]

    elif option == Person[4]:
        Person5=Person5+point5[5]

    elif option == Person[5]:
        Person6=Person6+point5[5]

    elif option == Person[6]:
        Person7=Person7+point5[5]

    elif option == Person[7]:
        Person8=Person8+point5[5]

    elif option == Person[8]:
        Person3=Person9+point5[5]

    elif option == Person[9]:
        Person10=Person10+point5[5]

    elif option == Person[10]:
        Person11=Person11+point5[5]

    elif option == Person[11]:
        Person12=Person12+point5[5]

    elif option == Person[12]:
        Person13=Person13+point5[5]

    elif option == Person[13]:
        Person14=Person14+point5[5]

    elif option == Person[14]:
        Person15=Person15+point5[5]

    elif option == Person[15]:
        Person16=Person16+point5[5]

    elif option == Person[16]:
        Person17=Person17+point5[5]

    elif option == Person[17]:
        Person18=Person18+point5[5]

    elif option == Person[18]:
        Person19=Person19+point5[5]

    else:
        Person20=Person20+point5[5]

    print("1st Place for :" ,Person1)
    print("2nd Place for :" ,Person2)
    print("3rd Place for :" ,Person3)
    print("4th Place for :" ,Person4)
    print("5th Place for :" ,Person5)
    print("6th Place for :" ,Person6)
    print("7th Place for :" ,Person7)
    print("8th Place for :" ,Person8)
    print("9th Place for :" ,Person9)
    print("10th Place for :" ,Person10)
    print("11th Place for :" ,Person11)
    print("12th Place for :" ,Person12)
    print("13th Place for :" ,Person13)
    print("14th Place for :" ,Person14)
    print("15th Place for :" ,Person15)
    print("16th Place for :" ,Person16)
    print("17th Place for :" ,Person17)
    print("18th Place for :" ,Person18)
    print("19th Place for :" ,Person19)
    print("20th Place for :" ,Person20)
    ###################################################################################
    option=str(input("Would you like to restart  Yes or No?")).lower()
    if option == "yes":
        multipleforindividual()
    else:
        sys.exit()
    
    
    
        
    
        
        

        
                    
                



        



        
    
        



        
            
                   
def Multiple():
    global T1
    global T2
    global T3
    global T4
    while True:
        
        try:
            print("") 
            e1f1=int(input("Enter points given for first place - Art "))
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        if e1f1 <1 or e1f1>20:
            print(" the points should be between 1 and 20")
            continue
        else:
            print("The Score you set for Art is ",e1f1)
                            
        try:
            e1f2=int(input("Enter points given for second place - Art "))
        except ValueError:
            print("Please make sure you enter a number!")
            continue 
        if e1f2 <1 or e1f2>20:
            print(" the points should be between 1 and 20")
            continue
        else:
            print("The Score you set for Art is ",e1f2)
            
        try:
            e1f3=int(input("Enter points given for third place - Art "))
        except ValueError:
              print("Please make sure you enter a number!")
              continue 
        if e1f3 <1 or e1f3>20:
                print(" the points should be between 1 and 20")
                continue
        else:
            print("The Score you set for Art is ",e1f3)
          
        try:
            e1f4=int(input("Enter points given for fourth place - Art "))
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        if e1f4 <1 or e1f4>20:
                print(" the points should be between 1 and 20")
                continue
        else:
            print("The Score you set for Art is ",e1f4)
            break
         
        
          
    while True:
        try:
            print("")
            e2f1=int(input("Enter points given for first place - English "))
        except ValueError:
            print("Please make sure you enter a number!")
            continue
            if e2f1 <1 or e2f1>20:
                print(" the points should be between 1 and 20")
                continue
            else:
                print("The Score you set for English is ",e2f1)

        try:
            e2f2=int(input("Enter points given for second place - English "))
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        if e2f1 <1 or e2f2>20:
            print(" the points should be between 1 and 20")
            continue
        else:
            print("The Score you set for English is ",e2f2)

        try:
            e2f3=int(input("Enter points given for third place - English "))
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        if e2f3 <1 or e2f3>20:
            print(" the points should be between 1 and 20")
            continue
        else:
            print("The Score you set for Englsih is ",e2f3)
        try:
            e2f4=int(input("Enter points given for fourth place - English "))
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        if e2f4 <1 or e2f4>20:
            print(" the points should be between 1 and 20")
            continue
        else:
            print("The Score you set for Englsih is ",e2f4)
            break
        

    while True:
        
        
        try:
            print("")
            e3f1=int(input("Enter points given for first place - Science "))
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        if e3f1 <1 or e3f1>20:
            print(" the points should be between 1 and 20")
            continue
        else:
                print("The Score you set for Science is ",e3f1)

            
        try:
            e3f2=int(input("Enter points given for second place - Science" ))
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        if e3f2 <1 or e3f2>20:
            print(" the points should be between 1 and 20")
            continue
        else:
            print("The Score you set for Science is ",e3f2)
            
        try:
            e3f3=int(input("Enter points given for third place - Science "))
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        if e3f3 <1 or e3f3>20:
            print(" the points should be between 1 and 20")
            continue
        else:
            print("The Score you set for Science is ",e3f3)
            
        try:
            e3f4=int(input("Enter points given for fourth place - Science "))
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        if e3f4 <1 or e3f4>20:
            print(" the points should be between 1 and 20")
            continue
        else:
            print("The Score you set for Science is ",e3f4)
            break
                    
    while True:
        try:
            print("")
            e4f1=int(input("Enter points given for first place - Maths"))
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        if e4f1 <1 or e4f1>20:
            print(" the points should be between 1 and 20")
            continue
        else:
            print("The Score you set for Maths is ",e4f1)
            
        try:
            e4f2=int(input("Enter points given for second place - Maths" ))
        except ValueError:
            print("Please make sure you enter a number!")
            continue            
        if e4f2 <1 or e4f2>20:
            print(" the points should be between 1 and 20")
            continue
        else:
            print("The Score you set for Maths is ",e4f2)
        
        try:            
            e4f3=int(input("Enter points given for third place - Maths "))
        except ValueError:
                print("Please make sure you enter a number!")
                continue
        if e4f3 <1 or e4f3>20:
                print(" the points should be between 1 and 20")
                continue
        else:
            print("The Score you set for Maths is ",e4f3)
            
        try: 
            e4f4=int(input("Enter points given for fourth place - Maths "))
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        if e4f4 <1 or e4f4>20:
            print(" the points should be between 1 and 20")
            continue
        else:
            print("The Score you set for Maths is ",e4f4)
            break

    while True:
        try:
            print("")
            e5f1=int(input("Enter points given for first place - Sports "))
        except ValueError:
                print("Please make sure you enter a number!")
                continue
        if e5f1 <1 or e5f1>20:
                print(" the points should be between 1 and 20")
                continue
        else:
            print("The Score you set for Sports is ",e5f1)
                   
        try:
            e5f2=int(input("Enter points given for second place - Sports "))
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        if e5f2 <1 or e5f2>20:
            print(" the points should be between 1 and 20")
            continue
        else:
            print("The Score you set for Sports is ",e5f2)
       
        try:
            e5f3=int(input("Enter points given for third place - Sports "))
        except ValueError:
            print("Please make sure you enter a number!")
            continue
        if e5f3 <1 or e5f3>20:
            print(" the points should be between 1 and 20")
            continue
        else:
            print("The Score you set for Sport  is ",e5f3)
        
        try:
            e5f4=int(input("Enter points given for fourth place - Sports "))
        except ValueError:
                print("Please make sure you enter a number!")
                continue
        if e5f4 <1 or e5f4>20:
                print(" the points should be between 1 and 20")
                event1()
        else:
            print("The Score you set for Sport is ",e5f4)
            
    
       

        print("--------------------------------------------------------------------")
        print("")
        choice=str(input("Which team came first for art"))
        if choice == Team[0]:
            T1=T1+e1f1
        elif choice == Team[1]:
            T2=T2+e1f1
        elif choice == Team[2]:
            T3=T3+e1f1
        else:
            T4=T4+e1f1

        choice=str(input("Which team came second for art"))
        if choice == Team[0]:
            T1=T1+e1f2
        elif choice == Team[1]:
            T2=T2+e1f2
        elif choice == Team[2]:
            T3=T3+e1f2
        else:
            T4=T4+e1f2

        choice=str(input("Which team came third for art"))
        if choice == Team[0]:
            T1=T1+e1f3
        elif choice == Team[1]:
            T2=T2+e1f3
        elif choice == Team[2]:
            T3=T3+e1f3
        else:
            T4=T4+e1f3

        choice=str(input("Which team came fourth for art"))
        if choice == Team[0]:
            T1=T1+e1f4
            
        elif choice == Team[1]:
            T2=T2+e1f4
            
        elif choice == Team[2]:
            T3=T3+e1f4
            
        else:
            T4=T4+e1f4
            


        print("")
        choice=str(input("Which team came first for english"))
        if choice == Team[0]:
            T1=T1+e2f1
        elif choice == Team[1]:
            T2=T2+e2f1
        elif choice == Team[2]:
            T3=T3+e2f1
        else:
            T4=T4+e2f1

        choice=str(input("Which team came second for english"))
        if choice == Team[0]:
            T1=T1+e2f2
        elif choice == Team[1]:
            T2=T2+e2f2
        elif choice == Team[2]:
            T3=T3+e2f2
        else:
            T4=T4+e2f2

        choice=str(input("Which team came third for english"))
        if choice == Team[0]:
            T1=T1+e2f3
        elif choice == Team[1]:
            T2=T2+e2f3
        elif choice == Team[2]:
            T3=T3+e2f3
        else:
            T4=T4+e2f3

        choice=str(input("Which team came fourth for english"))
        if choice == Team[0]:
            T1=T1+e2f4
        elif choice == Team[1]:
            T2=T2+e2f4
        elif choice == Team[2]:
            T3=T3+e2f4
        else:
            T4=T4+e2f4

        print("")
        choice=str(input("Which team came first for science"))
        if choice == Team[0]:
            T1=T1+e3f1
        elif choice == Team[1]:
            T2=T2+e3f1
        elif choice == Team[2]:
            T3=T3+e3f1
        else:
            T4=T4+e3f1

        choice=str(input("Which team came second for science"))
        if choice == Team[0]:
            T1=T1+e3f2
        elif choice == Team[1]:
            T2=T2+e3f2
        elif choice == Team[2]:
            T3=T3+e3f2
        else:
            T4=T4+e3f2

        choice=str(input("Which team came third for science"))
        if choice == Team[0]:
            T1=T1+e3f3
        elif choice == Team[1]:
            T2=T2+e3f3
        elif choice == Team[2]:
            T3=T3+e3f3
        else:
            T4=T4+e3f3

        choice=str(input("Which team came fourth for science"))
        if choice == Team[0]:
            T1=T1+e3f4
        elif choice == Team[1]:
            T2=T2+e3f4
        elif choice == Team[2]:
            T3=T3+e3f4
        else:
            T4=T4+e3f4

        print("")
        choice=str(input("Which team came first for maths"))
        if choice == Team[0]:
            T1=T1+e4f1
        elif choice == Team[1]:
            T2=T2+e4f1
        elif choice == Team[2]:
            T3=T3+e4f1
        else:
            T4=T4+e4f1

        choice=str(input("Which team came second for maths"))
        if choice == Team[0]:
            T1=T1+e4f2
        elif choice == Team[1]:
            T2=T2+e4f2
        elif choice == Team[2]:
            T3=T3+e4f2
        else:
            T4=T4+e4f2

        choice=str(input("Which team came third for maths"))
        if choice == Team[0]:
            T1=T1+e4f3
        elif choice == Team[1]:
            T2=T2+e4f3
        elif choice == Team[2]:
            T3=T3+e4f3
        else:
            T4=T4+e4f3

        choice=str(input("Which team came fourth for maths"))
        if choice == Team[0]:
            T1=T1+e4f4
        elif choice == Team[1]:
            T2=T2+e4f4
        elif choice == Team[2]:
            T3=T3+e4f4
        else:
            T4=T4+e4f4

        print("")
        choice=str(input("Which team came first for sport"))
        if choice == Team[0]:
            T1=T1+e5f1
        elif choice == Team[1]:
            T2=T2+e5f1
        elif choice == Team[2]:
            T3=T3+e5f1
        else:
            T4=T4+e5f1

        choice=str(input("Which team came second for sport"))
        if choice == Team[0]:
            T1=T1+e5f2
        elif choice == Team[1]:
            T2=T2+e5f2
        elif choice == Team[2]:
            T3=T3+e5f2
        else:
            T4=T4+e5f2

        choice=str(input("Which team came third for sport"))
        if choice == Team[0]:
            T1=T1+e5f3
        elif choice == Team[1]:
            T2=T2+e5f3
        elif choice == Team[2]:
            T3=T3+e5f3
        else:
            T4=T4+e5f3

        choice=str(input("Which team came fourth for sport"))
        if choice == Team[0]:
            T1=T1+e5f4
        elif choice == Team[1]:
            T2=T2+e5f4
        elif choice == Team[2]:
            T3=T3+e5f4
        else:
            T4=T4+e5f4

        print("--------------------------------------------------------------------")
        print("")
        print("Total points for team 1",T1)
        print("Total points for team 2",T2)
        print("Total points team 3",T3)
        print("Total points for team 4",T4)
        option=str(input("Would you like to Restart  Yes or No?")).lower()
        if option == "yes":
            Multiple()
        else:
            sys.exit()
           
                
####################################################################################
def singleandmultiple():
    global T1
    global T2
    global T3
    global T4
    print("please choose if you want to do single or mulitple ")
    choice=str(input("Enter single or multiple")).lower()
    if choice == "single":
        print("Which event would you like to select?")
        choice=int(input(" 1 - Art 2 - English 3 - Science 4 - Maths 5 - Sport "))
        if choice == 1:
           while True:               
                try:
                    print("") 
                    e1f1=int(input("Enter points given for first place - Art "))
                except ValueError:
                    print("Please make sure you enter a number!")
                    continue
                if e1f1 <1 or e1f1>20:
                    print(" the points should be between 1 and 20")
                    continue
                else:
                    print("The Score you set for Art is ",e1f1)
                                    
                try:
                    e1f2=int(input("Enter points given for second place - Art "))
                except ValueError:
                    print("Please make sure you enter a number!")
                    continue 
                if e1f2 <1 or e1f2>20:
                    print(" the points should be between 1 and 20")
                    continue
                else:
                    print("The Score you set for Art is ",e1f2)
                    
                try:
                    e1f3=int(input("Enter points given for third place - Art "))
                except ValueError:
                      print("Please make sure you enter a number!")
                      continue 
                if e1f3 <1 or e1f3>20:
                        print(" the points should be between 1 and 20")
                        continue
                else:
                    print("The Score you set for Art is ",e1f3)
                  
                try:
                    e1f4=int(input("Enter points given for fourth place - Art "))
                except ValueError:
                    print("Please make sure you enter a number!")
                    continue
                if e1f4 <1 or e1f4>20:
                        print(" the points should be between 1 and 20")
                        continue
                else:
                    print("The Score you set for Art is ",e1f4)
                
                

                    print("--------------------------------------------------------------------")
                    print("")
                    choice=str(input("Which team came first for art"))
                    if choice == Team[0]:
                        T1=T1+e1f1
                    elif choice == Team[1]:
                        T2=T2+e1f1
                    elif choice == Team[2]:
                        T3=T3+e1f1
                    else:
                        T4=T4+e1f1

                    choice=str(input("Which team came second for art"))
                    if choice == Team[0]:
                        T1=T1+e1f2
                    elif choice == Team[1]:
                        T2=T2+e1f2
                    elif choice == Team[2]:
                        T3=T3+e1f2
                    else:
                        T4=T4+e1f2

                    choice=str(input("Which team came third for art"))
                    if choice == Team[0]:
                        T1=T1+e1f3
                    elif choice == Team[1]:
                        T2=T2+e1f3
                    elif choice == Team[2]:
                        T3=T3+e1f3
                    else:
                        T4=T4+e1f3

                    choice=str(input("Which team came fourth for art"))
                    if choice == Team[0]:
                        T1=T1+e1f4
                        
                    elif choice == Team[1]:
                        T2=T2+e1f4
                        
                    elif choice == Team[2]:
                        T3=T3+e1f4
                        
                    else:
                        T4=T4+e1f4                  
            
                    print("--------------------------------------------------------------------")
                    print("")
                    print("Total points for team 1 ",T1)
                    print("Total points for team 2 ",T2)
                    print("Total points team 3 ",T3)
                    print("Total points for team 4 ",T4)
                    option=str(input("Would you like choose another event Yes or No?")).lower()
                    if option == "yes":
                        singleandmultiple()
                    else :
                        break
      
                
                
######################################################################Teams Single English #######################################################
        elif choice == 2:
        
            while True:
                
                try:
                    print("")
                    e2f1=int(input("Enter points given for first place - English "))
                except ValueError:
                    print("Please make sure you enter a number!")
                    continue
                    if e2f1 <1 or e2f1>20:
                        print(" the points should be between 1 and 20")
                        continue
                    else:
                        print("The Score you set for English is ",e2f1)

                try:
                    e2f2=int(input("Enter points given for second place - English "))
                except ValueError:
                    print("Please make sure you enter a number!")
                    continue
                if e2f1 <1 or e2f2>20:
                    print(" the points should be between 1 and 20")
                    continue
                else:
                    print("The Score you set for English is ",e2f2)

                try:
                    e2f3=int(input("Enter points given for third place - English "))
                except ValueError:
                    print("Please make sure you enter a number!")
                    continue
                if e2f3 <1 or e2f3>20:
                    print(" the points should be between 1 and 20")
                    continue
                else:
                    print("The Score you set for Englsih is ",e2f3)
                try:
                    e2f4=int(input("Enter points given for fourth place - English "))
                except ValueError:
                    print("Please make sure you enter a number!")
                    continue
                if e2f4 <1 or e2f4>20:
                    print(" the points should be between 1 and 20")
                    continue
                else:
                    print("The Score you set for Englsih is ",e2f4)
                    
                
                    print("--------------------------------------------------------------------")
                    print("")
                    choice=str(input("Which team came first for english"))
                    if choice == Team[0]:
                        T1=T1+e2f1
                    elif choice == Team[1]:
                        T2=T2+e2f1
                    elif choice == Team[2]:
                        T3=T3+e2f1
                    else:
                        T4=T4+e2f1

                    choice=str(input("Which team came second for english"))
                    if choice == Team[0]:
                        T1=T1+e2f2
                    elif choice == Team[1]:
                        T2=T2+e2f2
                    elif choice == Team[2]:
                        T3=T3+e2f2
                    else:
                        T4=T4+e2f2

                    choice=str(input("Which team came third for english"))
                    if choice == Team[0]:
                        T1=T1+e2f3
                    elif choice == Team[1]:
                        T2=T2+e2f3
                    elif choice == Team[2]:
                        T3=T3+e2f3
                    else:
                        T4=T4+e2f3

                    choice=str(input("Which team came fourth for english"))
                    if choice == Team[0]:
                        T1=T1+e2f4
                    elif choice == Team[1]:
                        T2=T2+e2f4
                    elif choice == Team[2]:
                        T3=T3+e2f4
                    else:
                        T4=T4+e2f4

                    print("--------------------------------------------------------------------")
                    print("")
                    print("Total points for team 1 ",T1)
                    print("Total points for team 2 ",T2)
                    print("Total points team 3 ",T3)
                    print("Total points for team 4 ",T4)
                    option=str(input("Would you like choose another event Yes or No?")).lower()
                    if option == "yes":
                        singleandmultiple()
                    else :
                        break
        
################################################################################Team Single Science ###########################################################        
        elif choice == 3:
            while True:
                try:
                    print("")
                    e3f1=int(input("Enter points given for first place - Science "))
                except ValueError:
                    print("Please make sure you enter a number!")
                    continue
                if e3f1 <1 or e3f1>20:
                    print(" the points should be between 1 and 20")
                    continue
                else:
                        print("The Score you set for Science is ",e3f1)

                    
                try:
                    e3f2=int(input("Enter points given for second place - Science" ))
                except ValueError:
                    print("Please make sure you enter a number!")
                    continue
                if e3f2 <1 or e3f2>20:
                    print(" the points should be between 1 and 20")
                    continue
                else:
                    print("The Score you set for Science is ",e3f2)
                    
                try:
                    e3f3=int(input("Enter points given for third place - Science "))
                except ValueError:
                    print("Please make sure you enter a number!")
                    continue
                if e3f3 <1 or e3f3>20:
                    print(" the points should be between 1 and 20")
                    continue
                else:
                    print("The Score you set for Science is ",e3f3)
                    
                try:
                    e3f4=int(input("Enter points given for fourth place - Science "))
                except ValueError:
                    print("Please make sure you enter a number!")
                    continue
                if e3f4 <1 or e3f4>20:
                    print(" the points should be between 1 and 20")
                    continue
                else:
                    print("The Score you set for Science is ",e3f4)
                
        
                    print("")
                    choice=str(input("Which team came first for science"))
                    if choice == Team[0]:
                        T1=T1+e3f1
                    elif choice == Team[1]:
                        T2=T2+e3f1
                    elif choice == Team[2]:
                        T3=T3+e3f1
                    else:
                        T4=T4+e3f1

                    choice=str(input("Which team came second for science"))
                    if choice == Team[0]:
                        T1=T1+e3f2
                    elif choice == Team[1]:
                        T2=T2+e3f2
                    elif choice == Team[2]:
                        T3=T3+e3f2
                    else:
                        T4=T4+e3f2

                    choice=str(input("Which team came third for science"))
                    if choice == Team[0]:
                        T1=T1+e3f3
                    elif choice == Team[1]:
                        T2=T2+e3f3
                    elif choice == Team[2]:
                        T3=T3+e3f3
                    else:
                        T4=T4+e3f3

                    choice=str(input("Which team came fourth for science"))
                    if choice == Team[0]:
                        T1=T1+e3f4
                    elif choice == Team[1]:
                        T2=T2+e3f4
                    elif choice == Team[2]:
                        T3=T3+e3f4
                    else:
                        T4=T4+e3f4

                    print("--------------------------------------------------------------------")
                    print("")
                    print("Total points for team 1 ",T1)
                    print("Total points for team 2 ",T2)
                    print("Total points for team 3 ",T3)
                    print("Total points for team 4 ",T4)
                    option=str(input("Would you like choose another event Yes or No?")).lower()
                    if option == "yes":
                        singleandmultiple()
                    else :
                        break
###################################################################################Team Single Maths #################################################
        elif choice == 4:
                while True:
                    try:
                        print("")
                        e4f1=int(input("Enter points given for first place - Maths"))
                    except ValueError:
                        print("Please make sure you enter a number!")
                        continue
                    if e4f1 <1 or e4f1>20:
                        print(" the points should be between 1 and 20")
                        continue
                    else:
                        print("The Score you set for Maths is ",e4f1)
                        
                    try:
                        e4f2=int(input("Enter points given for second place - Maths" ))
                    except ValueError:
                        print("Please make sure you enter a number!")
                        continue            
                    if e4f2 <1 or e4f2>20:
                        print(" the points should be between 1 and 20")
                        continue
                    else:
                        print("The Score you set for Maths is ",e4f2)
                    
                    try:            
                        e4f3=int(input("Enter points given for third place - Maths "))
                    except ValueError:
                            print("Please make sure you enter a number!")
                            continue
                    if e4f3 <1 or e4f3>20:
                            print(" the points should be between 1 and 20")
                            continue
                    else:
                        print("The Score you set for Maths is ",e4f3)
                        
                    try: 
                        e4f4=int(input("Enter points given for fourth place - Maths "))
                    except ValueError:
                        print("Please make sure you enter a number!")
                        continue
                    if e4f4 <1 or e4f4>20:
                        print(" the points should be between 1 and 20")
                        continue
                    else:
                        print("The Score you set for Maths is ",e4f4)
                        

                        print("")
                        choice=str(input("Which team came first for maths"))
                        if choice == Team[0]:
                            T1=T1+e4f1
                        elif choice == Team[1]:
                            T2=T2+e4f1
                        elif choice == Team[2]:
                            T3=T3+e4f1
                        else:
                            T4=T4+e4f1

                        choice=str(input("Which team came second for maths"))
                        if choice == Team[0]:
                            T1=T1+e4f2
                        elif choice == Team[1]:
                            T2=T2+e4f2
                        elif choice == Team[2]:
                            T3=T3+e4f2
                        else:
                            T4=T4+e4f2

                        choice=str(input("Which team came third for maths"))
                        if choice == Team[0]:
                            T1=T1+e4f3
                        elif choice == Team[1]:
                            T2=T2+e4f3
                        elif choice == Team[2]:
                            T3=T3+e4f3
                        else:
                            T4=T4+e4f3

                        choice=str(input("Which team came fourth for maths"))
                        if choice == Team[0]:
                            T1=T1+e4f4
                        elif choice == Team[1]:
                            T2=T2+e4f4
                        elif choice == Team[2]:
                            T3=T3+e4f4
                        else:
                            T4=T4+e4f4
                        print("--------------------------------------------------------------------")
                        print("")
                        print("Total points for team 1",T1)
                        print("Total points for team 2 ",T2)
                        print("Total points team 3 ",T3)
                        print("Total points for team 4 ",T4)
                        option=str(input("Would you like choose another event Yes or No?")).lower()
                        if option == "yes":
                            singleandmultiple()
                        else :
                            break
#########################################################################Team sports single################################################################                    
        elif choice  == 5:
                while True:
                    try:
                        print("")
                        e5f1=int(input("Enter points given for first place - Sports "))
                    except ValueError:
                            print("Please make sure you enter a number!")
                            continue
                    if e5f1 <1 or e5f1>20:
                            print(" the points should be between 1 and 20")
                            continue
                    else:
                        print("The Score you set for Sports is ",e5f1)
                               
                    try:
                        e5f2=int(input("Enter points given for second place - Sports "))
                    except ValueError:
                        print("Please make sure you enter a number!")
                        continue
                    if e5f2 <1 or e5f2>20:
                        print(" the points should be between 1 and 20")
                        continue
                    else:
                        print("The Score you set for Sports is ",e5f2)
                   
                    try:
                        e5f3=int(input("Enter points given for third place - Sports "))
                    except ValueError:
                        print("Please make sure you enter a number!")
                        continue
                    if e5f3 <1 or e5f3>20:
                        print(" the points should be between 1 and 20")
                        continue
                    else:
                        print("The Score you set for Sport  is ",e5f3)
                    
                    try:
                        e5f4=int(input("Enter points given for fourth place - Sports "))
                    except ValueError:
                            print("Please make sure you enter a number!")
                            continue
                    if e5f4 <1 or e5f4>20:
                            print(" the points should be between 1 and 20")
                            event1()
                    else:
                        print("The Score you set for Sport is ",e5f4)
                        

                        print("")
                        choice=str(input("Which team came first for sport"))
                        if choice == Team[0]:
                            T1=T1+e5f1
                        elif choice == Team[1]:
                            T2=T2+e5f1
                        elif choice == Team[2]:
                            T3=T3+e5f1
                        else:
                            T4=T4+e5f1

                        choice=str(input("Which team came second for sport"))
                        if choice == Team[0]:
                            T1=T1+e5f2
                        elif choice == Team[1]:
                            T2=T2+e5f2
                        elif choice == Team[2]:
                            T3=T3+e5f2
                        else:
                            T4=T4+e5f2

                        choice=str(input("Which team came third for sport"))
                        if choice == Team[0]:
                            T1=T1+e5f3
                        elif choice == Team[1]:
                            T2=T2+e5f3
                        elif choice == Team[2]:
                            T3=T3+e5f3
                        else:
                            T4=T4+e5f3

                        choice=str(input("Which team came fourth for sport"))
                        if choice == Team[0]:
                            T1=T1+e5f4
                        elif choice == Team[1]:
                            T2=T2+e5f4
                        elif choice == Team[2]:
                            T3=T3+e5f4
                        else:
                            T4=T4+e5f4

                        print("--------------------------------------------------------------------")
                        print("")
                        print("Total points for team 1 ",T1)
                        print("Total points for team 2 ",T2)
                        print("Total points team 3 ",T3)
                        print("Total points for team 4 ",T4)
                        option=str(input("Would you like choose another event Yes or No?")).lower()
                        if option == "yes":
                            singleandmultiple()
                        else :
                            break
                        
                
                
            
                            
            
        
                                                                                                                              
            
    elif choice == "multiple":
        Multiple()

    else:
        singleandmultiple()
        
        
while True:        
    choice=str(input("Teams or individual? ")).lower()
    if choice == "teams":
        
        print("Please Enter the name of 4 Teams!")
        
        for i in range(teams):
            team_names=str(input("Please enter the name for this team "))
            Team.append(team_names)

        print(Team)
        print("--------------------------------------------------------------------")
        while True:
            try:
                member=int(input("How many members should be in each team? "))
                break
            except ValueError:
                print("Please make sure you enter a number!")
                continue

        for i in range(member):
            print("")

            name_member1=str(input("Please enter a member's name for Team 1! "))
            team_names1.append(name_member1)
            print(Team[0],team_names1)

        for i in range(member):
            print("")
            name_member2=str(input("Please enter a member's name for Team 2! "))
            team_names2.append(name_member2)
            print(Team[1],team_names2)

        for i in range(member):
            print("")
            name_member3=str(input("Please enter a member's name for Team 3! "))
            team_names3.append(name_member3)
            print(Team[2],team_names3)

        for i in range(member):
            print("")
            name_member4=str(input("Please enter a member's name for Team 4! "))
            team_names4.append(name_member4)
            print(Team[3],team_names4)
        singleandmultiple()
            

        print("--------------------------------------------------------------------")

    elif choice == "individual":
        print("--------------------------------------------------------------------")
        print("Please enter names of 20 Individuals!")

            
        for i in range (20):
            choice=str(input("Please enter name of individual"))
            Person.append(choice)
        print("")
        print(Person)
        
        print("--------------------------------------------------------------------")
        while True:   
                print("please choose if you want to do single or mulitple ")
                choice=str(input("Enter single or multiple")).lower()
                if choice == "single":
                    while True:
                        option=str(input("enter art, english, science, maths and sports"))
                        if option == "art":
                            singleart()
                            break
                        elif option == "english":
                            singleenglish()
                            break

                        elif option == "science":
                            singlescience()
                            break

                        elif option == "maths":
                            singlemaths()
                            break

                        elif option == "sports":
                            singlesports()
                            break

                        else:
                            print("error")
                            continue
                        
                    
                
                elif choice == "multiple":
                    multipleforindividual()

                else:
                    print("Please make sure to enter one of the options!")
                    continue

    else:
        print("Please make sure to enter one of the options!")
        continue
    

