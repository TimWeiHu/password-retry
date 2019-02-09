password = 'a123456' #設定密碼
i = 0
while i < 3:
    x = input('請輸入密碼:')
    if x == 'a123456':
        print('登入成功!')
        break
    else:
        i = i + 1
        print('密碼錯誤！你還有', 3-i, '次機會')


