#Created by Ahmed Salama, You can ask me questions or alert me if anything goes wrong!
import re # Regular Expressions
import string

alphabets = "abcdefghijklmnopqrstuvwxyz" # this is the english letters
def encrypt(p, k):
    c = ""
    kpos = alphabets.find(k)   # this will return the index of the character ex: if k='d' then kpos= 3
    for x in p:
      pos = alphabets.find(x) + kpos    #find the number or index of the character and perform the shift with the key
      if pos > 25:
          pos = 26-pos               # check you exceed the limit
      c += alphabets[pos].capitalize()  #because the cipher text always capital letters
    return c

def decrypt(c, k):
    p = ""
    kpos = alphabets.find(k)
    for x in c:
        pos = alphabets.find(x) - kpos
        if pos < 0:
            pos = pos + 26
        p += alphabets[pos].lower()# because the cipher text always capital letters
    return p
try:
    print("Welcome to ceaser cipher algorithm by Ahmed salama.\n\n"
          "The text message should contain only characters and the key should be one digit character\n"
          "Press 1 to Enrypt a message \npress 2 to Decrypt a message")
    choose = input("Choice: ")
    if choose == '1':
       p = input("enter the plain text: ")
       p = p.replace(" ", "")  # this will make sure that there is no space in the message
       if p.isalpha():
           k = input("Enter the key: ")
           if len(k) > 1 or k.isalpha() == False:
               print("Enter valid key, key is only one letter")
           else:
               c = encrypt(p, k)
               print("The cipher text is: ", c)
       else:
           print("only letters are allowed !!")

    elif choose == '2':
        c = input("enter the cipher text: ")
        c = c.replace(" ", "")
        if c.isalpha():
            k = input("Enter the key: ")
            if len(k) > 1 or k.isalpha() == False:
                print("Enter valid key, key is only one letter")
            else:
                p = decrypt(c, k)
                print("The plain text is: ", p)
        else:
            print("only letters are allowed !!")

    else:
        print("Please enter a valid choice !")
except:
   exit("Enter a valid text please !")
