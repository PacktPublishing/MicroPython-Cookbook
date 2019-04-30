import os


def get_questions():
    paths = sorted(os.listdir())
    return [i for i in paths if i.endswith('question.bmp')]


def main():
    questions = get_questions()
    for question in questions:
        response = question.replace('question.bmp', 'response.bmp')
        print(question, response)


main()
