import requests
import json
from bs4 import BeautifulSoup

class Course:
    JSESSIONID=""
    lb = ""

    # 课程类别 0 1 2 3
    kclb = 0

    #学号
    xh_id = ""


    jxbzls = "1"
    jxb_id = ""
    jxb_ids = ""
    #公共参数
    zyh_id = ""
    njdm_id = ""
    xkxnm = ""
    xkxqm = ""
    kklxdm = "01" # 主修课程 01 体育课 06 素质教育 10 网络课程 11
    xkkz_id= ""
    kch_id=""

    

    # 选课提交参数
    # kch_id = ""
    
    rwlx = ""
    rlzlkz = ""
    sxbj = ""
    qz = "0"

    # 搜索课程提交参数
    filter_list=""
    bklx_id= ""
    xqh_id=""
    jg_id= ""
    # zyh_id= ""
    zyfx_id= ""
    # njdm_id= ""
    bh_id=""
    xbm=""
    xslbdm= ""
    mzm=""
    xz=""
    ccdm= ""
    xsbj=""
    # xkxnm=""
    # # xkxqm= ""
    # kklxdm= ""

    bj = "7"

    xkkz_id0 = "11CAEF36B8A73FCEE063B39AC379D771"
    xkkz_id1 = "0D78C46944313DF8E063B39AC37958FA"
    xkkz_id2 = "0D7878D544F91931E063B39AC37968C1"
    xkkz_id3 = "0D7A12293C75DDC0E063B39AC3796C6B"
    def __init__(self,kclb,kch,xh_id):
        self.kclb = kclb
        # self.kklxdm = kklxdm
        self.kch = kch
        self.xh_id = xh_id

        if(self.kclb == 0):
            self.xkkz_id = self.xkkz_id0
            self.kklxdm = "01"
        elif(self.kclb == 1):
            self.xkkz_id = self.xkkz_id1
            self.kklxdm = "06"
        elif(self.kclb == 2):
            self.xkkz_id = self.xkkz_id2
            self.kklxdm - "10"
        elif(self.kclb == 3):
            self.xkkz_id = self.xkkz_id3
            self.kklxdm = "11"
        
    # 设置登录信息
    def SetLoginInfo(self,datas):
        # with open('session.json', 'r') as file:
        #     datas = json.load(file) 
        # print(datas)
        for item in datas:
            if(item['id'] == self.xh_id):
                self.JSESSIONID = item['JSESSIONID']
                self.lb = item['lb']
    
    # 获取个人信息1
    def GetInfo1(self):
        url = "https://jwglxt-proxy4.buct.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default"

        headers = {
            "Cookie": "JSESSIONID="+self.JSESSIONID+"; _ga=GA1.1.197118017.1688103849; _ga_7YS8WBPT93=GS1.1.1704544198.96.1.1704545856.0.0.0; lb="+self.lb
        }

        response = requests.get(url, headers=headers,verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        input_tags = soup.find_all('input')

        input_dict = {}

        for tag in input_tags:
            input_id = tag.get('id')
            input_value = tag.get('value')
            if input_id is not None and input_value is not None:
                input_dict[input_id] = input_value

        return input_dict
    
    # 获取个人信息2
    def GetInfo2(self):
        url = "https://jwglxt-proxy4.buct.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbDisplay.html?gnmkdm=N253512"

        headers = {
            "Cookie": "JSESSIONID="+self.JSESSIONID+"; _ga=GA1.1.197118017.1688103849; _ga_7YS8WBPT93=GS1.1.1704544198.96.1.1704545856.0.0.0; lb="+self.lb
        }

        data = {
            "xkkz_id": self.xkkz_id,
            "xszxzt": "1",
            "kspage": "0",
            "jspage": "0"
        }

        response = requests.post(url, headers=headers, data=data,verify=False)

        soup = BeautifulSoup(response.text, 'html.parser')
        input_tags = soup.find_all('input')

        input_dict = {}

        for tag in input_tags:
            input_id = tag.get('id')
            input_value = tag.get('value')
            if input_id is not None and input_value is not None:
                input_dict[input_id] = input_value
        return input_dict

    # 设置个人信息
    def SetInfo(self):
        Info1 = self.GetInfo1()
        Info2 = self.GetInfo2()
        self.zyh_id = Info1['zyh_id']
        self.njdm_id = Info1['njdm_id']
        self.xkxnm = Info1['xkxnm']
        self.xkxqm = Info1['xkxqm']
        # self.kklxdm = Info1['kklxdm']

        self.rwlx = Info2['rwlx']
        self.rlzlkz = Info2['rlzlkz']
        self.bklx_id = Info2['bklx_id']
        self.xkxskcgskg = Info2['xkxskcgskg']
        self.xkly = Info2['xkly']

        self.sxbj = "1"
        self.xqh_id = Info1['xqh_id']
        self.jg_id = Info1['jg_id_1']
        self.zyfx_id = Info1['zyfx_id']
        self.bh_id = Info1['bh_id']
        self.xbm = Info1['xbm']
        self.xslbdm = Info1['xslbdm']
        self.mzm = Info1['mzm']
        self.xz = Info1['xz']
        self.ccdm = Info1['ccdm']
        self.xsbj = Info1['xsbj']

    # 获取课程信息
    def GetCourseInfo(self):
        url = "https://jwglxt-proxy4.buct.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbPartDisplay.html?gnmkdm=N253512"

        headers = {
            "Cookie": "JSESSIONID="+self.JSESSIONID+"; _ga=GA1.1.197118017.1688103849; _ga_7YS8WBPT93=GS1.1.1704544198.96.1.1704545856.0.0.0; lb="+self.lb
        }

        data = {
            "filter_list[0]": self.kch,
            "rwlx": self.rwlx,
            "bklx_id": self.bklx_id,
            "xqh_id": self.xqh_id,
            "jg_id": self.jg_id,
            "njdm_id_1": self.njdm_id,
            "zyh_id_1": self.zyh_id,
            "zyh_id": self.zyh_id,
            "zyfx_id": self.zyfx_id,
            "njdm_id": self.njdm_id,
            "bh_id": self.bh_id,
            "xbm": self.xbm,
            "xslbdm": self.xslbdm,
            "mzm": self.mzm,
            "xz": self.xz,
            "ccdm": self.ccdm,
            "xsbj": self.xsbj,
            "xkxnm":self.xkxnm,
            "xkxqm": self.xkxqm,
            "kklxdm": self.kklxdm,
            "kspage": "1",
            "jspage": "10",
        }

        response = requests.post(url, headers=headers, data=data,verify=False)
        # print(response.json())
        self.kch_id = response.json()['tmpList'][0]['kch_id']
        self.jxbzls = response.json()['tmpList'][0]['jxbzls']
        self.jxb_id = response.json()['tmpList'][0]['jxb_id']

        # print(response.text)

    #获取课程的jxb_ids
    def GetCourseJxb_ids(self):
        url = "https://jwglxt-proxy4.buct.edu.cn/jwglxt/xsxk/zzxkyzbjk_cxJxbWithKchZzxkYzb.html?gnmkdm=N253512"
        headers = {
            "Cookie": "JSESSIONID="+self.JSESSIONID+"; _ga=GA1.1.197118017.1688103849; _ga_7YS8WBPT93=GS1.1.1704544198.96.1.1704545856.0.0.0; lb="+self.lb
        }
        data = {
            "filter_list[0]": self.kch,
            "rwlx": self.rwlx,  
            "bklx_id": self.bklx_id,
            "xqh_id": self.xqh_id,
            "jg_id": self.jg_id,
            "zyh_id": self.zyh_id,
            "zyfx_id": self.zyfx_id,
            "njdm_id": self.njdm_id,
            "bh_id": self.bh_id,
            "xbm": self.xbm,
            "xslbdm": self.xslbdm,
            "mzm": self.mzm,
            "xz": self.xz,
            "ccdm": self.ccdm,
            "xsbj": self.xsbj,
            "xkxnm":self.xkxnm,
            "xkxqm": self.xkxqm,
            "xkxskcgskg":self.xkxskcgskg,
            "kklxdm": self.kklxdm,
            "kch_id": self.kch_id,
            "xkkz_id": self.xkkz_id,
        }

        response = requests.post(url, headers=headers, data=data,verify=False)
        
        courseData = response.json()
        # print("223:")
        # print(courseData)
        for item in courseData:
            if(item['jxb_id']==self.jxb_id):
                self.jxb_ids = item['do_jxb_id']
                # self.jxb_id = item['jxb_id']
        # return jsondata
    # SearchCourse(1,1,1,1,1)
    
    # 未知请求
    def UnknownRequest(self):
        url = "https://jwglxt-proxy4.buct.edu.cn/jwglxt/xsxk/zzxkyzb_cxXkTitleMsg.html?gnmkdm=N253512"

        headers = {
            "Cookie": "JSESSIONID="+self.JSESSIONID+"; _ga=GA1.1.197118017.1688103849; _ga_7YS8WBPT93=GS1.1.1704544198.96.1.1704545856.0.0.0; lb="+self.lb
        }

        data = {
            "jxb_ids":self.jxb_ids,
            "xkxnm": self.xkxnm,
            "xkxqm": self.xkxqm,
            "bj": self.bj,
            "kch_id": self.kch_id,
            "njdm_id": self.njdm_id,
            "zyh_id": self.zyh_id,
            "kklxdm": self.kklxdm
        }

        response = requests.post(url, headers=headers, data=data,verify=False)

        # print("266:"+response.text)
    # 获取实验教学班的信息
    def GetClassInfo(self):
        self.UnknownRequest()
        url = "https://jwglxt-proxy4.buct.edu.cn/jwglxt/xsxk/zzxkyzb_xkZyDisplayZzxkYzbZjxb.html?gnmkdm=N253512"
        headers = {
            "Cookie": "JSESSIONID="+self.JSESSIONID+"; _ga=GA1.1.197118017.1688103849; _ga_7YS8WBPT93=GS1.1.1704544198.96.1.1704545856.0.0.0; lb="+self.lb
        } 
        # print(self.jxb_ids)
        data = {
            "xkxnm": self.xkxnm,
            "xkxqm": self.xkxqm,
            "xkly": self.xkly,
            "jxb_id": self.jxb_ids,
            "jxbzls": self.jxbzls,
            # "rlkz": "1",
            "rlzlkz": self.rlzlkz,
            "rwlx": self.rwlx,
            "syqz": "100",
            "zyfx_id": self.zyfx_id,
            "bh_id": self.bh_id,
            "zyh_id": self.zyh_id,
            "njdm_id": self.njdm_id,
            "kklxdm": self.kklxdm,
            "xh_id": self.xh_id,
        }

        response = requests.post(url, headers=headers, data=data,verify=False)
        # print("310:"+response.text)
        cdata = response.json()

        
        self.jxb_ids = cdata[0]['do_jxb_id']+","+cdata[1]['do_jxb_id']
        # print(response.text)
    # 检测参数获取情况
    def CheckOut(self):
        for item in dir(self):
            if not item.startswith("__") and not item.endswith("__"):
                # 获取属性或方法的值
                attr_value = getattr(self, item)
                # if(attr_value==""):
                print(f"Attribute/Method Name: {item}, Value: {attr_value}")
    # 选课
    def CheckCourse(self):
        self.SetInfo()
        # self.SetLoginInfo()
        self.GetCourseInfo()
        self.GetCourseJxb_ids()
        # print("实验课是否开设："+self.jxbzls)
        if(self.jxbzls!="1"):
            self.GetClassInfo()

        url = "https://jwglxt-proxy4.buct.edu.cn/jwglxt/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512"

        headers = {
            "Cookie": "JSESSIONID="+self.JSESSIONID+"; _ga=GA1.1.197118017.1688103849; _ga_7YS8WBPT93=GS1.1.1704544198.96.1.1704545856.0.0.0; lb="+self.lb
        }

        data = {
            
            "kch_id": self.kch_id,
            "jxb_ids": self.jxb_ids,
            "rwlx": self.rwlx,
            "rlzlkz": self.rlzlkz,
            "sxbj": self.sxbj,
            "kklxdm": self.kklxdm,  # 主修课程 01 体育课06 素质教育10 网络课程11
            "xkkz_id": self.xkkz_id,
            "njdm_id": self.njdm_id,
            "zyh_id": self.zyh_id,
            "xkxnm": self.xkxnm,
            "xkxqm": self.xkxqm,
            "qz": self.qz
        }

        response = requests.post(url, headers=headers, data=data,verify=False)

        if(response.json()['flag']=="1"):
            print(self.kch + "抢课成功!!!")
        else:
            print(self.kch + "抢课失败")
        # print(response.text)
    


# course = Course(0,"CSE21200C","2022040179")

# course.CheckOut()
# course.CheckCourse()
