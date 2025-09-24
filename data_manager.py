#collect age and name
name = input("Enter your name: ")
age = int(input("Enter your age: "))

#collect hobbies and loop
hobbies = set()
while True:
    hobby = input("Enter a hobby (or type 'done' to finish): ")
    if hobby.lower() == "done":
        break
    hobbies.add(hobby)


user_data = {
    "name": name,
    "age": age,
    "hobbies": list(hobbies)
}


current_year = 2025
birth_year = current_year - age
years = (birth_year, current_year)

#print final data
print("\n--- Personal Data Summary ---")
print(f"Name: {user_data['name']}")
print(f"Age: {user_data['age']}")
print(f"Hobbies: {', '.join(user_data['hobbies'])}")
print(f"Birth Year: {years[0]}, Current Year: {years[1]}")
