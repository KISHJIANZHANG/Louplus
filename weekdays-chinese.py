#day of the week
weekdays='星期一星期二星期三星期四星期五星期六星期日'
n=input('请输入星期数（1-7）')
pos=(int(n)-1)*3
weekdayschinese=weekdays[pos:pos+3]
print('中文是'+weekdayschinese)

