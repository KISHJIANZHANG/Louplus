# average 4
def main():
    sum=0.0
    count=0
    xStr=input('enter a number (<enter>to quit)')  
    while xStr !='':
        while xStr .isdigit():
            x=eval(xStr)
            sum=sum+x
            count=count+1
            xStr=input('enter a number (<enter>to quit)')
        break
    print('please input a number')
    print('\nthe average of the above' ,count, 'numbers is',sum/count)
main()
