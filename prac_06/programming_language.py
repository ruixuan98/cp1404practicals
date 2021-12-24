"""
CP1404 Practicals
Class for different programming languages
"""


class ProgrammingLanguage:
    """Store list of lists of programming languages"""

    def __init__(self, field, typing, reflection, year=0):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True

    def __str__(self):
        return f"{self.field}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"
