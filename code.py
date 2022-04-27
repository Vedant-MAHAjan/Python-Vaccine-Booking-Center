# There comes situations in real life when we need to make some decisions
# and based on these decisions, we decide what should we do next.
#
# Similar situations arise in programming also where we need to make
# some decisions and based on these decisions we will execute the next block of code.
#
# Such conditional statement determine the flow of the code
#
# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")
# print("Exit")
#
# a = 23
# b = 12
# if a < b:
#   print("a is lesser than b")
# else:
#   print("a is greater than b")
#
#
# #equals "==" and not equals "!="
#
# a = 20
# b = 100/5
# c = 4*4
# if a==b:
#   print("a is equal to b")
# else:
#   print("a is not equal to b")
#
# #try coding for greater than ">=" and less than"<=
#
#
# a = 23
# b = 18
# c = 9
#
# if a>b:
#   if b>c:
#     print("b is greater than c")
#   else:
#     print("b is not greater than c")
# else:
#   print("a is not greater than c")
#
# flag = "green"
#
# if flag == "red":
#   print("Stop")
# elif flag == "yellow":
#     print("Go Slow")
# elif flag == "green":
#     print("Go")
# else:
#     pint("No color")
#
# #single line if else (short hand)
#
# i = 10
# print(True) if i < 15 else print(False)
#
#
#
#
# # Looping Statements
#
# Loops are used to execute certain block of code again and again multiple times.
#
# This saves the time of the programmer.
#
#
#
#
# ##While Loop
#
# runs until a condition is satisfied
#
# breaks out when the condtion is false
#
#
# count = 1
# print("Red Bull gives you",end="")
# while(count <= 3):
#   print("wings")
#   count = count+1
#   #count +=1
#
#
#
# #similar to if-else
#
# '''while condition is true:
#   execute this statement
# else:
#   execute this statement'''
#
#
#
#
#
#
#
#
# limit = 5
#
# for i in range(1,limit):
#   print(i)
#
# #for i in range(limit)
#
# start = 4
# end = 10
#
# '''
# for i in range(start,end):
#   print(i,end=" ")
# '''
#
# '''
# list = ["potato","eggplant","bittergourd","pumpkin"]
#
# for i in list:
#     print(i)
# '''
#
#
#
#
#
#
# #break
#
# for i in range(5):
#   print(i)
#   if i == 3:
#     break
#
# '''
# food = ["muffins","pizza","burger","donuts","apple","bittergourd"]
#
# for i in food:
#     if i == "apples":
#       break
#     print("Eating ",i)
# print("Boring food found")
# print("Stop eating")
# '''
#
#
#
#
#
#
#
# #continue
#
# for i in range(2,7):
#   if i == 5:
#     continue
#   print(i)
#
#
# '''
# food = ["almonds","cashews","peanuts","raisins","dates"]
#
# for i in food:
#     if i == "peanuts":
#         continue
#     print("Eating ",i)
# '''