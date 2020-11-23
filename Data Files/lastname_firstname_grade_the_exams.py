import pandas as pd
import numpy as np


def openfile():
    while True:
        try:
            # Task1:
            file_name = str(input('Enter a class file to grade (i.e. class1 for class1.txt):'))
            file_name = 'Data Files/' + file_name + '.txt'
            data = pd.read_csv(file_name, header=None)
            print('Successfully opened class1.txt')
            list_answer = data.to_numpy(dtype="object")
            # Task2:
            answer_key = np.array(
                ['B', 'A', 'D', 'D', 'C', 'B', 'D', 'A', 'C', 'C', 'D', 'B', 'A', 'B', 'A', 'C', 'B', 'D', 'A', 'C',
                 'A', 'A', 'B', 'D', 'D'])
            list_score = np.array([])
            dict_score = {}
            valid_line = 0
            for i in range(len(list_answer)):
                if len(list_answer[i][0]) != 9 or list_answer[i][0][0] != 'N':
                    print("N# is invalid at row", i + 1, list_answer[i])
                elif len(list_answer[i]) != 26:
                    print('Invalid line of data at row ', i + 1, ": Does not contain exactly 26 values:",
                          list_answer[i])
                else:
                    valid_line += 1
                    score = 0
                    for j in range(len(answer_key) - 1):
                        if list_answer[i][j + 1] == answer_key[j]:
                            score = score+4
                        elif list_answer[i][j + 1] == '':
                            score = score
                        # Task3
                        else:
                            score = score-1
                    list_score = np.append(list_score, score)
                    dict_score[list_answer[i][0]] = score
            print('****', 'REPORT', '****')
            print("Total valid lines of data:", valid_line, '/', len(list_answer))
            print("Total invalid lines of data:", len(list_answer) - valid_line, '/', len(list_answer))
            print("The average score:", np.mean(list_score))
            print("The highest score:", np.max(list_score))
            print("The lowest score:", np.min(list_score))
            print("The range of scores:", np.max(list_score) - np.min(list_score))
            print("The meadian of score:", np.median(list_score))
            # Task4
            result = open(file_name + "_grades", "w")
            for k, v in dict_score.items():
                result.write(str(k) + ',' + str(v) + '\n\n')
            print("File's created success!")
            result.close()
            break
        except FileNotFoundError as fnf:
            print('File cannot be found.')
            print(fnf)


openfile()
