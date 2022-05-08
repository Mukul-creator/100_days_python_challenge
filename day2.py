print("Welcome to the tip calculator\n")
bill_Amount = float(input("What was the total bill? "))
no_of_people = int(input("How many people to split bill? "))
tip_percentage = float(input("What percentage tip would yo like to give? 10, 20 or anything... "))

total_including_tip = bill_Amount + (tip_percentage * bill_Amount)/100

print("Each person should pay:", (total_including_tip/no_of_people).__format__(".2f"))