from random import *

print "Welcome To The Math Practice Game!!"
a=raw_input("Which game would you like to play?\n\n1-Addition Game\n2-Multiplication Game\n3-Subtraction Game\n4-Random\n1, 2, 3, or 4: ")

def add_easy():
   global score
   global lives
   add_easy_a=randint(1,10)
   add_easy_b=randint(1,10)
   print("\nscore: "+str(score))
   print("lives: "+str(lives))
   add_easy_answer=raw_input("How much is %s + %s? " % (add_easy_a,add_easy_b))
   if int(add_easy_answer)==(add_easy_a + add_easy_b):
      print("That's Right!!")
      score=score+1
      add_easy()
      add_easy_a=randint(1,10)
      add_easy_b=randint(1,10)
   else:
      print("Sorry, That's Not Right")
      lives=lives-1
      if lives>0:
         add_easy()
         add_easy_a=randint(1,10)
         add_easy_b=randint(1,10)
      else:
         print("\nToo Bad, You Lose :(")
         
def add_med():
   global score
   global lives
   add_med_a=randint(10,100)
   add_med_b=randint(10,100)
   print("\nscore: "+str(score))
   print("lives: "+str(lives))
   add_med_answer=raw_input("How much is %s + %s? " % (add_med_a,add_med_b))
   if int(add_med_answer)==(add_med_a + add_med_b):
      print("That's Right!!")
      score=score+1
      add_med()
      add_med_a=randint(10,100)
      add_med_b=randint(10,100)
   else:
      print("Sorry, That's Not Right")
      lives=lives-1
      if lives>0:
         add_med()
         add_med_a=randint(10,100)
         add_med_b=randint(10,100)
      else:
         print("\nToo Bad, You Lose :(")
         
def add_hard():
   global score
   global lives
   add_hard_a=randint(-100,100)
   add_hard_b=randint(-100,100)
   print("\nscore: "+str(score))
   print("lives: "+str(lives))
   add_hard_answer=raw_input("How much is %s + %s? " % (add_hard_a,add_hard_b))
   if int(add_hard_answer)==(add_hard_a + add_hard_b):
      print("That's Right!!")
      score=score+1
      add_hard()
      add_hard_a=randint(-100,100)
      add_hard_b=randint(-100,100)
   else:
      print("Sorry, That's Not Right")
      lives=lives-1
      if lives>0:
         add_hard()
         add_hard_a=randint(-100,100)
         add_hard_b=randint(-100,100)
      else:
         print("\nToo Bad, You Lose :(")
         
def mult_easy():
   global score
   global lives
   mult_easy_a=randint(1,10)
   mult_easy_b=randint(1,10)
   print("\nscore: "+str(score))
   print("lives: "+str(lives))
   mult_easy_answer=raw_input("How much is %s x %s? " % (mult_easy_a,mult_easy_b))
   if int(mult_easy_answer)==(mult_easy_a * mult_easy_b):
      print("That's Right!!")
      score=score+1
      mult_easy()
      mult_easy_a=randint(1,10)
      mult_easy_b=randint(1,10)
   else:
      print("Sorry, That's Not Right")
      lives=lives-1
      if lives>0:
         mult_easy()
         mult_easy_a=randint(1,10)
         mult_easy_b=randint(1,10)
      else:
         print("\nToo Bad, You Lose :(")
         
def mult_med():
   global score 
   global lives
   mult_med_a=randint(1,20)
   mult_med_b=randint(1,20)
   print("\nscore: "+str(score))
   print("lives: "+str(lives))
   mult_med_answer=raw_input("How much is %s x %s? " % (mult_med_a,mult_med_b))
   if int(mult_med_answer)==(mult_med_a * mult_med_b):
      print("That's Right!!")
      score=score+1
      mult_med()
      mult_med_a=randint(1,20)
      mult_med_b=randint(1,20)
   else:
      print("Sorry, That's Not Right")
      lives=lives-1
      if lives>0:
         mult_med()
         mult_med_a=randint(1,20)
         mult_med_b=randint(1,20)
      else:
         print("\nToo Bad, You Lose :(")
         
def mult_hard():
   global score 
   global lives
   mult_hard_a=randint(10,30)
   mult_hard_b=randint(10,30)
   print("\nscore: "+str(score))
   print("lives: "+str(lives))
   mult_hard_answer=raw_input("How much is %s x %s? " % (mult_hard_a,mult_hard_b))
   if int(mult_hard_answer)==(mult_hard_a * mult_hard_b):
      print("That's Right!!")
      score=score+1
      mult_hard()
      mult_hard_a=randint(10,30)
      mult_hard_b=randint(10,30)
   else:
      print("Sorry, That's Not Right")
      lives=lives-1
      if lives>0:
         mult_hard()
         mult_hard_a=randint(10,30)
         mult_hard_b=randint(10,30)
      else:
         print("\nToo Bad, You Lose :(")
         
