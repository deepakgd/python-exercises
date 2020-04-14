class Computer:
    def __init__(self, ram, memory):
        self.ram = ram
        self.memory = memory

    def config(self):
        print(f"""Ram: {self.ram}
Memory: {self.memory}""")

com1 = Computer("8GB", "500GB")
com2 = Computer("16GB", "1TB")

Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()