"""
Min Thiha Khine
(#14686570)

Score status determining program with functions
This program validates and categorizes scores based on predefined ranges."""

#CONSTANTS
LOWER_BOUND = 0
UPPER_BOUND = 100
EXCELLENT_SCORE_BOUND = 90
PASS_SCORE_BOUND = 50

score = float(input("Enter score: ")) # Get User input

# Rewritten the original conditions in an efficient manner
#Conditional outputs based on Score
if score < LOWER_BOUND or score > UPPER_BOUND: #Invalid Score
    print("Invalid score")
elif score >= EXCELLENT_SCORE_BOUND: #Excellent Score
    print("Excellent")
elif score >= PASS_SCORE_BOUND: #Passable Score
    print("Passable")
else: # Bad Score
    print("Bad score")

