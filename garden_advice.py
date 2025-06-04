def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"

def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."

# Get input from user
season = input("Enter the current season (e.g., summer, winter): ").strip().lower()
plant_type = input("Enter the plant type (e.g., flower, vegetable): ").strip().lower()

# Generate and print advice
advice = get_season_advice(season) + get_plant_advice(plant_type)
print(advice)
