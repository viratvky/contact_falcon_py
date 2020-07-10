import psycopg2
from faker import Faker
import random,string
connection = psycopg2.connect(host=’localhost’, database=’contact_api’, user=’vicky', password=’vicky@123')
cursor = connection.cursor()
fake=Faker()
for i in range(1,10):
 Contact_person=fake.name()
 Contact_number=int(‘’.join(random.choice(string.digits) for _ in range(10)))
 Contact_emailId=fake.email()
 cursor.execute(‘Insert into contact ("Contact_person”,”Contact_number”,”Contact_emailId”) VALUES (%s,%s,%s)’,(Contact_person,Contact_number,Contact_emailId))
 connection.commit()
if id==1:
    
    Contact_person=input("name")
    Contact_number=input("number")
    Contact_emailId=input("mail")
    cursor.execute(‘Insert into contact ("Contact_person”,”Contact_number”,”Contact_emailId”) VALUES (%s,%s,%s)’,(Contact_person,Contact_number,Contact_emailId))
if id==2:
    name=input("name")
    cursor.execute(‘DELETE FROM `contact` [contact_person==name]')
    Contact_person=input("update name")
    Contact_number=input("update number")
    Contact_emailId=input("update mail")
    cursor.execute(‘Insert into contact ("Contact_person”,”Contact_number”,”Contact_emailId”) VALUES (%s,%s,%s)’,(Contact_person,Contact_number,Contact_emailId))
if id==3:
    name=input("name")
    cursor.execute(‘DELETE FROM `contact` [contact_person==name]')
if id==4:
    name=input()
    cursor.execute(‘select * from contact where name==contact_person')

