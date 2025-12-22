def ask_for_limit():
  while True:
    n = input("Enter a limit of numbers to loop till: ")
    try:
      val = int(n)
      if val <= 0:
        print("Non-postive number is not allowed.")
      else: 
        return val
    except ValueError:
      print("It's not an integer.")

def fizzbuzz(val: int):
  for i in range(1, val + 1):
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)

def main():
  val = ask_for_limit()
  fizzbuzz(val)

main()

