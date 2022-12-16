def calculate_calories (calories_string : str):
    calories_per_elf = calories_string.split('\n')
    calories_per_elf = map(int, calories_per_elf)
    
    return sum(calories_per_elf)

elves_calories = []

#Getting elves calories

with open("elves_calories.txt", "r") as calories_file:
    calories_str = calories_file.read()
    calories_arr = calories_str.split("\n\n")
    
    #Getting elves total calories
    elves_calories = [*map(calculate_calories, calories_arr)]
    print(f"The maximum number of calories is : {max(elves_calories)}")
    
    