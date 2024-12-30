score = [int]*5
for counter in range (0,5):
    score[counter] = int(input("Enter a test score here: "))
    while score[counter] <0 or score[counter] >150:
        score[counter] = int(input("Invalid score. Please enter a score between 1 and 150: "))
for counter in range (0,5):
    percentage = (score[counter]/150)*100
    if percentage >= 70:
        print(percentage ,"%. Congratulations, you passed")
    else:
        print(percentage ,"%. Sorry, you did not pass")

