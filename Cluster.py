from random import randint


class Cluster():

    def __init__(self):
        self.pointsArray = [(1.0,1.0),(1.5,2.0),(3.0,4.0),(5.0,7.0),(3.5,5.0),(4.5,5.0),(3.5,4.5)]
        #Since there are 2 clusters , we have 2 different lists which belong to one of the clusters
        self.Cluster1 = list()
        self.Cluster2 = list()


    def clusterOP(self):
        point1 = 0
        point2 = 0
        while(point1==point2): #First , we randomly select any 2 data points as cluster centers.
            point1= randint(0,len(self.pointsArray)-1)
            point2= randint(0, len(self.pointsArray) - 1)
        C1 =(self.pointsArray[point1][0],self.pointsArray[point1][1])
        C2=(self.pointsArray[point2][0],self.pointsArray[point2][1])
        #Then we calculate the distance between each cluster center and data point
        #A data point is assigned to that cluster whose center is nearest to that data point
        for i in self.pointsArray:
            dist1 = abs(C1[0]-i[0])+abs(C1[1]-i[1])
            dist2 = abs(C2[0]-i[0])+abs(C2[1]-i[1])
            if(dist1 < dist2): #It means cluster1 center is nearest to data point
                self.Cluster1.append(i)
            else:  #It means cluster2 center is nearest to data point
                self.Cluster2.append(i)

        #Finally,we print the clusters
        print("Cluster1 with center",C1)
        for i,j in self.Cluster1:
            print((i,j))
        print("Cluster2 with center",C2)
        for i,j in self.Cluster2:
            print((i,j))









