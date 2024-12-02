spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_name = [food['name'] for food in spicy_foods]
    return food_name

get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    food = [heat_food for heat_food in spicy_foods if heat_food['heat_level'] > 5]
    return food
get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for spici_food in spicy_foods:
       heat_level = '🌶' * spici_food['heat_level']

       new_outlook = f"{spici_food['name']} ({spici_food['cuisine']}) | Heat Level: {heat_level}"
       print(new_outlook)
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # type_cuisine = [by_cuisine for by_cuisine in spicy_foods if cuisine == by_cuisine['cuisine']]
    for by_cuisine in spicy_foods:
        if cuisine == by_cuisine['cuisine']:
            type_cuisine = by_cuisine
    return type_cuisine
get_spicy_food_by_cuisine(spicy_foods, 'Sichuan')

def print_spiciest_foods(spicy_foods):
    for spici_food in spicy_foods:
        heat_level = '🌶' * spici_food['heat_level']

        if spici_food['heat_level'] > 5:
            new_outlook = f"{spici_food['name']} ({spici_food['cuisine']}) | Heat Level: {heat_level}"
            print(new_outlook)
           
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
        total_level = sum(spici_food['heat_level'] for spici_food in spicy_foods)
        av_heatlevel = int(total_level / len(spicy_foods))
        print(av_heatlevel)
        return av_heatlevel
get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
create_spicy_food(spicy_foods, spicy_foods)