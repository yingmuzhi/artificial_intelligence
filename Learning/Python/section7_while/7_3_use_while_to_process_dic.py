
# while 和 list 结合
unconfirmed_users = ["ymz", "scj"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
    print("1")


