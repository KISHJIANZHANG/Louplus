#average read file
import webbrowser
def main():
    fileName=input('what file are the numbers in?')
    infile = webbrowser.open(fileName, 'r')
    sum = 0.0
    count =0
    line = infile.readline()
    while line !="":
        sum=sum+eval(line)
        count=count+1
        line=infile.readline()
    print('\nThe average of the numbers in this file is',sum/count)
main()
