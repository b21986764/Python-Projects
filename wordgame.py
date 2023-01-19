import sys

import time

liste=[]
my_dic={}
my_dic2={}
def form2(guessed):
   guessed=guessed.replace("I","ı")

   guessed=guessed.replace("İ","i")

   guessed=guessed.lower()
  # print(guessed)
   return(guessed)
def open1():
    f = open("correct_words.txt", "r",encoding="utf-8-sig").readlines()
    y=len(f)  
    j=0
    while j<y:
        f1=f[j].split(":") 
        liste.append(f1[0])      
        liste2=f1[1].split("\n")
       # print(liste2)
        liste3=liste2[0].split(",")
        global my_dic
        my_dic[f1[0]]=liste3
        j+=1
    
open1()

def open2():
    f2 = open("letter_values.txt", "r",encoding="utf-8-sig").readlines()
    z=len(f2)
    a=0
    global liste12

    while a<z:
        
        f3=f2[a].split(":")
      #  print(f3)
        
        
        liste9=f3[1].split("\n")
        liste10=liste9[0].split(",")
        global my_dic2
        my_dic2[f3[0]]=liste10
        global liste11
        liste11=list(my_dic2.keys())
        liste12=list(my_dic2.values())
       # print(liste9)
        
        a+=1
    for i in range(len(liste11)):
        liste11[i]=form2(liste11[i])
open2()
liste13=list(my_dic.values())
for i in range(len(liste13)):
    for j in range(len(liste13[i])):
        liste13[i][j]=form2(liste13[i][j])
y="I"
liste14=[]
liste15=[]



#print("liste13  {}".format(liste13))

def scoring(crrct):
    global point
    global liste12
    global guessed
    point=0
    p=0

    if len(crrct)!=0:
     for i in range(len(crrct)):
      for j in range(len(crrct[i])):   
          
            u = crrct[i][j]
           
            p+=int(liste12[liste11.index(u)][0])
      point+=p*len(crrct[i])
      p=0
    return point
#print("liste 12 {}".format(liste12))
#print("liste 11 {}".format(liste11))
def sure(baslangic):
        global tm
        tm=(30-(int(time.time()-baslangic)))
        
def game():

   for i in range(len(liste)):
    baslangic =time.time()
    crrct=[]
    t=True
    print("shuffled letters are {} Please guess words for the letters with minimum three letters".format(liste[i]))
    while t:
        
        guessed=input("Guess :")
        guessed=form2(guessed)
      
        guessed=guessed.lower()
    
        sure(baslangic)
        for j in range(len(liste13[i])):
            if crrct.count(guessed)>0:
                print("This word is guessed before")
                break
            elif liste13[i].count(guessed)==1:
              if guessed!="":
                crrct.append(guessed)           
                break   
            if guessed not in liste13[i]:
                print("This word is not valid")
                break
        
        if tm>=0:        
               print("You have {} time".format(tm))
        else:
               print("You have 0 time")
        if tm<=0:
            result=scoring(crrct)
            #result=0
            if len(crrct)!=0:
             print("Score for {} is {} and guessed words are: ".format(liste[i],result), end="")
            else:
              print("Score for 0 is and guessed words are: ", end="")
            print(*crrct, sep = "-") 
            t=False
           
    
        
  

    


game()
    
    
    
    
    
    
        
    
        
    
    
#print(my_dic)