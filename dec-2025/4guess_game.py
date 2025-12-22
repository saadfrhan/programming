import random

secret_number = random.randint(1, 100)
tries_used = 0

while True:
  guess = int(input("Guess the secret number: "))
  tries_used += 1
  if tries_used == 7:
    print(f"YOU LOSE! The number was {secret_number}")
    break
  elif guess > secret_number:
    print("high")
  elif guess < secret_number:
    print("low")
  elif guess == secret_number:
    print(f"YOU WIN! you tried {tries_used} times.")
    break

print("Day 1 complete.")
