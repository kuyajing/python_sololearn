'''
Lesson1 

try:
  variable = 10
  print (10 / 2)
except ZeroDivisionError:
  print("Error")
print("Finished")

'''


try:
  meaning = 42
  print(meaning / 0)
  print("the meaning of life")
except (ValueError, TypeError):
  print("ValueError or TypeError occurred")
except ZeroDivisionError:
  print("Divided by zero")