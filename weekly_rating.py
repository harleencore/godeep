hours = 0
intensity = 0
breakthroughs = 0
goals = 0
committed_changes = 0

print("\n")

print("NUMBER OF HOURS")
num_hours = float(input("How many hours did you clock in this week? "))
hours = num_hours/25
print("hours:", hours, "\n")

print("INTENSITY")
print("How would you rate the effectiveness of your deep work sessions?")
print("Not effective[25%] somewhat effective[50%] effective[75%] very effective[100%]")
intensity = float(input("enter a number from 0.25 to 1: "))
print("\n")

print("BREAKTHROUGHS")
print("Did you learn 3 big things this week?")
print("1 big thing: 50%")
print("2 big things: 75%")
print("3 big things: 100%")
breakthroughs = float(input("enter a number from 0 to 1: "))
print("\n")

print("GOALS")
print("Were your goals realistic? Too easy? Just nice? Too hard! Were they met?")
goals = float(input("Enter a number from 0 to 1: "))
print("\n")

print("COMMITTED CHANGES")
number_commits = float(input("Enter number of changes committed last week: "))
number_changes = float(input("Enter number of successfully addressed changes: "))
committed_changes = number_changes/number_commits
print("committed_changes:", committed_changes, "\n")

score = (hours + intensity + breakthroughs + goals + committed_changes)/5
print("Your score is:", score)
