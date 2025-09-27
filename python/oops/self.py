class dev:
    desingnation="Senior"
    language = "Javascript"
    def getInfo(self):
        print(f"The designation of a devloper is {self.desingnation} and the working language is {self.language}")
    @staticmethod #This is deorator function it doesn't need self object to pass in the function
    def greeet():
        print("Hello Devloper")

robin = dev()
dev.getInfo(robin)
robin.greeet()