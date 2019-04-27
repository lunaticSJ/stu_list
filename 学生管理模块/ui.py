from bll import StudentManagerController
from models import StudentModel
class StudentManagerView:
    """
        学生管理器视图类
    """
    def __init__(self):
        # 创建学生管理控制器对象
        self.__controller = StudentManagerController()


    def __display_menu(self):
        """
            显示菜单
        :return:
        """
        print("---------------------")
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩降序显示")
        print("---------------------")

    def __select_menu(self):
        """
            选择菜单
        :return:
        """
        number = input("请输入选项：")
        if number == "1":
            self.input_student()
        elif number =="2":
            self.__out_put_students(self.__controller.list_stu)
        elif number == "3":
            self.del_student()
        elif number == "4":
            self.xiugai_student()
        elif number == "5":
            self.order_score()

    def main(self):
        """
            学生管理器入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()
    def input_student(self):
        while True:
            stu = StudentModel()
            stu.name = input("请输入姓名")
            stu.age = int(input("请输入年龄"))
            stu.score = int(input("请输入成绩"))
            self.__controller.add_student(stu)
            if input("按Y继续") != "Y":
                break

    def __out_put_students(self,list_stu):
        for item in list_stu:
            print("%d|%s|%d|%d "%(item.id,item.name,item.age,item.score))


    def del_student(self):
        while True:
            stu = StudentModel()
            Num = int(input("请输入ID："))
            self.__controller.remove_student(Num)
            if input("按Y继续") != "Y":
                break


    def xiugai_student(self):
            stu_info = StudentModel()
            stu_info.id=int(input("请输入你要修改的Id："))
            stu_info.name= str(input("请输入你要修改的名字："))
            stu_info.age= int(input("请输入你要修改的年纪："))
            stu_info.score=(int(input("请输入你要修改的分数：")))
            if self.__controller.update_student(stu_info):
                print("修改成功")
            else:
                print("修改失败")


    # def  order_score(self):
    #         result = self.__controller.order_by_score()
    #         self.__out_put_students(result)
    #
    # def save_stu(self):
