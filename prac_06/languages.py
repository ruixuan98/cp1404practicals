"""
Cp1404 Practical
Determine if programming languages are dynamic or not
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Print programs and list Dynamically typed languages"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, "1995")
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(visual_basic)

    languages = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.field)


main()
