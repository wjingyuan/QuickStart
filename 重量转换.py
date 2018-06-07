'''
重量转换，输入一个带单位的重量值，转换为另一个重量。
'''

gravity = input("请输入带单位的重量（如23kg）。")
if gravity[-2:] in ["kg","KG"]:
    gram = eval(gravity[:-2])*1000
    print(str(gram)+"g")
elif gravity[-1] in ["g","G"]:
    kilogram = eval(gravity[:-1])/1000
    print(str(kilogram)+"kg")
else:
    print("输入格式错误。")