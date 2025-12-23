def take_input():
  while True:
    try:
      n = input("Enter a number: ")
      val = int(n)
      if val <= 0:
        print("Positive numbers are allowed.")
      else:
        return val
    except ValueError:
      print("It's not an integer.")

def sum_numbers(val: int):
  sum = 0
  sum_even = 0
  sum_odd = 0
  for i in range(1, val + 1):
    sum += i
    if i % 2 == 0:
      sum_even += i
    else:
      sum_odd += i
  return sum, sum_even, sum_odd

def main():
  val = take_input()
  sum, sum_even, sum_odd = sum_numbers(val)
  print(f"Total: {sum}")
  print(f"Even: {sum_even}")
  print(f"Odd: {sum_odd}")

main()
