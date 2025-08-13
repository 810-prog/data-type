age = [25, 18, 29, 21, 25, 25, 30, 
 22, 19, 28, 20, 24, 25, 18, 
 21, 23, 27, 26, 20, 29, 20, 
 21, 23, 26, 24, 18, 28, 22,
 27, 26, 22, 24, 23, 29, 20,  
 21, 25, 27, 29, 21, 23, 26,
 20, 19, 22, 24, 28, 25, 23,20 ]



indian_dummy_names = [
    "Aarav Sharma", "Veda Iyer", "Ishaan Patel", "Saanvi Kapoor", "Aditya Reddy",
    "Ananya Gupta", "Vikram Mehta", "Priya Rao", "Arjun Desai", "Neha Verma",
    "Rohit Singh", "Sneha Joshi", "Karan Shah", "Pooja Malhotra", "Sameer Agarwal",
    "Shreya Jain", "Rahul Yadav", "Kritika Choudhury", "Amit Kumar", "Rina Nair",
    "Ravi Mishra", "Tanya Kapoor", "Manish Gupta", "Swati Sharma", "Vishal Bhat",
    "Ayesha Khan", "Deepak Patil", "Tanvi Agarwal", "Siddharth Reddy", "Aarti Mehta",
    "Ankur Prasad", "Madhavi Rao", "Puneet Sharma", "Maya Verma", "Anil Kapoor",
    "Disha Patel", "Yash Rajput", "Kiran Das", "Divya Joshi", "Rajesh Saini",
    "Pallavi Singh", "Raghav Gupta", "Simran Bedi", "Nikhil Deshmukh", "Kavya Saxena",
    "Himanshu Kumar", "Neelam Kapoor", "Gaurav Tiwari", "Rekha Yadav", "Suman Nair"
]
# try to do these tasks use loop or comprehensions

# * Print Names with Age Using For Loop ex: Vipin: 24 and so on\
# for name, age in zip(indian_dummy_names,age):
#     print(f"{name}:{age}")

    # .......output.......
#arav Sharma:25
# names with age 

# Veda Iyer:18
# Ishaan Patel:29
# Saanvi Kapoor:21
# Aditya Reddy:25
# Ananya Gupta:25
# Vikram Mehta:30
# Priya Rao:22
# Arjun Desai:19
# Neha Verma:28
# Rohit Singh:20
# Sneha Joshi:24
# Karan Shah:25
# Pooja Malhotra:18
# Sameer Agarwal:21
# Shreya Jain:23
# Rahul Yadav:27
# Kritika Choudhury:26
# Amit Kumar:20
# Rina Nair:29
# Ravi Mishra:20
# Tanya Kapoor:21
# Manish Gupta:23
# Swati Sharma:26
# Vishal Bhat:24
# Ayesha Khan:18
# Deepak Patil:28
# Tanvi Agarwal:22
# Siddharth Reddy:27
# Aarti Mehta:26
# Ankur Prasad:22
# Madhavi Rao:24
# Puneet Sharma:23
# Maya Verma:29
# Anil Kapoor:20
# Disha Patel:21
# Yash Rajput:25
# Kiran Das:27
# Divya Joshi:29
# Rajesh Saini:21
# Pallavi Singh:23
# Raghav Gupta:26
# Simran Bedi:20
# Nikhil Deshmukh:19
# Kavya Saxena:22
# Himanshu Kumar:24
# Neelam Kapoor:28
# Gaurav Tiwari:25
# Rekha Yadav:23
# Suman Nair:20


# * Make a new list that has elements in group of name and age ex: ("vipin", 24), ... and so on
# name_age_pairs = [(name, age) for name, age in zip(indian_dummy_names, age)]
# print(name_age_pairs)

# # ......output...../
# [('Aarav Sharma', 25), ('Veda Iyer', 18), ('Ishaan Patel', 29), 
# ('Saanvi Kapoor', 21), ('Aditya Reddy', 25), ('Ananya Gupta', 25),  ('Vikram Mehta', 30), ('Priya Rao', 22), ('Arjun Desai', 19), 
# ('Neha Verma', 28), ('Rohit Singh', 20), ('Sneha Joshi', 24),  ('Karan Shah', 25), ('Pooja Malhotra', 18), ('Sameer Agarwal', 21),
# ('Shreya Jain', 23), ('Rahul Yadav', 27), ('Kritika Choudhury', 26), 
# ('Amit Kumar', 20), ('Rina Nair', 29), ('Ravi Mishra', 20), 
# ('Tanya Kapoor', 21), ('Manish Gupta', 23), ('Swati Sharma', 26), 
# ('Vishal Bhat', 24), ('Ayesha Khan', 18), ('Deepak Patil', 28),
# ('Tanvi Agarwal', 22), ('Siddharth Reddy', 27), ('Aarti Mehta', 26),
# ('Ankur Prasad', 22), ('Madhavi Rao', 24), ('Puneet Sharma', 23), 
# ('Maya Verma', 29), ('Anil Kapoor', 20), ('Disha Patel', 21), ('Yash Rajput', 25),
# ('Kiran Das', 27), ('Divya Joshi', 29), ('Rajesh Saini', 21), ('Pallavi Singh', 23),
# ('Raghav Gupta', 26), ('Simran Bedi', 20), ('Nikhil Deshmukh', 19), ('Kavya Saxena', 22),
# ('Himanshu Kumar', 24), ('Neelam Kapoor', 28), ('Gaurav Tiwari', 25), ('Rekha Yadav', 23), 
# ('Suman Nair', 20)]





#  Remove all duplicate data from the Age List
# unique_ages = list(set(age))
# print( unique_ages)

# # .....output.../
# [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# # * Get all Names Above 20 years by combining the Age and Numbers
# names_above_20 = [name for name, age in zip(indian_dummy_names, age) if age > 20]
# print("\n")
# print(names_above_20)

# # ...../....output....
# ['Aarav Sharma', 'Ishaan Patel', 'Saanvi Kapoor', 
# 'Aditya Reddy', 'Ananya Gupta', 'Vikram Mehta', 
# 'Priya Rao', 'Neha Verma', 'Sneha Joshi', 'Karan Shah', 
# 'Sameer Agarwal', 'Shreya Jain', 'Rahul Yadav', 'Kritika Choudhury', 
# 'Rina Nair', 'Tanya Kapoor', 'Manish Gupta', 'Swati Sharma', 'Vishal Bhat',
# 'Deepak Patil', 'Tanvi Agarwal', 'Siddharth Reddy', 'Aarti Mehta', 'Ankur Prasad', 
# 'Madhavi Rao', 'Puneet Sharma', 'Maya Verma', 'Disha Patel', 'Yash Rajput',
# 'Kiran Das', 'Divya Joshi', 'Rajesh Saini', 'Pallavi Singh', 'Raghav Gupta',
# 'Kavya Saxena', 'Himanshu Kumar', 'Neelam Kapoor', 'Gaurav Tiwari', 'Rekha Yadav']




# * Get All Names Who Are Of 30 Years
# names_with_30 = [name for name, age in zip(indian_dummy_names, age) if age == 30]
# print(names_with_30)


# # .....output......./
# ['Vikram Mehta']