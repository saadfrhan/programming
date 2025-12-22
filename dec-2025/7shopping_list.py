shop_list: list[str] = [""]

while True:
  print("=== SHOPPING LIST ===")
  print("1. Add item")
  print("2. View list")
  print("3. Remove item")
  print("4. Exit")
  option = input("Choose option: ")
  if option == "1":
    item_name = input("Enter item name: ")
    shop_list.append(item_name)
    print(f"ADDED")
  elif option == "2":
    for index, item in enumerate(shop_list):
      if item == "":
        print("Your list is empty.")
      else:
        print(f"{index}. {item}")
  elif option == "3":
    item_number = int(input("Enter which item number to remove: "))
    shop_list.pop(item_number)
    print(f"REMOVED")
  elif option == "4":
    break
