from models import StudentModel
import os
FILE_PATH = "stu.txt"
class TextDao:
    @staticmethod
    def save_stu(list_stu):
        with open(FILE_PATH, "w", encoding="utf-8") as stu_file:
            for stu in list_stu:
                stu_file.write(stu.__repr__() + "\n")

    @staticmethod
    def load_stu():
        list_stu = []
        if not os.path.isfile(FILE_PATH):
            return  list_stu

        with open(FILE_PATH, "r", encoding="utf-8") as stu_file:
            for line in stu_file:
                stu = eval(line)
                list_stu.append(stu)
        return list_stu
