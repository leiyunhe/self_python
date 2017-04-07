# Flask实现登录功能

参考教程
> https://pythonspot.com/en/login-authentication-with-flask/


# 文件目录
app.py
dummy.py
tabledef.py
static
  ./style.css
templates
  ./login.html
tutorial.db 

# 运行步骤：
python tabledef.py
python dummy.py
python app.py


# 备注
tutorial.db是程序运行中生成的数据库文件

# 下一步计划

将本功能移植对接到py103学习分析的项目中，需要解决的问题有：

 + 注册功能
 + 用户登陆信息与数据库的匹配与判断（目前抄写出的代码，不能进行正确的判断）
 + 退出程序的功能写到父页面中，可以在所有页面显示