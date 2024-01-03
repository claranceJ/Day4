list_of_random_things = [1, 3.4, 'a string', True]

# list_of_random_things[len(list_of_random_things) - 1]
#slicing
print(len(list_of_random_things))
print(list_of_random_things[0])
print(list_of_random_things[:3])
print(list_of_random_things[1:])
print(list_of_random_things[-1])
print(list_of_random_things[-2])

#using in and not in
print(1 in list_of_random_things)
print("yellow" not in list_of_random_things)
print("a string" not in list_of_random_things)

#order and mutability

list_of_random_things[0] = "one"
print(list_of_random_things)

month = 8
name_months = [
    "January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December"
]
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# TODO: replace None with appropriate code
# Use list indexing to determine the number of days in `month`
name = (name_months[month - 1])
num_days = (days_in_month[month - 1])
print(name, month, num_days)

# TODO: replace first two months with "jan" and "feb"
# Use list slicing to replace the first two months with "jan" and "feb"
name_months[0:2] = ["jan", "feb"]
print(name_months)

#find the max, min and sorted
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(numbers))
print(min(numbers))
names = [67, 23, 89, 12, 45, 67, 89, 12, 45, 67, 89, 12, 45, 67, 89, 12]
print(sorted(names, reverse=True))

#using join method in list
ruling_class = ['Lion', 'Tiger', 'Dragon', 'Snake', 'Horse', 'Go']
print("-".join(ruling_class))
#using append method in list
ruling_class.append("Monkey")
print(ruling_class)
