password = 'a123456' #設定密碼
i = 3
while i > 0:
    x = input('請輸入密碼:')
    if x == password:
        print('登入成功！')
        break
    else:
        i = i - 1
        print('密碼錯誤！你還有', i, '次機會')


