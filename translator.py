import sys

with open(sys.argv[1]) as f:
    # read txt file and convert to readable format
    txt = f.read()
    txt_list = list(txt)
    print(txt_list)