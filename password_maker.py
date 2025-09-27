import random #for password generator
import re

#strength checker function
def check_strength(password):
  length = len(password)
  # check the criteria
  has_lower = re.search(r"[a-z]", password)
  has_upper = re.search(r"[A-Z]", password)
  has_digit = re.search(r"[0-9]", password)
  has_symbol = re.search(r"[!@#$%&*?]", password)
  #rules
  if length < 6:
    return "The password is WEAK (Too Short)"
  elif length >= 8 and has_lower and has_upper and has_digit and has_symbol:
    return "The password is STRONG"
  else:
    return "The password is MEDIUM. Please make it longer"
    
# Main Program
print ("WELCOME TO PERSONALIZED PASSWORD MAKERS !")
while True:
  name = input ("\nEnter your nickname: ")
  birth_year = input ("Enter your birth year: ")
  base = name[:3] + birth_year [-2:] #choosen one is 3 first word nickname + last 2 birthyear
  keyword =  input("Enter a word that you love (related to hobby / food / hometown / etc.: ").upper()
  symbols = "!@#$%&*?"

#make iteration (3 password suggestion)
  for i in range (1,4):
    password = base + str(random.randint(10,99)) + keyword + random.choice(symbols)
    print (f"{i}. {password}")
    print ("Strength: " , check_strength(password))
  again = input("\nDo you want to generate again? (yes/no): ").lower()
  if again !="yes":
    print("Goodbye!")
    break
