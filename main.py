print("Hi, Welcome to the tip calculator.")
total_bill= float(input("What was the total bill ?$ "))
tip = int(input("What percentage tip would you like to give ? 10 ,12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
total_bill += (total_bill*(tip/100))
each_person_bill =(total_bill / number_of_people)
final_amount = round(each_person_bill,2)
final_amount ="{:.2f}".format(each_person_bill)
print(f"Each persson should pay: ${final_amount}")


