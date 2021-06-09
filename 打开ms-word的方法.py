#average read file 文件需要在特定的文件夹内，或者使用绝对地址进行连接
def main():
    fileName=input('what file are the numbers in?')
    infile = open(fileName, 'r')
    sum = 0.0
    count =0
    line=infile.readline()
    while line !="":
        sum=sum+eval(line)
        count=count+1
        line=infile.readline()
    print('\nThe average of the numbers in this file is',sum/count)
main()
