import sys

while True:
    
    Alph = str (raw_input("Enter an alphabet "))

    if Alph and  Alph.isalpha():
         if len(Alph) > 1 :
              print("sorry! Enter an alphabet")
         else:
              if (Alph == 'a' or Alph =='i' or Alph =='e' or Alph =='o' or Alph =='u') :
                   print ("Vowel")
                   break
              else :
                   print ("Consonant")
                   break
    else :
         print("sorry. Enter an alphabet")



