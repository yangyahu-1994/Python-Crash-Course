import printing_functions as pf
 
# 定义未打印的设计列表
unprinted_designs = ['iphon case', 'robot pendant', 'dodecahedron']
# 定义completed_models为空列表 
completed_models = []
# 调用print_models函数,其中unprinted_designs[:]使用的是副本，而非原件
pf.print_models(unprinted_designs[:], completed_models)
# 调用show_completed_models()函数
pf.show_completed_models(completed_models)
# 查看unprinted_designs列表原件
print(unprinted_designs)