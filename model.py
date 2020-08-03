questions_ans = {'question_1': 'India', 'question_2':'West Bengal', 'question_3': 'Python', 'question_4':'Tableau'}
def ans(val1, val2, val3, val4):
    num = 0
    if val1 == questions_ans['question_1']:
        num += 1
    if val2 == questions_ans['question_2']:
        num += 1
    if val3 == questions_ans['question_3']:
        num += 1
    if val4 == questions_ans['question_4']:
        num += 1
    if num >= 3:
        return 'You are Eligible'
    else:
        return 'Sorry, You are not eligible'
if __name__ == "__main__":
    print(ans('India', 'West Bengal', 'Python', 'Seaborn'))