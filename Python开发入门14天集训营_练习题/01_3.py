# 输入姓名、性别、年龄，判断如果是女生且年龄小于28岁，打印我喜欢女生，否则，打印姐弟恋也很好奥！如果是男生，打印一起来搞基！

name = input('请输入姓名：')
sex = input('请输入年龄（男/女）：')
age = input('请输入年龄：')
if sex == '女' and age < 28:
    print('我喜欢女生。')
elif sex == '女' and age >= 28:
    print('姐弟恋也很好奥。')
else:
    print('一起来搞基！')