
try:
    def average(x,y):
        c = (x+y)/2
        return(c)
    if __name__=="__main__":
        x = int(input("Enter the first number: \n"))
        y = int(input("Enter the second number: \n"))
        print("Average:",average(x,y))
except Exception as e:
    print(e)