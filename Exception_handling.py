1# print("stmt-1")
# try:
#     print(10 / 0)
# except:
#     print(10 / 2)
# print("stmt-3")
2# try:
#     print(10/2)
# except:
#     print(10/3)
3# try:
#     print("stmt-1")
#     print("stmt-2")
#     print("stmt-3")
# except:
#     print("stmt-4")
# print("stmt-5")
4# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print("Exception raised and Descrption is",msg)
5# try:
#     x = int(input("Enter The First Number:"))
#     y = int(input("Enter The Second Number:"))
#     print(x / y)
# except ZeroDivisionError:
#     print("Cannot Divide With Zero")
# except ValueError:
#     print("Please Provide Int Value Only")
6# try:
#     x = int(input("Enter The First Number:"))
#     y = int(input("Enter The Second The Number:"))
#     print(x / y)
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ArithmeticError:
#     print("ArithmeticError")
7# try:
#     x = int(input("Enter The First Number:"))
#     y = int(input("Enter The Second Number:"))
#     print(x / y)
# except(ZeroDivisionError,ValueError) as msg:
#     print("Please Provide Valid Input Value Only And Problem is:",msg)
 # 8 try:
#     print('try')
# except:
#     print('except')
# finally:
#     print('finally')
9# try:
#     print('try')
#     print(10/0)
# except ZeroDivisionError:
#     print('except')
# finally:
#     print('finally')
try:
    print('try')
    print(10/0)
except ValueError:
    print('except')
finally:
    print('finally')







