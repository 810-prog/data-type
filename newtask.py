people=[
("Vipin", 24),
("Rahul kumar", 30),
("Priya", 25),
("Amit", 28),
("Rahul", 30),
("Sonia", 22)]



# write a python program Use Loop or comprehension to solve program mentioned below:
# * Print a greeting for each person, like "Hello Vipin, you are 24 years old." and so on.

# for name, age in people:
#     print(f"Hello {name}, you are {age} years old.")
# print("-" * 50)

# ......*output.......
# Hello Vipin, you are 24 years old.
# Hello Rahul kumar, you are 32 years old.
# Hello Priya, you are 25 years old.
# Hello Amit, you are 28 years old.
# Hello Rahul, you are 30 years old.
# Hello Sonia, you are 22 years old.
# --------------------------------------------------

# * Create a single string that lists all the names separated by a comma. The output should be "Vipin, Rahul, Priya, Amit, Rahul, Sonia".

# people_names = ", ".join([name for name, age in people])
# print(people_names)

# .....output......
# Vipin, Rahul, Priya, Amit, Rahul, Sonia


# * Create a dictionary of names and ages, but only for people whose age is a multiple of 5 (e.g., 25, 30).
# people_dict = {name: age for name, age in people if age % 5 == 0}
# print("people_dict:", people_dict)

# ....output...
# people_dict: {'Rahul kumar': 30, 'Priya': 25, 'Rahul': 30}


# * Get the total number of people who are 30 years or older.
# total_people_30_or_older = sum(1 for _, age in people if age >= 30)
# print("total_people_30_or_older:",total_people_30_or_older)

# ...output...
# 2


# * Find the oldest person's name and age. The output should be a tuple, e.g., ("Rahul", 32).
# oldest_person = max(people, key=lambda x: x[1])
# print("oldest_person:",oldest_person)

# .....output.....
# oldest_person:('Rahul kumar', 30)


# * Find the average age of all the people in the list.
# average_age = sum(age for _, age in people) / len(people)
# print("average age:", round(average_age, 2))

# ...output......
# average age: 26.5