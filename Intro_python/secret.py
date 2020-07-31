secret_number=42
guess=0 
while guess!=secret_number:
 guess=eval(input(" Enter number: "))
if guess < secret_number:
  print(" low")
elif guess > secret_number:
  print(" high")
print("Correct!")
