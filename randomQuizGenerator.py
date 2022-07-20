import random
i = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10','11':'11','12':'12','13':'13','14':'14','15':'15','16':'16','17':'17','18':'18','19':'19','20':'20','21':'21','22':'22','23':'23','24':'24','25':'25','26':'26','27':'27','28':'28','29':'29','30':'30','31':'31','32':'32','33':'33','34':'34','35':'35'}
for quizNum in range(35):
    file = open(f'capitalsquiz{quizNum+1}.txt','w')
    answerFile = open(f'capitalsquiz_answers{quizNum+1}.txt','w')
    file.write(f'Name:\nDate:\nPeriod:\nState Capitals Quiz(Form{quizNum+1})\n')
    
    j = list(i.keys())
    random.shuffle(j)
    
    for questionNum in range(35):
        correctAnswer = i[j[questionNum]]
        wrongAnswer = list(i.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer,3)
        options = [correctAnswer] + wrongAnswer
        random.shuffle(options)
        
        file.write(f'{questionNum + 1}.{j[questionNum]}\n')
        for I in range(4):
            file.write(f"{'ABCD'[I]}.{options[I]}\n")
        file.write('\n')
        answerFile.write(f"{questionNum+1}.{'ABCD'[options.index(correctAnswer)]}\n")
    file.close()
    answerFile.close
    