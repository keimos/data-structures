# File Manipulator

def main():
    # Open file
    f = open("text-keith.txt", "a")

    # Write some code to write line sof data to file
    # for i in range(10):
    #   f.write("This is line " + str(i) + "\r\n")

    # Close the file
    # f.close()
    if f.mode == 'r':
        # content = f.read()
        # print(content)
        fl = f.readline()
        for x in fl:
            print(x)


if __name__ == "__main__":
    main()
