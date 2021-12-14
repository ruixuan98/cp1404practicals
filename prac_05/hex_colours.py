"""
CP1404 Practical
User to lookup hexidecimal colour
"""

COLOUR_CODES = {"Absolute Zero": "#0048ba",
                "Acid Green": "#b0bf1a",
                "Aliceblue": "#f0f8ff",
                "Alizarin crimson": "#e32636",
                "Amaranth": "#e52b50",
                "Amber": "#ffbf00",
                "Amethyst": "##9966cc",
                "Antiquewhite": "#faebd7",
                "Apricot": "#fbceb1",
                "Aqua": "#00ffff"}

colour_name = str(input("Enter colour: ")).title()
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print(f"Code for {colour_name} is {COLOUR_CODES[colour_name]}")
        colour_name = str(input("Enter colour: ")).title()
    else:
        print("Colour not found.")
        colour_name = str(input("Enter colour: ")).title()