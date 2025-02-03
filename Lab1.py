x = 4
y = 2
print(x+y)
car_name = "Mercedes"
num_wheels = 4
print(f"The car name is a {car_name} and it has {num_wheels} wheels")
name = "Gabriel"
num_apples = 24
num_friends = 7
apples_per_friend = num_apples // num_friends
print(f"My name is {name}. I have {num_apples} apples, and {num_friends} of friends. For each friend I can give them {apples_per_friend} apples.")
bill_total = 120
num_people = 6
cost_per_person = bill_total/num_people
print(f"The bill total is ${(bill_total):0.2f} for the {num_people} person table. Per person it costs: ${(cost_per_person):0.2f}")
print(f"The bill total is ${int(bill_total)} for the {num_people} person table. Per person it costs: ${int(cost_per_person)}")
dessert_cost = 6.55 
total_cost_of_desserts = num_people * dessert_cost
print(f"For {num_people} people, the total cost of desserts is ${total_cost_of_desserts:0.2f} at each dessert ${dessert_cost:0.2f}")