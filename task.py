print("Welcome to the tip calculator")
bill = float(input("what is the bill$ "))
tip = int(input("what percentage tip would you like: 10 12 15 "))
people = int(input("how many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
bill_after_split = bill_with_tip / people

final_amount = (round(bill_after_split, 2))
print(f"each person will pay: ${final_amount}")