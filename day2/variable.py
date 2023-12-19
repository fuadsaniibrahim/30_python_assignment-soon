#Day 2: 30 Days of python programming
import math

first_name = "Fuad"
last_name = "Sani"
full_name = first_name + " " + last_name
country = "Nigeria"
city = "Kano"
age = 30
year = 2023
is_married = True
is_true = False
is_light_on = True


_python, _like, number = True, True, 180


print("First Name:", first_name)
print("Last Name:", last_name)
print("Full Name:", full_name)
print("Country:", country)
print("City:", city)
print("Age:", age)
print("Year:", year)
print("Is Married:", is_married)
print("Is True:", is_true)
print("Is Light On:", is_light_on)
print("Address:", _python)
print("Zip Code:", _like)
print("Height:", number)


#level 2

# Check data types
print("Data type of first_name:", type(first_name))
print("Data type of last_name:", type(last_name))
print("Data type of full_name:", type(full_name))
print("Data type of country:", type(country))
print("Data type of city:", type(city))
print("Data type of age:", type(age))
print("Data type of year:", type(year))
print("Data type of is_married:", type(is_married))
print("Data type of is_true:", type(is_true))
print("Data type of is_light_on:", type(is_light_on))
print("Data type of address:", type(_python))
print("Data type of zip_code:", type(_like))
print("Data type of height:", type(number))


len_first_name = len(first_name)
print("Length of first name:", len_first_name)


len_last_name = len(last_name)
if len_first_name == len_last_name:
    print("Length of first name is equal to length of last name.")
else:
    print("Length of first name is not equal to length of last name.")


num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two


radius_of_circle = 30
area_of_circle = math.pi * (radius_of_circle ** 2)
circum_of_circle = 2 * math.pi * radius_of_circle


user_radius = float(input("Enter the radius of the circle: "))
user_area_of_circle = math.pi * (user_radius ** 2)


user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = int(input("Enter your age: "))


help('keywords')
