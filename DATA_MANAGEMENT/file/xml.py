import re


class ReadXml:
    def __init__(self, filename):
        self.file = open(filename, "rb")
        self.data = self.file.read().decode()
        self.additional = re.search(r"(:.+)", self.data).group()

    def get_plateName(self):
        info = re.findall("<PlateName>(.+)</PlateName>", self.additional)
        return ''.join(info)

    def get_other_info(self, mark):
        pattern_value = rf'<{mark} value=\\"(.+?)\\" chnname=\\"(\w+)\\"'
        info = re.findall(pattern_value, self.additional)
        return f'{info[0][1]}:{info[0][0]}'


if __name__ == '__main__':
    car = ReadXml("12273_20210609140251536.dat")
    car_info = ["VehicleType", "AxleCnt", "CarWidth", "Wheelbase", "CarLength"]
    print(car.get_plateName())
    for item in car_info:
        print(car.get_other_info(item))
