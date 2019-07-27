#赋初始化值
""" list2 = []

list2 = [1,2,3,"a",'b','d']

print(list2[0],len(list2))

print(list2[-1],list2[-2])
list2.append(100)
list2.append([1,2,3])
print(list2)

list2.pop(-1)
print(list2) """

# 多维list
""" a = [[1,4],[2,5,6],[3,7,8,9]]

print(a[2][1]) """

# 列表的运算
""" list_a = [1,2]
list_b = [2,3]
list_c = list_a + list_b
print(list_c) """

# 更新列表值
""" aa = [1,2,3]
aa[1] = 10
print(aa) """

# 初始化
""" dict_a = {}
dict_a = {"name":"chengyimin","age":21,"like":["eat","drink"]}
name = dict_a["name"]
age = dict_a["age"]
like = dict_a["like"]
print(name,age,like) """

""" dict_b = {"message":{"name":"chengyimin","age":24}}
#age = dict_b["message"]["age"]
age = dict_b.get("message").get("age")
print(age) """

""" dict_a["time"] = "7月27日"
print(dict_a) """

# 初始化元组
""" tuple()
tuple_a = (1,2,3)
print(tuple_a) """

# 初始化一个集合
""" set_a = set()
list_c = [1,2,3,4]
set_a = set(list_c)
print(set_a)
 """

# 集合的运算
""" listA = [1,2,3,4]
listB = [2,3,4,5]
ret = list(set(listA).difference(set(listB)))
print(ret)

ret = list(set(listB).difference(set(listA)))
print(ret)

ret = list(set(listA).union(set(listB)))
print(ret)

ret = list(set(listA).intersection(set(listB)))
print(ret) """

# 条件语句
""" if 2 != 2:
    print(3)
else:
    print(1)

if "a" not in "assfsf":
    print("yes!")
else:
    print("no!") """

#判断成绩
""" a = float(input("请输入成绩："))
if a >=90:
    print("优秀")
elif a <=89 and a >=80:
    print("良好")
elif a <=79 and a >=60:
    print("一般")
else:
    print("不及格") """





