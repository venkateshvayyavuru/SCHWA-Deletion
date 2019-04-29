import numpy as np
import sys
import re
from collections import OrderedDict
from collections import defaultdict
dict_lines=open("dictionary.txt",'r',encoding='utf-8')
dictionary={}
for line in dict_lines:
	dictionary[line.rstrip().split(" ")[0]]=line.rstrip().split(" ")[1]
dict_lines.close()
pronounciation=open("lex_words_hindi_itrans.txt",'r',encoding='utf-8')
g=open("write.txt",'w',encoding='utf-8')
fw=open("temp.txt",'w',encoding='utf-8')
for p_line in pronounciation:
 list_pronun=p_line.rstrip().split(" ")
 temp=[]
 #First step
 i=0
 while i < len(list_pronun):
  if i == 0 :
   prev=""
  if i != 0 :
   prev=dictionary[list_pronun[i-1]]
  try:
   next=dictionary[list_pronun[i+1]]
  except IndexError:
   next=""
  current=dictionary[list_pronun[i]]
  if current == "VOW" and i == 0:
   temp.append(list_pronun[i]+"-F")
  elif current == "VOW" and ( prev == "VOW" or prev == "SCWA"):
   temp.append(list_pronun[i]+"-F")
  elif current == "VOW" and next == "VOW" :
   temp.append(list_pronun[i]+"-F")
  elif current == "SCWA" and ( prev == "VOW" or prev == "SCWA") :
   temp.append(list_pronun[i]+"-F")
  elif current == "VOW" and next == "CON" :
   temp.append(list_pronun[i]+"-F")
  elif current == "VOW" and prev == "SCWA" :
   temp.append(list_pronun[i]+"-F")
  elif current == "SCWA" and i == 0 :
   temp.append(list_pronun[i]+"-F")
  elif current == "CON" and next == "VOW" :
   temp.append(list_pronun[i]+list_pronun[i+1]+"-F")
   i=i+1
  elif current == "CON" and next == "CON" :
   temp.append(list_pronun[i]+"-H")
  elif current == "CON" and next == "SCWA" :
   temp.append(list_pronun[i]+list_pronun[i+1]+"-UNK")
   i=i+1
  i=i+1
 if dictionary[list_pronun[-1]] == "CON" :
   temp.append(list_pronun[-1]+"-F")
 for i in range(0,len(temp)):
   key=temp[i].split("-")[0]
   value=temp[i].split("-")[1]
   #Second Rule
   if key == "ya" :
     if i == 0 :
      temp[i]=key+"-F"
      continue
     elif temp[i-1].split("-")[0] == "i" or temp[i-1].split("-")[0] == "I" or temp[i-1].split("-")[0] == "u" or temp[i-1].split("-")[0] == "U" or temp[i-1].split("-")[0] == "ri" :
      temp[i]=key+"-F"
   #Third Rule
   if key == "ya" or key == "ra" or key == "la" or key == "va" :
    if i == 0 :
      temp[i]=key+"-F"
      continue
    elif temp[i-1].split("-")[1] == "H" :
     temp[i]=key+"-F"
   #Fourth Rule
   if value == "UNK" :
    try :
     if temp[i+1].split("-")[0] == "I" or temp[i+1].split("-")[0] == "i"  or temp[i+1].split("-")[0] == "u" or temp[i+1].split("-")[0] == "U" or temp[i+1].split("-")[0] == "A" or temp[i+1].split("-")[0] == "au" or temp[i+1].split("-")[0] == "ai" or temp[i+1].split("-")[0] == "e" :
      temp[i]=key+"-F"
    except IndexError:
     a=0
   #Fifth Rule
   if value == "UNK" :
    try :
     if temp[i+1].split("-")[1] == "F" :
      temp[i]=key+"-F"
    except IndexError:
     b=0
   #Sixth Rule
   if temp[-1].split("-")[1] == "UNK" :
    temp[-1]=temp[-1].split("-")[0]+"-H"
   #Seventh Rule
   if value == "UNK" :
    try :
     if temp[i+1].split("-")[1] == "H" :
      temp[i]=key+"-F"
    except IndexError:
     c=0
   #Eigth Rule
   if value == "UNK" :
      try :
       if temp[i-1].split("-")[1] == "F" and (temp[i+1].split("-")[1] == "F" or temp[i+1].split("-")[1] == "UNK") :
        temp[i]=key+"-H"
       else:
        temp[i]=key+"-F"
      except IndexError:
       c=0
 g.write(p_line.rstrip()+"\t"+str(" ".join(temp)+"\n"))
 fw.write(str(" ".join(temp)+"\n"))
fw.close()
g.close()
g=open("output.txt",'w',encoding='utf-8')
for line in open("temp.txt",encoding='utf-8'):
 start=line
 line=line.replace("a-H","-H")
 line=line.replace("ai-F"," ai")
 line=line.replace("au-F"," au")
 line=line.replace("RRi-F"," RRi")
 line=line.replace("a-F"," a")
 line=line.replace("A-F"," A")
 line=line.replace("e-F"," e")
 line=line.replace("E-F"," E")
 line=line.replace("I-F"," I")
 line=line.replace("i-F"," i")
 line=line.replace("U-F"," U")
 line=line.replace("u-F"," u")
 line=line.replace("o-F"," o")
 line=line.replace("O-F"," O")
 line=line.replace("-F","")
 line=line.replace("-H","")
 #Some Anuswara rules
 line=line.replace("M g","n g")
 line=line.replace("M Ch","n Ch")
 line=line.replace("M ch","n ch")
 line=line.replace("M kh","n kh")
 line=line.replace("M k","n k")
 line=line.replace("M t","n t")
 g.write(line.rstrip()+"\t"+start)
 
 
 








