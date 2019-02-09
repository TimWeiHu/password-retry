password = 'a123456' #設定密碼
i = 3
while i > 0:
    i = i - 1
    x = input('請輸入密碼:')
    if x == password:
        print('登入成功！')
        break
    else:
        print('密碼錯誤！')
        if i > 0:
            print('你還有', i, '次機會')
        else:
            print('沒機會囉！')


