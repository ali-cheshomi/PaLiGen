import os
import random
from time import sleep 



file = open("./pgex.txt","w")

def s_Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def s_Restart():
    print("ERROR RESTART !!!")
    sleep(1)
    os.system('python.exe PaLiGen.py' if os.name == 'nt' else 'python3 PaLiGen.py')

s_Clear()
banner="""

########     ###    ##       ####  ######   ######## ##    ## 
##     ##   ## ##   ##        ##  ##    ##  ##       ###   ## 
##     ##  ##   ##  ##        ##  ##        ##       ####  ## 
########  ##     ## ##        ##  ##   #### ######   ## ## ## 
##        ######### ##        ##  ##    ##  ##       ##  #### 
##        ##     ## ##        ##  ##    ##  ##       ##   ### 
##        ##     ## ######## ####  ######   ######## ##    ## 
                                             
pssword list generator
by MR_AC

"""
print(banner)
print("**[Pass list Generaitor]**\n")
wordlist_1=['1','2','3','4','5','6','7','8','9','0']
wordlist_2=[
    '+','-','/',
    '*',' ','.',
    '\\',';',':',
    '\'','\"','|',
    '`','~','!',
    '?','@','#',
    '$','%','^',
    '&','*','(',
    ')','{','}',
    '[',']',',',
    '<','>','=',
    '-','_',
    ]
wordlist_3=[
    'a','b','c',
    'd','e','f',
    'g','h','i',
    'j','k','l',
    'm','n','o',
    'p','q','r',
    's','t','u',
    'w','x','y',
    'z','v'
    ]
wordlist_4=[
    'A','B','C',
    'D','E','F',
    'G','H','I',
    'J','K','L',
    'M','N','O',
    'P','Q','R',
    'S','T','U',
    'V','W','X',
    'Y','Z'
    ]
wordlist_5=[]
wordlist_6=[]
wordlist_7=[]
wordlist_8=[]
wordlist_9=[]
wordlist_10=[]
wordlist_10=[]
wordlist_11=[]
wordlist_12=[]
wordlist_13=[]
wordlist_14=[]



########################################$$$$$$$$$$$$$$$$$$$$
for i in range(len(wordlist_1)):
    wordlist_5.append(wordlist_1[i])
for i in range(len(wordlist_2)):
    wordlist_5.append(wordlist_2[i])
random.shuffle(wordlist_5)
########################################SSSSSSSSSSSSSSSSSSSSS

########################################$$$$$$$$$$$$$$$$$$$$
for i in range(len(wordlist_1)):
    wordlist_6.append(wordlist_1[i])
for i in range(len(wordlist_3)):
    wordlist_6.append(wordlist_3[i])
random.shuffle(wordlist_6)
########################################SSSSSSSSSSSSSSSSSSSSS

########################################$$$$$$$$$$$$$$$$$$$$
for i in range(len(wordlist_1)):
    wordlist_7.append(wordlist_1[i])
for i in range(len(wordlist_4)):
    wordlist_7.append(wordlist_4[i])
random.shuffle(wordlist_7)
########################################SSSSSSSSSSSSSSSSSSSSS

########################################$$$$$$$$$$$$$$$$$$$$
for i in range(len(wordlist_3)):
    wordlist_8.append(wordlist_3[i])
for i in range(len(wordlist_4)):
    wordlist_8.append(wordlist_4[i])
random.shuffle(wordlist_8)
########################################SSSSSSSSSSSSSSSSSSSSS

########################################$$$$$$$$$$$$$$$$$$$$
for i in range(len(wordlist_3)):
    wordlist_9.append(wordlist_3[i])
for i in range(len(wordlist_2)):
    wordlist_9.append(wordlist_2[i])
random.shuffle(wordlist_9)
########################################SSSSSSSSSSSSSSSSSSSSS

########################################$$$$$$$$$$$$$$$$$$$$
for i in range(len(wordlist_4)):
    wordlist_10.append(wordlist_4[i])
for i in range(len(wordlist_2)):
    wordlist_10.append(wordlist_2[i])
random.shuffle(wordlist_10)
########################################$$$$$$$$$$$$$$$$$$$$

########################################$$$$$$$$$$$$$$$$$$$$
for i in range(len(wordlist_8)):
    wordlist_11.append(wordlist_8[i])
for i in range(len(wordlist_2)):
    wordlist_11.append(wordlist_2[i])
random.shuffle(wordlist_11)
########################################SSSSSSSSSSSSSSSSSSSSS
########################################$$$$$$$$$$$$$$$$$$$$
for i in range(len(wordlist_6)):
    wordlist_12.append(wordlist_6[i])
