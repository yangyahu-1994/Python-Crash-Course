# 根据观众的年龄收取不同的票价
prompt = "Our cinema charges different fares according to different ages. Please enter your age:"
prompt += "\n(To exit, press the ‘q’ key.) "

# 编写循环
active = True
while active:
    message = input(prompt)
    if message == 'q':
        break
    elif int(message) < 3:
        print("You are free.")
    elif 3 <= int(message) <= 12:
        print("You charge $10.") 
    elif int(message) > 12:
        print("You charge $15.")