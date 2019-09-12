class ProgrammingLanguage:

    def __init__(self, name, type, reflection, year):
        self.name = name
        self.type = type
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Type, Reflection={}, Year={}".format(self.name, self.type, self.reflection, self.year)

    def is_dynamic(self):
        return self.type == "dynamic"

# testring if the language is dynamic
# def testing(self):
#     ruby = ProgrammingLanguage("Ruby", "dynamic", True, 1995)
#     python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
#     visual_basic = ProgrammingLanguage("Visual Basic", "static", False, 1991)

#    languages = [ruby, python, visual_basic]
#    print(python)

#    print("The dynamically typ of languages are: ")
#    for language in languages:
#        if language.is_dynamic():
#            print(language.name)
              