mylist=["川川一号","川川二号","川川三号","川川四号"]
print(mylist)
print(mylist[0])
for i in mylist:
    print(i)
print(len(mylist))
#List列表是一个有序且可变的集合。允许重复成员。#
#turple元组是一个有序且不可更改的集合。允许重复成员。#
#Set集合是一个无序且无索引的集合。没有重复的成员。#
#dict字典是一个有序*且可变的集合。没有重复的成员。#
print(mylist[-1])
if    "apple" in mylist:
    print("YES")
else:
    print("NO")
mylist[0]="川川五号"
print(mylist[0])
mylist[1:3]=["六号","七号"]
print(mylist)
mylist.insert(2,"啊")
#insert是插入#
print(mylist)
mylist.append("结尾")
#append是结尾添加#
print(mylist)
mylist1=["川川一号","川川二号","川川三号","川川四号"]
mylist.extend(mylist1)
#extend是合并#
print(mylist)
mylist.remove('川川二号')
#remove是删除#
print(mylist)
mylist1.pop(2)
#pop是删除指定索引clear清空del删除#
print(mylist1)

