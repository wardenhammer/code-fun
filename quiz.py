answers = [11, 10, 2015, 23, 47]
questions = ["How many songs (not including interludes) are on My Beautiful Dark Twisted Fantasy? ",
             "How many studio albums has Kanye West released? ",
             "What year did Kanye West release the single All Day? ",
             "How long are both the albums ye and KIDS SEE GHOSTS? ",
             "How old is Kanye West? "]
score = 0
for counter in range (0,5):
    print(questions[counter])
    answer = int(input())
    if answer == answers[counter]:
        score += 1
print ("you got", score, "out of 5")