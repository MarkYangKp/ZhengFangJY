from DrissionPage import ChromiumPage, ChromiumOptions
import time as T
import json
import requests

def SetPath():
    path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'  # 请改为你电脑内Chrome可执行文件路径
    ChromiumOptions().set_browser_path(path).save()
# 获取JSESSIONID
def login(ids,password):
    
    try:
        co = ChromiumOptions()
        co = co.headless(True)  # 解决浏览器无法连接报错
        page = ChromiumPage(co)
        page.clear_cache()
        page.get("https://jwglxt.buct.edu.cn")
    except:
        print("路径错误，正在重新设置")
        SetPath()
        return
    # print(page.html)
    T.sleep(5)
    page.ele("#username").input(str(ids))
    page.ele("#password").input(str(password))
    print("已填写账号密码")
    T.sleep(1)
    page.ele(".btn").click()
    print("正在登陆.....")
    T.sleep(2)
    
    lb =page.get_cookies(as_dict=False)[0]['value'] 
    JSESSIONID = page.get_cookies(as_dict=False)[1]['value']
    # print("已获取session数据")
    page.quit()
    # print("模拟操作退出。。")
    with open('data\\session.json', 'r') as file:
        datas = json.load(file)
    
    data = {
        'id':ids,
        'password':password,
        'lb':lb,
        'JSESSIONID':JSESSIONID
    }
    isExist = False
    i = 0
    for item in datas:

        if(item['id'] == ids):
            # print(item)
            datas[i] = data
            item = data
            isExist = True

        i+=1
    
    if isExist == False:
        datas.append(data)
    # print(datas)
    # 读取session.json文件
    with open('data\\session.json', 'w') as file:
        file.write(json.dumps(datas))
        # json.dump(datas,file)
    print("登录成功，获取到必要信息")
    return data
    # except:
        # return -1


