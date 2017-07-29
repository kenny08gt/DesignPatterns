class PresentationLayer:
    def __init__(self):
        self.name = "PresentationLayer"

    def setLowerLayer(self, lowerLayer):
        self.lowerLayer = lowerLayer

    def s3(self, param):
        print("Entramos al servicio %s" % self.name)
        self.lowerLayer.s2(param)
        print("Terminamos servicio %s" % self.name)

class LogicLayer:
    def __init__(self):
        self.name = "logicLayer"

    def setLowerLayer(self, lowerLayer):
        self.lowerLayer = lowerLayer

    def s2(self, param):
        print("Entramos al servicio %s" % self.name)
        self.lowerLayer.s1(param)
        print("Terminamos servicio %s" % self.name)


class DataLayer:
    def __init__(self):
        self.name = "DataLayer"

    def s1(self, param):
        print("Entramos al servicio %s" % self.name)
        print("Process layer con %s" % param)
        print("Terminamos servicio %s" % self.name)

if __name__ == "__main__":
    ui = PresentationLayer()
    logic = LogicLayer()
    data = DataLayer()

    ui.setLowerLayer(logic)
    logic.setLowerLayer(data)

    ui.s3("exampleParam")
