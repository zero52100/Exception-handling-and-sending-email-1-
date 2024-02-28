try:
    filename=input("Enter the filename")
    with open(filename,'r')as opnefile:
        filedata=opnefile.read()
        print("file data :",filedata)
except FileNotFoundError:
    print("The entered file not found")
