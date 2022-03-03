# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:27:59 2021

@author: Gowtham S
"""

variable = 10

x = 2.5

name = "Gowtham"

letter = 'G'


y = x
#What is the value of y?

# Comments
#What is a comment??

# This is single line comment

"""
This is 
a multi line
comment
"""

# Variables

name = "ggg"

#na me = "gowtham"
# No Spaces allowed

#2name = "gwowtha"
# No start with 2

name2 = "whatevre"

na-me = 50
# Not allowed use any characters

na_me = 50

# Types/ways

my_name = "g" # snake case
myName = "g"  # camel case
MyName = "g"  # Pascal Case


# Arithmetic
# +, -, *, /, %, //, **

x = 10
y = 5

x+y

x/y

x//y # Floor Division

x**y # ?? Exponent

"""
10 to the power of 5




My Assignment - 1.0
1. 10, 1, 8, 3, 6, 5, 4, 7, x, y
   Find general solution of x and y?
   Write an algorithm for the same

2. Check out floor division with 3 different values

3. Revise all that has been taken

Instructions:
1. Upload the above assignment in GitHub with
    a different repository name, example: Python
2. Dont worry about submission now.

Doubts on uploading to github - watch the first live session


Deadline:
3rd of January 2022 for MyCaptain App assignments

Review timing - 11 pm to 1 am every night mostly



Priority:

1. Live Sessions
2. Assignments given in Live sessions
3. Assignments in the app

Suggestion - 1 to 2 hrs a day
"""

x = 2
y = 5

y ** x


# Assignment Operators
# =

x = 2
"""
the value of 2 is taken by x
so x stands for 2
"""
y = 10

x += 2
x = x + 2
"""
x += 2
or
x -= 2
Do not use this in programming
"""



# Comparison operators
# <, >, <=, >=, !=,==

a = 2
x = 2

x == a

x != a
"""
2 and 2 are same, 
"""

# Logical Operator
# and, or, not

x = 5
y = 6

x == y and x != y


# Type Casting / Type Conversion

x = 2
"""
y to have the value of x in float
"""

y = float(x)

"""
what is the floating/float form of 2 ?
"""

y = 2.6

x = int(y)

name = "g"

int(name)

name = "1"

int(name)





# Print

print("Hello World")

x = 2
print("The value of x is ",x)


# Input


a = int(input("Pls enter value of a: "))


answer = a + 2
print(answer)


"""
Assignment 1.1
1. Try out other two logic operators
2. Try out other Comparison operators
3. Complete the first part of the first assignment
    in the app (find area of a circle)

first assignment has two parts:
    1. Area of circle
    2. Getting the file extension

DO NOT SUBMIT THEM YET
DO NOT EVEN THINK ABOUT SUBMISSION YET
JUST COMPLETE THEM
"""















"""
1. It is ok to use Google
2. BUT do not copy and paste the code - Type it
3. Make necessary changes
4. Contact me
5. Answers wont be direct
"""

# if conditions
"""
Turing Complete Code means ??
Turing ??
Imitation Games - movie - Alan Turing is the inventor

Cryptography - encrypting a data

Captcha ?? - I am Not robot
Turing test

Turing Complete - A Programming language
that can induce logic
1. If conditions
2. Loops
"""

"""
If it rains then I will take an Umbrella
"""

rains = 0

if rains == 1:
    print("Take an Umbrella")

"""
If it rains then I will take an Umbrella
"""

"""
If it rains then I will take an Umbrella
Else I will Not take an Umbrella
"""

rains = 0
if rains == 1:
    print("Take an Umbrella")
else:
    print("Will not take an Umbrella")

"""
If it rains then I will take an Umbrella
Else If it snows I will wear boots
Else I will Not take an Umbrella Or Boots
"""

rains = 0
snows = 0

if rains == 1:
    print("TAU")
elif snows == 1:
    print("Wear Boots")
else:
    print("WNTAUOB")





# Functions
# User-Defined 

def addition(a, b):
    print(a+b)

addition(1, 2)

addition(105, 55)

"""
Assignment 1.2
1. Build a calculator using if-conditions and Functions
Sample:
Enter value: 1, 3
1. Add
2. Subtraction
...

Enter Choice: 1
4

Complete Creative freedom

2. Create a function with 3 and 4 parameters

Submission:
1. Upload ur code in GitHub with different repo name
2. I will send you a google forms, 
   submit the link in that forms

"""




# Test

dogs = 1
cats = 0

dogs == 1


dogs == 1 and cats == 0
dogs == 1 - True
cats == 0 - True

dogs == 1 or cats == 0

if dogs == 1 and cats == 1:
    print("I am happy")
else:
    print("I am not")

dogs == 1 and cats == 1

def add(a, b):
    print(a+b)

add(3, 4)


# Loops
# For and While
# Turing Complete

# For Loop
# Loops ?? What is Looping ?? - English Terms

for items in range(0, 20):
    print(items)

# what Range will be printed?


# Data Structures


Lists


l1 = [1, 2, 3, 4]

l2 = [10, 22, 33, 44]

# Access
l1[2]

# Add ??
# Functions/Methods for list

l1.append(10)

l2.append(99)


# Remove ??
l2.pop()


# Display the entire list

for index in range(0, 5):
    print(l1[index])

# index values - 0 to 4


l1 = [1, 2, 3, 4]

l1[0]

index = 2
l1[index]



"""
Assignment 2.1:
MOST IMPORTANT

1. Step Function in For Loop (Google)
Create two different codes(values) using Step Functions

