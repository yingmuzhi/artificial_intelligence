# 计数循环
cnt = 0
while cnt < 5:
    cnt += 1
    print(cnt)
# 使用输入特定字符串退出循环
msg = ''
while msg != "exit()":
    msg = input("please input your msg\t")
    if msg != "exit()":
        print(msg)
# 使用标志退出循环
active = True
while active:
    msg = input("please input\t")
    if msg == "quit":
        active = False
    elif msg == "exit()":
        active = False
    else:
        print(msg)
# 使用break退出循环
while True:
    msg = input("input\t")
    if msg == "exit()":
        break
    print(msg)
#%%
# 使用continue进入下一次循环
cnt = 0
while cnt < 5:
    msg = int(input("in\t"))
    if msg not in [1, 2, 3]:
        continue
    cnt += 1
    print(cnt)

# %%
