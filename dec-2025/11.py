def take_input():
  while True:
    try:
      n = input("Enter a number: ")
      val = int(n)
      if val <= 1:
        print("Number greater than 1 is allowed.")
      else:
        return val
    except ValueError:
      print("It's not an integer.")

def is_prime(n: int):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def main():
  n = take_input()
  prime_count = 0
  for i in range(2, n + 1):
    if is_prime(i):
      prime_count += 1
      print(i)
  print(f"Total primes: {prime_count}")

main()
