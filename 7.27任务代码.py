# 判断三角形并计算周长和面积
import math
a = float(input("请输入第一条边的长度:"))
b = float(input("请输入第二条边的长度:"))
c = float(input("请输入第三条边的长度:"))
if a+b>c and a-b<c:
    print("这三条边可以构成三角形。")
    l=a+b+c
    p=l/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("周长是：",l,"\t","面积是:",s)
else:
    print("这三条边不能构成三角形。")

# 用户身份验证
print("欢迎进入XX系统，请登录！")
username = str(input("请输入用户名："))
password = str(input("请输入密码："))
if(username=="方开" and password=="123") or (username=="刘晨" and password=="12345"):
    print("管理员登录成功！")
elif(username=="方开" and password!="123") or (username=="刘晨" and password!="12345"):
    print("管理员登录失败！")
elif(username=="张旭" and password=="123321") or (username=="沈章" and password=="123456") or (username=="许景" and password=="123456"):
    print("用户登录成功！")
elif(username=="张旭" and password!="123321") or (username=="沈章" and password!="123456") or (username=="许景" and password!="123456"):
    print("用户登录失败！")
else:
        if password=="guest":
            print("访客登录成功！")
        else:
            print("访客登录失败！")