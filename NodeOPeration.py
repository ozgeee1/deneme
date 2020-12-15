import Nodes


class NodeOP():
    def __init__(self):
        A = Nodes.Node("A")
        B = Nodes.Node("B")
        C=Nodes.Node("C")
        D=Nodes.Node("D")
        E=Nodes.Node("E")

        self.nodes_list = [A,B,C,D,E]
        self.adj_list = [[C,1,A,C,2,D],[A,3,B],[D,5,B,D,7,E],[B,3,A,B,5,D,B,1,E],[E,1,B,E,7,D]]

    def smallestPathNodeC(self):
        for i in range(0,len(self.adj_list)):
            self.updateValues(self.adj_list[i])
        self.updatePaths()

    def updatePaths(self):
        for i in self.nodes_list:
            done=True
            while(done):
                if(i.getNodeName()=="C"):
                    done=False
                elif i.getPaths()[0][0]!="C":
                    newPath = self.check(i.getPaths()[0][0])
                    i.addPaths(newPath)

                else :
                    done=False



    def check(self,Node):
        for i in self.nodes_list:
            for j in i.getPaths():
                if j[1]==Node:
                    return j

    def print_the_paths(self):
        for i in self.nodes_list:
            pathString = ""
            for j in i.getPaths():
                pathString += j[0]+"->"+j[1]+" "
            pathString += "total : "+str(i.getNodeValue())
            print(pathString)

    def updateValues(self,list):
        for i in range(0,len(list),3):
            NodeSource = list[i]
            valueToAdd = list[i+1]
            NodeDest = list[i+2]
            NodeSrcValue = self.getNodevalue(NodeSource)
            NodeDestValue = self.getNodevalue(NodeDest)
            if(valueToAdd+NodeSrcValue < NodeDestValue or NodeDestValue==0):
                NodeDest.setNodeValue(valueToAdd+NodeSrcValue)
                NodeDest.setPaths([NodeSource.getNodeName(),NodeDest.getNodeName()])


    def getNodevalue(self,Node):
        for i in self.nodes_list:
            if(i.getNodeName()==Node.getNodeName()):
                return i.getNodeValue()


