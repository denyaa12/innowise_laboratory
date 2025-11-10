def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Invalid age"

year = 2025

user_name = input("Enter your full name: ")
print(f"Nice to meet you, {user_name}!")

birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)

current_age = year - birth_year
print(f"Your current age: {current_age}")

hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    hobbies.append(hobby)

life_stage = generate_profile(current_age)

user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

print("\nUser Profile")
print(f"Name: {user_profile['name']}")
print(f"Current Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")

# Check if hobbies list is empty
if len(user_profile['hobbies']) == 0:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
    for hobby in user_profile['hobbies']:
        print(f"  - {hobby}")
