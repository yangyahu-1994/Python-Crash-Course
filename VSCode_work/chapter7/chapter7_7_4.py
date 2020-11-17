# 提示内容
prompt = "Please enter a series of pizza ingredients:"
prompt += "\n(Please press ‘quit’ when you finish typing.) "

# 编写循环
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print("We will add this ingredient to the pizza.")