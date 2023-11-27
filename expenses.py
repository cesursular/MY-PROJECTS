expenses = []

def enter_expense():
    value = float(input("Entry a expense value: "))
    description = input("Entry expense's description: ")
    expense = {"value": value, "description": description}
    expenses.append(expense)
    print("Expense is added")

def list_the_expenses():
    for expense in expenses:
      print(f"Value: {expense["value"]}, Description: {expense["description"]}")

def calc_all_expenses():
    total = sum(expense["value"] for expense in expenses)
    print(f"Total Expenses: {total}")

def main_menu():
    while True:
      print("\n--- PERSONAL EXPENSE FOLLOW LIST---")
      print("1. add expense")
      print("2. list the expenses")
      print("3. calc to all expenses")
      print("4. exit")

      choice = input("Make a choice (!-4): ")

      if choice == "1":
          enter_expense()
      elif choice == "2":
          list_the_expenses()
      elif choice == "3":
          calc_all_expenses()
      elif choice == "4":
          print("exiting the app")
          break
      else:
          print("invalid choice! please choice between 1-4")
