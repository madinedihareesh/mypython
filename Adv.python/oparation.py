import os
import time
import csv
import pprint

# print(os.path.exists('/Users/pjangala/Desktop/python.jpeg'))
# print(os.name)
# print(os.path.isdir('/Users/pjangala/Desktop'))
# print(os.path.split('/Users/pjangala/Desktop/python.jpeg'))
# print(os.path.join('/Users/pjangala/Desktop','python.jpeg'))
# print(time.ctime(os.path.getmtime('/Users/pjangala/Desktop/python.jpeg')))
# print(time.ctime(os.path.getctime('/Users/pjangala/Desktop/python.jpeg')))
# print(time.ctime(os.path.getatime('/Users/pjangala/Desktop/python.jpeg')))
# print(os.path.abspath('../../Desktop/python.py'))
# os.mkdir('/Users/pjangala/Desktop/Grand')
# os.rmdir('/Users/pjangala/Desktop/Grand')
# os.makedirs('/Users/pjangala/Desktop/Grand/Parent/Child')
# os.removedirs('/Users/pjangala/Desktop/Grand/Parent/Child')
# os.rmdir('/Users/pjangala/Desktop/Grand')
# os.remove('/Users/pjangala/Desktop/python.jpeg')

with open('/Users/pjangala/Desktop/students.csv','r') as f:
        data=csv.DictReader(f)
        dic={}
        for row in data:
            dic[row['stu_name']]=row

        pprint.pprint(dic)
        pprint.pprint(dic['amardeep']['stu_email'])    