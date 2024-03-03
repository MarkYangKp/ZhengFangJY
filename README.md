# 开发文档

登录部分使用模拟点击登录，用的DrissionPage，直接用request进行登录目前我不会写。如果有大佬弄出来了，不吝赐教。


## 使用说明
安装需要的包
```bash
pip install -r requirement.txt
```
主程序为：```main.py```

有可能会出现多次“浏览器路径错误，正在重设”，一般会出现2-3次，如果出现多次则有误

**每次打开需要输入学号**

抢课前需要先登录获取必要的登录信息（提前半小时登录都也，信息有效期很久，提前拿避免登录不上），然后再设置需要抢的课的课程号
等到抢课系统开发，即刻执行抢课操作，理论上肯定会比手速快，但系统卡死，可能也请求不上，反复请求几次

有空再加一个等待成功结果，否则反复请求的逻辑。


## 记录说明
课程搜索时要分类搜索(提交一个参数"xkkz_id")，目前不确定是固定还是每个学期动态变化。

- 主修课的 xkkz_id:```11CAEF36B8A73FCEE063B39AC379D771```
- 体育课的 xkkz_id:```0D78C46944313DF8E063B39AC37958FA```
- 素质教育课的 xkkz_id:```0D7878D544F91931E063B39AC37968C1```
- 网络课的 xkkz_id:```0D7A12293C75DDC0E063B39AC3796C6B```

选课提交参数：
"kklxdm": "01",  主修课程 01 体育课06 素质教育10 网络课程11
```json
    "kcmc": "(CSE21200C)算法设计与分析 - 2.0 学分",
    "kch_id": "CSE21200C",
    "jxb_ids": "07fe65079082c0b768f78584227038b43772087b4c70efa9bebc8de45549e2605de4c82757d9a1213b5408d774a3a25cbe32063499a6742c33764eabe3458d75c17d358c77d102323ef5837582e9feb8c3c2295cd7aba8e0e87c5364d177f52abd0d51edc1abf5a60e98db18f40e795d555e4c9436752bcae072046429fae1bf,31b5e5d9ae636c3aa11535c7ebaafb033d3693d9292e2f5467ccf062590a4ec59093af03147cd8d75f9226d0d9cf7fcb978054b3bacf385f23cd8df951ccc61cca78e41bc00cdcdeb8ec2412aacd17b2c5bd9237500941ce37752c7d31a52f36122f7ed4651d900ad12a55c972514f8ac0944d9fc9c916b101e60ae18e37f667",
    "rwlx": "1",
    "rlzlkz": "1",
    "sxbj": "1",
    "kklxdm": "01",  
    "xkkz_id": "11CAEF36B8A73FCEE063B39AC379D771",
    "njdm_id": "2022",
    "zyh_id": "C1A03C102B5141DEE053B39AC3793EA3",
    "xkxnm": "2023",
    "xkxqm": "12",
    "qz": "0"
```
---


搜索课程提交参数：
```json
    "filter_list[0]": "CSE21200C",
    "bklx_id": "0",
    "xqh_id": "2",
    "jg_id": "04",
    "zyh_id": "C1A03C102B5141DEE053B39AC3793EA3",
    "zyfx_id": "wfx",
    "njdm_id": "2022",
    "bh_id": "04202201",
    "xbm": "1",
    "xslbdm": "32",
    "mzm": "06",
    "xz": "4",
    "ccdm": "3",
    "xsbj": "4294967296",
    "xkxnm": "2023",
    "xkxqm": "12",
    "kklxdm": "01",
    "kch_id": "CSE21200C",
    "xkkz_id": "11CAEF36B8A73FCEE063B39AC379D771",
```

