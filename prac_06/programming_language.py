"""
CP1404 Practicals
Class for different programming languages
"""


class ProgrammingLanguage:
    """Store list of lists of programming languages"""

    def __init__(self, field, typing, reflection, year=0):
        """Initialize a programming language"""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True value if language is dynamically typed"""
        if self.typing == "Dynamic":
            return True

    def __str__(self):
        """Prints objects neatly in a string"""
        return f"{self.field}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"
