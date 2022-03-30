file = open("markdown.txt", "r")
file2 = open("markdown2.txt", "w")
flag = False
for line in file:
    if line.strip()[0] == '"' or line.strip()[0] == "'":
        for index, char in enumerate(line):
            if char == "'" or char == '"':
                if flag:
                    line = line[:index] + "»" + line[index + 1:]
                    flag = False
                else:
                    line = line[:index] + "«" + line[index + 1:]
                    flag = True
    file2.write(line)
print("Done!")