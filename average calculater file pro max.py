#average read file
def main():
    fileName=input('what file are the numbers in?')
    infile = open(fileName, 'r')
    sum = 0.0
    count =0
    line = infile.readline()
    while line !="":
 #每行不止一个数字，用,分割
        for xStr in line.split(','):
            sum=sum+eval(xStr)
            count=count+1
        line=infile.readline()
    print('\nThe average of the numbers in this file is',sum/count)
main()