返回参数：
```json
[
  {
    "bxbj": "0",
    "date": "二○二四年二月二十九日",
    "dateDigit": "2024年2月29日",
    "dateDigitSeparator": "2024-2-29",
    "day": "29",
    "do_jxb_id": "",
    "fxbj": "0",
    "jgpxzd": "1",
    "jsxx": "2019500055/王坤峰/教授",
    "jxb_id": "",
    "jxbrl": "144",
    "jxdd": "一教A-205",
    "jxms": "--",
    "kclbmc": "专业",
    "kcxzmc": "专业选修",
    "kkxymc": "信息科学与技术学院",
    "listnav": "false",
    "localeKey": "zh_CN",
    "month": "2",
    "pageTotal": 0,
    "pageable": true,
    "queryModel": {
      "currentPage": 1,
      "currentResult": 0,
      "entityOrField": false,
      "limit": 15,
      "offset": 0,
      "pageNo": 0,
      "pageSize": 15,
      "showCount": 10,
      "sorts": [],
      "totalCount": 0,
      "totalPage": 0,
      "totalResult": 0
    },
    "rangeable": true,
    "sksj": "星期六第6-8节{1-9周}",
    "totalResult": "0",
    "userModel": {
      "monitor": false,
      "roleCount": 0,
      "roleKeys": "",
      "roleValues": "",
      "status": 0,
      "usable": false
    },
    "xqh_id": "2",
    "xqumc": "北区",
    "year": "2024",
    "yqmc": "--"
  }
]
```


GET可以拿到的参数：
```json
{
    "pkey": "",
    "kqhjs": "0",
    "shyjsfbt": "0",
    "localeKey": "zh_CN",
    "csrftoken": "",
    "cdTsxx": "-zfsplit-",
    "wjylSfkf": "0",
    "dingdingbj": "",
    "pageNumber": "15",
    "sessionUserKey": "2022040179",
    "gnmkdmKey": "N253512",
    "iskxk": "1",
    "to_kch": "",
    "jzxkf": "0",
    "xkzgmc": "30",
    "xkzgxf": "50",
    "zkcs": "10",
    "zxfs": "18.5",
    "bdzcbj": "2",
    "xkxnm": "2023",
    "xkxqm": "12",
    "xkxnmc": "2023-2024",
    "xkxqmc": "2",
    "xh_id": "2022040179",
    "xqh_id": "2",
    "jg_id_1": "04",
    "zyh_id": "",
    "zymc": "",
    "zyfx_id": "wfx",
    "njdm_id": "2022",
    "njmc": "2022",
    "bh_id": "04202201",
    "xbm": "1",
    "zh": "",
    "xslbdm": "32",
    "mzm": "06",
    "xz": "4",
    "ccdm": "3",
    "xsbj": "",
    "sjhm": "",
    "xszxzt": "1",
    "njdm_id_1": "2022",
    "zyh_id_1": "",
    "sfxsxkbz": "0",
    "sfxskssj": "0",
    "wrljxbbhkg": "0",
    "jxbzbkg": "1",
    "tykpzykg": "0",
    "tkdxyzms": "0",
    "jxbzhkg": "0",
    "xxdm": "10010",
    "xkgwckg": "0",
    "cxkctskg": "0",
    "kxqxktskg": "0",
    "tbtkxqxktskg": "0",
    "xkkczdsqkg": "1",
    "xkmcjzxskcs": "10",
    "xkckctkckg": "",
    "xkbzsyljkg": "0",
    "zzxkgjcxkg_kcz": "0",
    "zzxkgjcxkg_nj": "1",
    "zzxkgjcxkg_xy": "1",
    "zzxkgjcxkg_zy": "1",
    "zzxkgjcxkg_kkxy": "1",
    "zzxkgjcxkg_xqu": "0",
    "zzxkgjcxkg_yqu": "0",
    "zzxkgjcxkg_tjbj": "0",
    "zzxkgjcxkg_kclb": "1",
    "zzxkgjcxkg_kcxz": "1",
    "zzxkgjcxkg_jxms": "1",
    "zzxkgjcxkg_kcgs": "1",
    "zzxkgjcxkg_skxq": "1",
    "zzxkgjcxkg_skjc": "1",
    "zzxkgjcxkg_jxb": "1",
    "zzxkgjcxkg_sfcx": "1",
    "zzxkgjcxkg_ywyl": "1",
    "zzxkgjcxkg_sksjct": "0",
    "xkczbj": "1",
    "isSlct": "0",
    "kklxdm": "",
    "kklxmc": "",
    "xkkz_id": "",
    "jxbzb": "",
    "firstKklxdm": "01",
    "firstKklxmc": "",
    "firstXkkzId": "",
    "firstNjdmId": "2022",
    "firstZyhId": ""
}
```
全校课表提交参数：
```json
    "xnm": "2023",
    "xqm": "12",
    "kc": "",
    "_search": "false",
    "nd": "",
    "queryModel.showCount": "15",
    "queryModel.currentPage": "1",
    "queryModel.sortName": "",
    "queryModel.sortOrder": "asc"
```
