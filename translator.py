import sys

with open(sys.argv[1]) as f:
    # read txt file and convert to readable format
    txt = f.read()
    txt_list = list(txt)

    # convert chars to ascii equivalent
    ascii_list = []
    bf = ">"
    for x in range(len(txt_list)):
        ascii_list.append(ord(txt_list[x]))

        # convert ascii values to extremely inefficient brainfuck code
        for i in range(ascii_list[x]):
            bf = bf + '+'
        bf = bf + '.>'

    # write to brainfuck file
    with open(sys.argv[2], 'w') as f:
        f.write(bf)
    
    print("\nFile successfully translated")
