#Practice-1

dollar_amount = float(input("Enter the amount in dollars: $"))

exchange_rate = 2
euro_amount = dollar_amount * exchange_rate

print(f"${dollar_amount} is equal to {euro_amount} euros.")

#Practise-2
ranking_list = ["John", "Sen", "Lisa"]

rank_number = int(input("Enter rank number: "))

if 1 <= rank_number <= len(ranking_list):
    person = ranking_list[rank_number - 1]
    print(f"The person at rank {rank_number} is {person}.")
else:
    print("Invalid rank number.")

#Practise-3

ranking_list = ["John", "Sen", "Lisa"]

person_name = input("Enter the person's name: ")

if person_name in ranking_list:
    rank = ranking_list.index(person_name) + 1
    print(f"{person_name} is ranked {rank}.")
else:
    print(f"{person_name} is not in the ranking list.")

#Practise-4

mood = "Happy"      # String
strength = 8.5      # Float
rank = 3             # Integer

print("Mood:", mood)
print("Strength:", strength)
print("Rank:", rank)

#Practise-5

# Assigning a tuple to color_codes
color_codes = (
    ("Red", 255, 0),
    ("Green", True, 128),
    ("Blue", 0, 255)
)

print("Color Codes:", color_codes)

#Practise-6
serials = [123, 456, 789, 101, 112]

print("The 3rd item of the list is:", serials[2])

#Practise-7

seconds = [10, 20, 30, 40]

current = 50

seconds.append(current)

print("Updated list:", seconds)

#Practise-8

file_list = ["Document.txt", "Report.txt", "Presentation.txt"]

for index, file_name in enumerate(file_list):
    print(f"{index}-{file_name}")

#Practise-9

ip_list = ["192.168.1.1", "100.122.133.111"]

user_input = input("Enter an index (0 or 1): ")

try:
    index = int(user_input)
    chosen_ip = ip_list[index]
    print(f"You chose {chosen_ip}")
except (ValueError, IndexError):
    print("Invalid index or input.")

#Practise-10

temperatures = [25.5, 18, "High"]

print("Temperatures:", temperatures)








