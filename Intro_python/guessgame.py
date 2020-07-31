def askUserForNumber():
  userNumber=int(input("Guess the number:"))
  return userNumber
 def checkUserNumber(userNumber, randomNumber):
  if userNumber>randomNumber:
    return "Too High"
  elif userNumber<randomNumber:
    return "Too low"
  else:
 def main():
  randomNumber=generateRandomNumber()
  userNumber=askUserForNumber
  message=checkUserNumber(userNumber,randomNumber)
  while message!="Congradulations":
    print(message)
    userNumber=askUserForNumber