def sub_easy():
   global score 
   global lives
   sub_easy_a=randint(1,10)
   sub_easy_b=randint(1,10)
   print("\nscore: "+str(score))
   print("lives: "+str(lives))
   sub_easy_answer=raw_input("How much is %s - %s? " % (sub_easy_a,sub_easy_b))
   if int(sub_easy_answer)==(sub_easy_a - sub_easy_b):
      print("That's Right!!")
      score=score+1
      sub_easy()
      sub_easy_a=randint(1,10)
      sub_easy_b=randint(1,10)
   else:
      print("Sorry, That's Not Right")
      lives=lives-1
      if lives>0:
         sub_easy()
         sub_easy_a=randint(1,10)
         sub_easy_b=randint(1,10)
      else:
         print("\nToo Bad, You Lose :(")
         
def sub_med():
   global score 
   global lives
   sub_med_a=randint(10,100)
   sub_med_b=randint(10,100)
   print("\nscore: "+str(score))
   print("lives: "+str(lives))
   sub_med_answer=raw_input("How much is %s - %s? " % (sub_med_a,sub_med_b))
   if int(sub_med_answer)==(sub_med_a - sub_med_b):
      print("That's Right!!")
      score=score+1
      sub_med()
      sub_med_a=randint(10,100)
      sub_med_b=randint(10,100)
   else:
      print("Sorry, That's Not Right")
      lives=lives-1
      if lives>0:
         sub_med()
         sub_med_a=randint(10,100)
         sub_med_b=randint(10,100)
      else:
         print("\nToo Bad, You Lose :(")
         
def sub_hard():
   global score 
   global lives
   sub_hard_a=randint(-100,100)
   sub_hard_b=randint(-100,100)
   print("\nscore: "+str(score))
   print("lives: "+str(lives))
   sub_hard_answer=raw_input("How much is %s - %s? " % (sub_hard_a,sub_hard_b))
   if int(sub_hard_answer)==(sub_hard_a - sub_hard_b):
      print("That's Right!!")
      score=score+1
      sub_hard()
      sub_hard_a=randint(-100,100)
      sub_hard_b=randint(-100,100)
   else:
      print("Sorry, That's Not Right")
      lives=lives-1
      if lives>0:
         sub_hard()
         sub_hard_a=randint(-100,100)
         sub_hard_b=randint(-100,100)
      else:
         print("\nToo Bad, You Lose :(")

score=0
lives=3

if a==str(1):
   b=raw_input("Pick a level:\n\n1-easy\n2-medium\n3-hard\n1, 2, or 3: ")
   if b==str(1):
      add_easy()    
   elif b==str(2):
      add_med()
   elif b==str(3):
      add_hard()
   else:
      print("You have to enter \"1\" \"2\" or \"3\"")
elif a==str(2):
   b=raw_input("Pick a level:\n\n1-easy\n2-medium\n3-hard\n1, 2, or 3: ")
   if b==str(1):
      mult_easy()
   elif b==str(2):
      mult_med()
   elif b==str(3):
      mult_hard()
   else:
      print("You have to enter \"1\" \"2\" or \"3\"")
elif a==str(3):
   b=raw_input("Pick a level:\n\n1-easy\n2-medium\n3-hard\n1, 2, or 3: ")
   if b==str(1):
      sub_easy()
   elif b==str(2):
      sub_med()
   elif b==str(3):
      sub_hard()
   else:
      print("You have to enter \"1\" \"2\" or \"3\"")
elif a==str(4):
   rand_num=randint(1,9)
   if rand_num==1:
      print("\nYou Got The Easy Addition Game")
      add_easy()
   elif rand_num==2:
      print("\nYou Got The Medium Level Addition Game")
      add_med()
   elif rand_num==3:
      print("\nYou Got The Hard Addition Game")
      add_hard()
   elif rand_num==4:
      print("\nYou Got The Easy Multiplication Game")
      mult_easy()
   elif rand_num==5:
      print("\nYou Got The Medium Level Multiplication Game")
      mult_med()
   elif rand_num==6:
      print("\nYou Got The Hard Multiplication Game")
      mult_hard()
   elif rand_num==7:
      print("\nYou Got The Easy Subtraction Game")
      sub_easy()
   elif rand_num==8:
      print("\nYou Got The Medium Level Subtraction Game")
      sub_med()
   elif rand_num==9:
      print("\nYou Got The Hard Subtraction Game")
      sub_hard()      
else:
   print("You have to enter \"1\", \"2\", \"3\", or \"4\"")