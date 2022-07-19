with open("config.txt", 'w+') as f:
    f.write("Hello \n")  # Its takes String type
    f.writelines(['welcome \n', 'bye'])  # Its takes list type
