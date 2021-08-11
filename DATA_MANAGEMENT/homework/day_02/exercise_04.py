import re


def get_info():
    file = open("../../file/log.txt", "r")
    while True:
        info = ""
        for item in file:
            if item == "\n":
                break
            info += item
        if not info:
            file.close()
            break
        else:
            yield info


def get_address(port):
    for info in get_info():
        act_port = re.match(r"\S+", info)
        if act_port.group() == port:
            result = re.search(r"([0-9a-f]{4}\.){2}[0-9a-f]{4}", info).group()
            return result if result else "unknown"
    return "not exist"


print(get_address("BVI100"))
