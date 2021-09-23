# 导入类
from collections import OrderedDict

# 创建有序空字典
glossary = OrderedDict()

# 给有序空字典添加键-值对
glossary['print'] = '打印'
glossary['title'] = '首字母大写'
glossary['lower'] = '全部小写'
glossary['upper'] = '全部大写'
glossary['str'] = '字符串'
glossary['key'] = '键'
glossary['value'] = '值'
glossary['items'] = '项目'
glossary['sorted'] = '排序'
glossary['set'] = '集合'

# 遍历字典并打印
for vocabulary, explanation in glossary.items():
    print(f"{vocabulary.title()}'s explanation is {explanation.title()}")