age = int(input("What's your age? "))

if age < 13:
  print("You're a kid.")
elif age >= 13 and age <= 19:
  print("You're a teenager.")
elif age >= 20 and age <= 59:
  print("You're an adult.")
else:
  print("You're a senior.")

can_code = input("Can you code? (yes/no) ")

if can_code == "yes" and (age >= 20 and age <= 59):
  print("You're ready for this journey.")
elif can_code == "no":
  print("You will learn.")
