import csv
from xml.dom import minidom

#读取本地csv文件
#data = csv.reader(open('./data/info.csv','r'))
#循环输出每一行信息
#for user in data:
#    print(user)
#    print(user[0])
#读取本地txt文件
user_file = open('./data/user_info.txt','r')
#lines = user_file.readlines()
#for line in lines:
#    username = line.split(',')[0]
#    password = line.split(',')[1]
#    print(username,password)
#将文本信息处理为字典列表
#info = []
#for line in user_file:
#    result = [ele.strip() for ele in line.split(',')]
#    print(result)
#    ele = {}
#    for r in result:
#        eledict = [element.strip() for element in r.split('=')]
#        #print(eledict)
#        ele.update(dict([eledict]))
#    info.append(ele)
#print(info[0].keys())
#打开xml文档
dom = minidom.parse('./data/info.xml')
root = dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print(root.ELEMENT_NODE)
#获得任意标签名
tagname = root.getElementsByTagName('browser')
print(tagname[0].tagName)
tagname = root.getElementsByTagName('login')
print(tagname[1].tagName)
tagname = root.getElementsByTagName('province')
print(tagname[2].tagName)
#获得标签属性值
logins = root.getElementsByTagName('login')
# 获得 login 标签的 username 属性值
username = logins[0].getAttribute("username")
print(username)
# 获得 login 标签的 password 属性值
password = logins[0].getAttribute("password")
print(password)
# 获得第二个 login 标签的 username 属性值
username = logins[1].getAttribute("username")
print(username)
# 获得第二个 login 标签的 password 属性值
password = logins[1].getAttribute("password")
print(password)
#获得标签对之间的数据
provinces = dom.getElementsByTagName('province')
citys = dom.getElementsByTagName('city')
# 获得第二个 province 标签对的值
p2 = provinces[1].firstChild.data
print(p2)
# 获得第一个 city 标签对的值
c1 = citys[0].firstChild.data
print(c1)
# 获得第二个 city 标签对的值
c2 = citys[1].firstChild.data
print(c2)