import requests


def GetMyScore(JSESSIONID,lb):
        try:
            url = 'https://jwglxt-proxy4.buct.edu.cn/jwglxt/cjcx/cjcx_cxXsgrcj.html?doType=query&gnmkdm=N305005'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
                'Referer': 'https://jwglxt-proxy4.buct.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default',
                "Cookie": "JSESSIONID="+JSESSIONID+";lb="+lb
            }

            data = {
                "xnm": "2023",
                "xqm": "3",
                "kcbj": "",
                "_search": "false",
                # "nd": "1705146134475",
                "queryModel.showCount": "15",
                "queryModel.currentPage": "1",
                "queryModel.sortName": "",
                "queryModel.sortOrder": "asc",
                "time": "0"
            }

            response = requests.post(url, headers=headers, data=data)
            print(response.status_code)
            # print(response.json())

            return response.json()
        except:
            return -1