"""
Min Thiha Khine
#14686570

CP1404/CP5632 - Practical
Broken program to determine score status
"""

"""
Assumptions - "There is no intention to do any repetition." + Original code not having while validation check
The instruction seems to stressed out on the not to do 'ANY REPETITION' 
-so I assume it will only run once to give either 4 outputs

"Rewrite the following program using the most efficient if, elif, else structure you can "
"""

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

