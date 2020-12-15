import matplotlib.pyplot as plt

#NOTE : I wanted to use numerical computations but i didn't have any function.
#So i decided to check the distribution of the points to see find easy solution




def main():
    xAxes = [2,5,8,9,23,30]
    yAxes =[6,10,18,19,50,65]
    plt.plot(xAxes,yAxes)

    plt.show()
    #In the graph as we see , after x=10 , there is almost straight line.
    #So , i am using the equation of a line from 2 points.
    #I am selecting the points from the left and right side of the point at x=15
    x1=9
    y1=19
    x2=23
    y2=50
    m=float(y2-y1)/float(x2-x1)
    approximateY = m*(15-23)+50
    print(approximateY)






main()
