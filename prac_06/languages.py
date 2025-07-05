"""
Estimated: 8 minutes
Actual:
"""

from prac_06.programming_language import ProgrammingLanguage



python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [python, ruby, visual_basic] # List containing the three programming languages

print("The dynamically typed languages are:")
for language in programming_languages: # Loop through all the programming languages one by one
    if language.is_dynamic(): # If dynamic
        print(language.name) # print the language name

