class School_jur:
    def __init__(self, student, subject):
        self.student  = student 
        self.subject  = subject 
        self.grade_list  = [] 

    def grade(self, otsen):
        self.grade_list.append(int(otsen))


    def printer(self):
        print("Имя ученика:", self.student)
        print("Предмет:", self.subject)
        print("Оценки:", self.grade_list)

    def final_grade(self):
        sr = 0
        for i in range(len(self.grade_list )):
            sr += self.grade_list[i]
        sr = sr / int(len(self.grade_list ))
        print("Средний бал: ", sr)

schoolJournal = School_jur("Alex", "Math")

while True:
    ot = int(input("Введите оценку (Если хотите закончить 0):"))
    if ot == 0:
        break
    schoolJournal.grade(ot)
    
schoolJournal.printer()   
schoolJournal.final_grade()