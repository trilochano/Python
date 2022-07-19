try:
    f1=open("../Files/text.txt", mode='r')
    try:
        f1.write("Welcome")
    except IOError:
        print("not readble")
    finally:
        print("Inner Finally Block")
except IOError:
    print("File is not available")
finally:
    print("Finally Block")
