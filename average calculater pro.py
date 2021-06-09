#average 2
def main():
    sum=0.0
    count=0
    moredata = 'yse'
    while moredata[0]=='y':
        x=eval(input('enter a number'))
        sum=sum+x
        count=count+1
        moredata=input('do you have more numbers(y/n)?')
    print('the average of numbers is' , sum/count)
main()
