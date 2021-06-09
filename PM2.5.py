def main():
    PM=eval(input('input today\'s PM2.5 index'))
    if PM<=35:
        print('good')
    elif PM<=75:
        print('mordrate')
    elif PM<=115:
        print('轻度污染')
    elif PM<=150:
        print('中度污染')
    elif PM<=250:
        print('重度污染')
    else:
        print('严重污染')
main()
