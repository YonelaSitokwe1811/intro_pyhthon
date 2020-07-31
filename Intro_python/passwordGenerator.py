import random
def passwordGenerator():
  lowerchars=['a','b','c','d']
  upperchars=['A','B','C','D']
  specialchars=['&','!','*']
  numericchars=['1','2','3','4']
  pass

  password=random.choice(lowerchars)+random.choice(upperchars)+random.choice(specialchars)+random.choice(numericchars)
 
  password=password+password
  return password

print(passwordGenerator())
  