try:
    f = open('/opt/tmp/myfile.txt')
except IOError:
    print('File not found')
except EnvironmentError:
    print('Failed to open file')