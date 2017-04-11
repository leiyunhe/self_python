# 为《Py103学习分析》添加Flask登录功能

参考教程
> https://pythonspot.com/en/login-authentication-with-flask/


# 文件目录
app.py
dummy.py
tabledef.py
update_db_from_api.py
query_function.py
static
  ./style.css
templates
  ./login.html
  ./layout.html
  ./index.html
utils
  ./const_value.py
pic
  ./precisionlearning_logo.jpg
tutorial.db
database.db
runtime.txt
requirements.txt
Procfile

# 运行步骤：
python update
python tabledef.py
python dummy.py
python app.py


# 备注
tutorial.db是登录用户信息的数据库文件
database.db是查询程序的数据库文件

# 下一步计划

+ bootstrap页面设计
+ 程序抽象化处理，让程序适应更多的情况，可以考虑开智课堂其他课程，如写作班、数据科学、自然语言处理，怎么样设计一套更为通用的模板，让管理者可以通过简单的定义，完成不同课程的情况监测。
+ 功能开始复杂起来了，如何优化成更规范的代码？