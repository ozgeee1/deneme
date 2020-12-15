
class Information:

    def __init__(self):
        self.height_list = []
        self.weight_list = []
        self.Tshirt_size = []



    def fill_the_lists(self):
        file = open("Informations.txt", "r", encoding="utf-8")
        I_list = file.readlines()
        for index in range(1,len(I_list)):
            line = I_list[index]
            line_list = line.split(" ")
            height = int(line_list[0])
            weight = int(line_list[1])
            Tshirt_size = line_list[2][:-1]
            self.height_list.append(height)
            self.weight_list.append(weight)
            self.Tshirt_size.append(Tshirt_size)
        file.close()
