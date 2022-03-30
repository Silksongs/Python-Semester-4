import graphviz, os
import pydot


def graphvis_functions():
    dot = graphviz.Digraph()
    kk = 65
    number = 65
    path = "C:/Users/1/Desktop/2 семестр/Python" # input("Enter path: ")
    dirrs = path.split("/")
    dirr = dirrs[len(dirrs)- 1]
    dot.node(chr(number), dirr)

    lists = {}

    for dirpath, dirnames, filenames in os.walk(path):
        tmp = 65
        # перебрать каталоги
        for dirname in dirnames:
            number += 1
            dot.node(chr(number), dirname)
            dot.edge(chr(kk), chr(number))
            lists[dirname] = chr(number)

        # перебрать файлы
        for filename in filenames:
            temps = dirpath.replace("\\", "/").split("/")
            temp = temps[len(temps) - 1]
            name_ = lists[temp] + chr(tmp)
            dot.node(name_, filename)
            dot.edge(lists[temp], name_)
            tmp += 1
        kk += 1

    # Сохранить исходный код в файл и предоставить движок Graphviz
    print(dot)


if __name__ == '__main__':
    # Example 13
    graphvis_functions()