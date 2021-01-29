aString = input("输入要倒序的字符串：")
list1 = list(aString)
list1.reverse()  #列表元素倒序
print("倒序后的字符串为：")
for i in list1:
    print(i,end="")
print()