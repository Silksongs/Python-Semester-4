def my_tabulate(items, headers, tablefmt="grid"):
    string = []
    if tablefmt == "grid":


        # Максимальные элементы из каждого столбца
        mx = []
        for i in range(len(headers)):
            mx.append(len(max(headers[i].split("\n"), key=lambda elem: len(elem))))
        for i in range(len(items[0])):
            for item in items:
                if mx[i] < len(max(str(item[i]).split("\n"), key=lambda elem: len(str(elem)))):
                    mx[i] = len(max(str(item[i]).split("\n"), key=lambda elem: len(str(elem))))

        head_str = "+"
        # Верхушка
        for head in range(len(headers)):
            head_str += "-" + ('-' * mx[head]) + "---+"
        string.append(head_str)
        for i in range(len(max(headers, key=lambda elem: len(elem.split("\n"))).split("\n"))):
            head_str = "|"
            for j in range(len(headers)):
                try:
                    head_str += " " + headers[j].split("\n")[i] + (" " * (mx[j] - len(headers[j].split("\n")[i]))) + "   |"
                except:
                    head_str += " " + (" " * mx[j]) + "   |"

            string.append(head_str)
        # Низ
        head_str = "+"
        for head in range(len(headers)):
            head_str += "=" + ('=' * mx[head]) + "===+"
        string.append(head_str)

        # Основа

        for item in items:
            for i in range(len(max(item, key=lambda elem: len(str(elem).split("\n"))).split("\n"))):
                item_str = "|"
                for j in range(len(item)):
                    try:
                        item_str += " " + str(item[j]).split("\n")[i] + (" " * (mx[j] - len(str(item[j]).split("\n")[i]))) + "   |"
                    except:
                        item_str += " " + (" " * mx[j]) + "   |"
                string.append(item_str)
            string.append("+" + "".join(["-" + ('-' * mx[head]) + "---+" for head in range(len(headers))]))
    return '\n'.join(string)




table = [["eggs", 451], ["more\nspam", 42]]
headers = ["item\nname", "qty"]
print(my_tabulate(table, headers, tablefmt="grid"))