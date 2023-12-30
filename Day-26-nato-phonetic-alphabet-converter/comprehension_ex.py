# Comprehension
numbers = [1, 1, 2, 3, 4, 5, 8, 13, 21, 34, 55]
# make a list of squared numbers from the numbers list
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

# make a list of even numbers from the numbers list filtering out odd numbers
even_numbers_only = [int(num) for num in numbers if num % 2 == 0]
print(even_numbers_only)

# given 2 lists of names, make a list of names that are common in both lists
first_names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
second_names = ["Alex", "Giovanni", "Caroline", "Micheal", "Andrew", "Marco"]

new_names = [name for name in first_names if name in second_names]
print(new_names)

# Dictionary Comprehension
import random

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
studpent_scores = {student: random.randint(1, 100) for student in names}
print(studpent_scores)
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

passed_students = {
    student: score for (student, score) in studpent_scores.items() if score >= 60
}
print(f"passed students: {passed_students}")

# phrase = input()
phrase = "what is the airspeed velocity of an unladen swallow"
phrase_dict = {word: len(word) for word in phrase.split()}
print(phrase_dict)

temperature = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# create a new dictionary from the temperature dictionary and convert the values from celsius to fahrenheit
temperature_f = {day: (temp * 9 / 5) + 32 for (day, temp) in temperature.items()}
print(temperature_f)
