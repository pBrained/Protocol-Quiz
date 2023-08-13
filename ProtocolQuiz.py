import pandas as pd
import random
#You need to run Python3 and use the pip3 moudule to download the random generatr module and pandas module"
#search google how to run Py File, pandas module, random generator

#A Quick Poem
#if necessary you should only need to learn something once
#if necessary keep learning untill ingraned, irony - Preston C

#This uses pandas (pd) read comma seperated value sheet module
prototable = pd.read_csv('Messer.csv') 
ammount = input("Welcome, how many questions do you want?\n")
score = 0

#Then we itterate over the desired ammount of questions
for x in range(int(ammount)):

#Generating Problems and Answers
    qnum = random.randint(0,25)
    print('Description & Port')
    print('Ports:', prototable.iloc[qnum][1])
    print('Question:', prototable.iloc[qnum][3])
    answer = prototable.iloc[qnum]['Protocol']

#And we check For correctness and update score
    ans = input()
    if ans == answer:
        print(prototable.iloc[qnum]['Name'],", Nice +1")
        score += 1
    else:
        print("\nIt's", answer, '\n')
        continue

#Normalizing score for user
ratio = int(score) / int(ammount)
ratio = ratio * 100
if ratio % 1 == 0:
    print("you got %d percent" %  ratio)
else:
    print('You got %.2f percent' % ratio)

#Debugging Tests (Start here if lost)
#print(prototable['Port'])
#print(prototable[['Name','Port','Description']])
#print(prototable[0:10][['Name']])
#print(prototable.loc[['FTP']])


