'''try:
    print(1)
    print(20 / 0)
    print(2)
except ZeroDivisionError:
    print(3)
finally:
    print(4)'''


'''x = 3
try:
 x+="2"
except:
 x+=2
else:
 x+=4
finally:
 print(x)'''

x = 0
try:
 x+=1
 raise ValueError
except NameError:
 x+=1
except ValueError:
 x+=1
else:
 x+=1
finally:
 x+=1
 print (x)

