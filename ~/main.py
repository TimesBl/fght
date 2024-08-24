from main_window import*
from menu_window import*

from random import choice, shuffle
from time import sleep


class Question():

    def __init__(self, qestion, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.qestion = qestion
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3 

        self.actual = True
        self.attempts = 0
        self.correct = 0

    def got_right(self):
        #"змінює статистику, отримавши правельну відповідь"
        self.attempts += 1
        self.correct += 1
        
    def got_wrong(self):
         #"змінює статистику, отримавши неправельну відповідь"
        self.attempt += 1       

# питання

q1 = Question(" Скільки планет у нашій Сонячній системі?", "8", "7", "9", "10")
q2 = Question("Яка планета найближча до Сонця?", "Меркурій", "Земля", "Венера", "Марс")
q3 = Question("Яка планета найбільша у Сонячній системі?", "Юпітер", "Сатурн", "Земля", "Нептун")
q4 = Question("На якій планеті є кільця?", "Сатурн", "Марс", "Венера", "Земля")
q5 = Question("Яка планета має найбільше супутників?", "Юпітер", "Земля", "Марс", "Венера")
q6 = Question("Яка планета відома як 'червона планета'?", "Марс", "Венера", "Юпітер", "Сатурн")
q7 = Question("Яка планета обертається навколо Сонця найдовше?", "Нептун", "Меркурій", "Земля", "Венера")
q8 = Question("Який об'єкт є карликовою планетою в Сонячній системі?", "Плутон", "Марс", "Земля", "Венера")
q9 = Question("Яка з планет має найбільший нахил осі?", "Уран", "Меркурій", "Юпітер", "Земля")
q10 = Question("Який об'єкт є найбільшим у Сонячній системі?", "Сонце", "Юпітер", "Земля", "Нептун")

# список 
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]                                                                       
question = [q1, q2, q3, q4, q5, q5, q6, q7, q8, q9, q10]

def new_question():
    global cur_question
    cur_question = choice(question)
    lb_Question.setText(cur_question.question)
    lb_Correct.setText(cur_question.answer)

    shuffle(radio_list)

    radio_list[0].setText(cur_question.wrong_answer1)
    radio_list[1].setText(cur_question.wrong_answer2)
    radio_list[2].setText(cur_question.wrong_answer3)
    radio_list[3].setText(cur_question.answer)


def rest():
    main_win.hide()
    n = box_Minutes.value() + 60
    sleep(n)
    main_win.show()


def show_menu():
    menu_wind.show()
    main_win.hide()

def back_menu():
    menu_wind.hide()
    main_win.show()


def clear():
    txt_Qestion.clear()
    txt_Answer.clear()
    txt_Wrong1.clear()
    txt_Wrong2.clear()
    txt_Wrong3.clear()


#підкючення виклику функції

new_question()
btn_Menu.clicked.connect(show_menu)
btn_back.clicked.connect(back_menu)
btn_clear.clicked.connect(clear)
btn_Sleep.clicked.connect(sleep)



main_win.show()
app.exec_()