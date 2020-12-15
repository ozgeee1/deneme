

class Node():
    def __init__(self,nodeName):
        self.nodeName = nodeName
        self.NodeValue = 0
        self.paths = []


    def getNodeName(self):
        return self.nodeName
    def getNodeValue(self):
        return self.NodeValue
    def setNodeValue(self,value):
        self.NodeValue=value
    def getPaths(self):
        return self.paths;
    def setPaths(self,path):
        self.paths=[path]
    def addPaths(self,path):
        self.paths.insert(0,path)