2. Implement List methods in w3schools
Deadline of this assignment will be given in the next session

28th of December 2021
"""


for i in range(0, 3):
    print(i)
"""
a. 0
b. 0 to 3
c. 0 to 2
d. None/Error
"""




l1 = [22, 33, 56, 77, 92]

l1[2]

"""
what is the index number/value of the last number in list l1??
4

l1[5]

N - None
E - Error
"""


"""
Is List ordered ??
Yes
What does ordered?
Index values
"""


# Tuple
# Immutable - Unchangeable
# Ordered

t1 = (1, 2, 3, 4)

t1[0]

"""
Tuples are faster to display items than lists when Large Data
Numpy - Is used In matrix calc
"""

# Dictionary

d1 = {"name":"Gowtham", "Dept":"CSE"}

d1["name"]

d1["marks"] = 100

# Word Frequency , Descending Order - Dict

# Strings

l1 = ['g', 'o', 'w', 't', 'h', 'a', 'm']

s1 = "gowtham"

l1[1]

s1[1]

# Filename Extension - Using String Functions


# While

for i in range(0, 10):
    print(i)


i = 0
while i<10:
    print(i)

l1 = [0,1, 33, 4]

i = 0
while i<4:
    print(l1[i])
    i = i+1


3 - last index value of above list l1


for index in range(0, 4):
    print(l1[index])

for items in l1:
    print(items)






Assignment 2.2

1. Tuples are immutable, then how can you change a value in 
  a Tuple ?? Find workaround

2. Learn about set in w3schools

3. Create a dictionary with a number as the key
  and a List, dictionary as a value

4. Implements methods of Dictionary from w3schools

5. Implements methods of Strings from w3schools

Deadline for this is 30th December 2021 - 12:30 AM





# Web Scraping

import requests
from bs4 import BeautifulSoup as bs


urls = ["https://www.amazon.in/United-Colors-Benetton-Sneakers-11-19P8SNEA3113I_902_40/dp/B07L58JVGV/ref=pd_d0_recs_v4_ac_w2_22/258-3905153-5220442?pd_rd_w=1uyYc&pf_rd_p=d07e23a0-088f-4edf-84b9-2836fb74cf31&pf_rd_r=4TKKTDR8TCG1WV73P70B&pd_rd_r=e725627d-a833-48c0-8d14-1869b648be09&pd_rd_wg=thhbR&pd_rd_i=B07LGJZ3YP&psc=1"]

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}

page = requests.get(urls[0], headers=headers)

soup = bs(page.content, "html.parser")

title = soup.find(id="productTitle").get_text()

price = soup.find_all('span', attrs={"class":"a-price-whole"})[0].get_text()


price

replace , to . ?? - what function?


from twilio.rest import Client

client = Client('ACe2a630f70c541317ddd1db56b251f57f', '39a9c77b662cc798172f9115c8fb')

client.message.create(to_='+919382601818', from_='+14703471360', body='Price Reduced'+urls[0])


# OCR
# Tesseract
import pytesseract
# Computer Vision - OpenCV
import cv2
# Numpy - matrix calculations
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"D:\Program_Files\Tesseract-OCR\tesseract.exe"

# reads an image and convert it to a matrix
image = cv2.imread("ce_sam_p_ed2.jpg")
# Filter
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(3,3),0)
blur1 = cv2.GaussianBlur(image,(3,3),0)
gray1 = cv2.cvtColor(blur1, cv2.COLOR_BGR2GRAY)
kernel = np.ones((3, 3), np.uint8)

img_erosion = cv2.erode(image, kernel, iterations=1) 
img_dilation = cv2.dilate(image, kernel, iterations=1) 
img_erdil = cv2.dilate(img_erosion, kernel, iterations=1)
erdil_blur = cv2.GaussianBlur(img_erdil,(3,3),0)

# EXTRACTION
text_image_sup = pytesseract.image_to_string(image)
text_blur_sup = pytesseract.image_to_string(blur)
text_gray_sup = pytesseract.image_to_string(gray)
text_blur1_sup = pytesseract.image_to_string(blur1)
text_gray1_sup = pytesseract.image_to_string(gray1)
text_erosion_sup = pytesseract.image_to_string(img_erosion)
text_erdil_sup = pytesseract.image_to_string(img_erdil)
text_erdil_blur_sup = pytesseract.image_to_string(erdil_blur)


#cv2.imshow("Image", image)
'''cv2.imshow("blur", blur)
cv2.imshow("Gray", gray)
cv2.imshow("Gray1", gray1)
cv2.imshow("Gray2", gray2)
cv2.imshow("Gray3", gray3)
cv2.imshow("Gray4", gray4)'''
cv2.imshow("blur", blur)
cv2.imshow("Gray", gray)
cv2.imshow("Erosion", img_erosion)
cv2.imshow("Dilation", img_dilation)
cv2.imshow("Er - Dil", img_erdil)
#cv2.imshow("Gray5", gray5)
#cv2.imshow("thresh", thresh)
#cv2.imshow("blur", blur)
#cv2.imshow("blur", img)
cv2.waitKey(0)
cv2.destroyAllWindows()






# Class

class Vehicle:
    def __init__(self, wheels, doors, color):
        self.wheels = wheels
        self.doors = doors
        self.color = color
    
    def display(self):
        print("Vroom..")


lambo = Vehicle(4, 2, "blue")

lambo.display()

lambo.color

l1 = [1, 2, 3, 4]

l1[0]

l1.append(5)


l2 = [10, 20 , 35]

l2[0]