for i in range(len(wordlist_2)):
    wordlist_12.append(wordlist_2[i])
random.shuffle(wordlist_12)
########################################SSSSSSSSSSSSSSSSSSSSS

########################################$$$$$$$$$$$$$$$$$$$$
for i in range(len(wordlist_7)):
    wordlist_13.append(wordlist_7[i])
for i in range(len(wordlist_2)):
    wordlist_13.append(wordlist_2[i])
random.shuffle(wordlist_13)
########################################SSSSSSSSSSSSSSSSSSSSS

########################################$$$$$$$$$$$$$$$$$$$$
for i in range(len(wordlist_8)):
    wordlist_14.append(wordlist_8[i])
for i in range(len(wordlist_5)):
    wordlist_14.append(wordlist_5[i])
random.shuffle(wordlist_14)
########################################SSSSSSSSSSSSSSSSSSSSS


# print(wordlist_14)

####################
pass_len =1
count =1
mode=0
password =''
passwords =[]

# print(wordlist_1)
try:
    count = int(input("how many password do you want : "))
except:
    s_Restart()
try:
    pass_len = int(input("how long password lenght : "))
except:
    s_Restart()
try:
    mode = int(input("""\n
** select what charector you want to be in password** \n
Mode (1) : [1,2,3,...,9] \n
Mode (2) : [*,-,/,...,@] \n
Mode (3) : [a,b,c,...,z] \n
Mode (4) : [A,B,C,...,Z] \n


Mode (5) : [1,2,3,...,9] & [*,-,/,...,@] \n
Mode (6) : [1,2,3,...,9] & [a,b,c,...,z] \n
Mode (7) : [1,2,3,...,9] & [A,B,C,...,Z] \n
Mode (8) : [a,b,c,...,z] & [A,B,C,...,Z] \n
Mode (9) : [a,b,c,...,z] & [*,-,/,...,@] \n
Mode (10) : [A,B,C,...,Z] & [*,-,/,...,@] \n



Mode (11) : [a,b,c,...,z] & [A,B,C,...,Z] & [*,-,/,...,@] \n
Mode (12) : [1,2,3,...,9] & [a,b,c,...,z] & [*,-,/,...,@] \n
Mode (13) : [1,2,3,...,9] & [A,B,C,...,Z] & [*,-,/,...,@] \n
mode (14) : [1,2,3,...,9] & [A,B,C,...,Z] & [a,b,c,...,z] & [*,-,/,...,@] \n

(enter number) :

"""))
except:
    s_Restart()

def mode1_Pass_Gen():
    pword =''
    pwords =[]
    # print(f"def is running len and co : {len},{1}")
    for i in range(3):
        for j in range(5):
           rand_num= random.randrange(0,10)
           pword += wordlist_1[rand_num] 
        pwords.append(pword)
        pword=''

    # print(f"passwords : \"{pwords}\"")
##################################################

def word_selector(wlist):
    pword = ''
    rand_num= random.randrange(0,len(wlist))
    pword = wlist[rand_num]
    return pword 
    # print(f"password : {pword}")



s=word_selector(wordlist_14)
# print(f" ss = {s}  and t = {type(s)}")


def p_Gen(wlist , pc , pln):
    pss=''
    pwords =[]
    for i in range(pc):
        for j in range(pln):
            pwords.append(word_selector(wlist))
        #print(f"passwords : \"{pss.join(pwords)}\"")
        file.writelines(pwords)
        file.writelines("\n")

        pwords=[]





print(f"mode = {mode}")

############################
if mode == 1 :
    # mode1_Pass_Gen()
    p_Gen(wordlist_1, count, pass_len)

elif mode == 2 :
    p_Gen(wordlist_2, count, pass_len)

elif mode == 3 :
    p_Gen(wordlist_3, count, pass_len)

elif mode == 4 :
    p_Gen(wordlist_4, count, pass_len)

elif mode == 5 :
    p_Gen(wordlist_5, count, pass_len)

elif mode == 6 :
    p_Gen(wordlist_6, count, pass_len)

elif mode == 7 :
    p_Gen(wordlist_7, count, pass_len)

elif mode == 8 :
    p_Gen(wordlist_8, count, pass_len)

elif mode == 9 :
    p_Gen(wordlist_9, count, pass_len)

elif mode == 10 :
    p_Gen(wordlist_10, count, pass_len)

elif mode == 11 :
    p_Gen(wordlist_11, count, pass_len)

elif mode == 12 :
    p_Gen(wordlist_12, count, pass_len)

elif mode == 131 :
    p_Gen(wordlist_13, count, pass_len)

elif mode == 14 :
    p_Gen(wordlist_14, count, pass_len)

print(f"********************************************")

file.close()




    