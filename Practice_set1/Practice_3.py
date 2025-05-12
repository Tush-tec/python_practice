# Fruit Ripeness Checker

#  Determine if a Fruit is Ripe, Overripe , orr Unripe based on its color
# (e.g, Banana: 
# Green - unRipe
# Yellow - Ripe
# Brown - Overripe
# )

color = input("Enter the color of the fruit: ")
fruit = input("Enter the name of the fruit: ")

fruit_stage = lambda c: (
    "unripe" if c == "Green"  else
    "Ripe" if c == "Yellow" else
    "Overripe" if c == "Brown" else
    "Unknown stages"
)
print(f"the {fruit} is {fruit_stage(color)}")