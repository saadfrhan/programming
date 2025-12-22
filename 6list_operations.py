numbers: list[int] = []

for i in range(1, 6):
  num = input(f"enter number {i}: ")
  numbers.append(int(num))

print([num for num in numbers])
print(sum(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers) / len(numbers))
