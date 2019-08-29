scores_file = open("scores.csv")
scores_data = scores_file.readlines()
print(scores_data)
subjects = scores_data[0].strip().split(",")
score_values = []
for score_line in scores_data[1:]:
    score_strings = score_line.strip().split(",")
    score_numbers = [int(value) for value in score_strings]
    score_values.append(score_numbers)
scores_file.close()
for i in range(len(subjects)):
    print(subjects[i], "Scores:")
    for score in score_values[i]:
        print(score)
    print("Max:", max(score_values[i]))
    print()