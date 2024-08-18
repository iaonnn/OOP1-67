#Juthamas 000

# Function ฟังก์ชัน

"""
รูปแบบของฟังก์ชัน



def ชื่อของฟังก์ชัน(ตัวแปร):
    สิ่งที่เราอยากให้ฟังก์ชันทำงาน


print("Happy Birthday to you")
print("Happy Birthday to you")
print("Happy Birthday Happy Birthday")
print("Happy Birthday to you")

print("Happy Birthday to you")
print("Happy Birthday to you")
print("Happy Birthday Happy Birthday")
print("Happy Birthday to you")

print("Happy Birthday to you")
print("Happy Birthday to you")
print("Happy Birthday Happy Birthday")
print("Happy Birthday to you")
"""

#ฟังก์ชันแบบไม่มีตัวแปร
def HBD():
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print("Happy Birthday Happy Birthday")
    print("Happy Birthday to you")

#HBD()
#HBD()
#HBD()

#ฟังก์ชันแบบมีตัวแปร
#ตัวแปรเดียว
def HBD2(name):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday  to {name}")
    print("Happy Birthday to you")

#HBD2("Juthamas")
#HBD2("AON")
#HBD2("COMPUTER")

#ฟังก์ชันแบบมีตัวแปร
#ตัวแปรหลายตัว
"""def juthamas(name,sur,room,no):
    print(f"My name is {name}")
    print(f"My surname is {sur}")
    print(f"My room is {room}")
    print(f"My no is {no}")

juthamas("Juthamas","Sangeumrum","3/1","000")
"""
#รับ input ทาง keyboard
"""#ฟังก์ชัน
def juthamas2(name,sur,room,no):
    print(f"My name is {name}")
    print(f"My surname is {sur}")
    print(f"My room is {room}")
    print(f"My no is {no}")

#input รับค่า
w = input("What's your name? : ")
x = input("What's your surname? : ")
y = input("What's your room? : ")
z = input("What's your no? : ")

#เรียกใช้ฟังก์ชัน
juthamas2(w,x,y,z)"""


#โปรแกรมหาพื้นที่สี่เหลี่ยม
#สูตร กว้างxยาว
#ฟังก์ชัน
def juthamas2(a,b):
    print(f"ขนาดความกว้างคือ {a}")
    print(f"ขนาดความยาวคือ {b}")
    print("พื้นที่ของสี่เหลี่ยมคือ",a*b)

#input รับค่า
w = int(input("ความกว้่างของสี่เหลี่ยม : "))
h = int(input("ความยาวของสี่เหลี่ยม : "))

#เรียกใช้ฟังก์ชัน
juthamas2(w,h)

#----------------------------------------

