from GetCourse import Course
from Login import login
import json
from DrissionPage import ChromiumOptions

# 抢课脚本使用说明
# 需要提前登录获取JSESSIONID 和 lb
# 系统开放后直接执行抢课 前提是登陆信息是有效的

courseList = []

xh_id = ""
def Login():
    global xh_id
    # xh_id = input("学号:")
    psw = input("密码:")
    login(xh_id,psw)
    
def CheckCourse():
    global courseList
    kclb = int(input("课程类别(主修课 0 体育课 1 素质教育课 2 网络课程 3)"))
    kch = input("请输入需要抢的课程的课程号:")
    course = Course(kclb,kch,xh_id)
    with open('data\\session.json', 'r') as file:
        datas = json.load(file) 
    # print(datas)
    course.SetLoginInfo(datas)
    courseList.append(course)
# 抢课
def GetCourse():
    if courseList != []:
        for item in courseList:

            item.CheckCourse()
    else:
        print("未添加目标课程")

def ShowCourseList():
    if courseList == []:
        print("未添加目标课程")
        print("***************************")
        return
    i = 0
    print("已选择课程如下:")
    for item in courseList:
        print(str(i+1)+"."+item.kch)
    print("***************************")

def main():
    global courseList
    while True:
        print("指令:")
        print("1:登陆获取必要信息 2:添加目标课程 3:抢课 4:查看已添加的目标课程 5:清空目标课程 exit:退出程序" )
        cmd = input("请输入指令:")
        if cmd == "1":
            Login()
        elif cmd == "2":
            CheckCourse()
        elif cmd == "3":
            GetCourse()
        elif cmd == "4":
            ShowCourseList()
        elif cmd == "5":
            courseList = []
        elif cmd == "exit":
            break


if __name__ == "__main__":
    xh_id = input("请输入你的学号:")
    print("********************************************")
    print("抢课脚本使用说明")
    print("需要提前登录获取JSESSIONID 和 lb")
    print("系统开放后直接执行抢课 前提是登陆信息是有效的")
    print("********************************************")
    main()

