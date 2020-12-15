
from InformationFileIO import*
from Customer import*

import NodeOPeration


def FindSize(Object1,Object2):
    #In this function , i try to find the closest weight and height to customer's weight and height.
    #First i checked both weight and height to compare
    #If there are more than 1 option with same distance from customer weight and height,
    # then i checked if weight and height are different equally or
    # one of them is outweigh.If so , i calculated how different.
    #And i choosed option that is closest to the customer's measurement with its weight and height have proportional difference
    difference = []
    inf = Object1
    cus = Object2

    for i in range(0,len(inf.weight_list)):
        difference.append(abs(inf.height_list[i]-cus.getH())+abs(inf.weight_list[i]-cus.getW()))

    min_difference = min(difference) #It is describing the closest option to the customer's measurement

    if difference.count(min_difference) > 1:
        for i in range(0,len(difference)):
            if(difference[i]==min_difference):
                difference[i] = abs(abs(cus.getH()-inf.height_list[i])-abs(cus.getW()-inf.weight_list[i]))
        updated_min_difference= min(difference)
        up_min_dif = difference.index(updated_min_difference)
        if difference.count(updated_min_difference) > 1:
            distance_w = abs(inf.weight_list[up_min_dif]-cus.getW())
            for i in range(up_min_dif+1,len(difference)):
                if(difference[i]==updated_min_difference and abs(inf.weight_list[i]-cus.getW()) < distance_w):
                    up_min_dif = i
                    distance_w = abs(inf.weight_list[i]-cus.getW())

            return inf.Tshirt_size[up_min_dif]
        else:
            return inf.Tshirt_size[up_min_dif]
    else:
        index = difference.index(min_difference)

        return inf.Tshirt_size[index]


def main():
    inf = Information()
    cus = Customer("Monica", 161, 61)
    inf.fill_the_lists()
    TshirtSize = FindSize(inf, cus)
    cus.setSize(TshirtSize)
    cus.ShowCustomerInformations()









main()


