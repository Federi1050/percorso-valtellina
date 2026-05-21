class Computer:
    def __init__(self, ram, cpu, disco_rigido):
        self.set_ram(ram) # numero intero
        self.set_cpu(cpu) 
        self.set_disco_rigido(disco_rigido)

    def set_ram(self, ram):
        if isinstance(ram, int) and ram>0:
            self.__ram = ram
        else:
            print("errore nel valore ram, setting default")
            self.__ram = 4
    
    def get_ram(self):
        return self.__ram
    
    def set_cpu(self, cpu):
        if isinstance(cpu, str) and cpu:
            self.__cpu = cpu
        else:
            print("errore nel valore cpu, setting default")
            self.__cpu = "unknown"

    def get_cpu(self):
        return self.__cpu
    
    def set_disco_rigido(self,disco_rigido):
        if isinstance(disco_rigido,int) and disco_rigido>0:
            self.__disco_rigido = disco_rigido
        else:
            print("errore nel valore disco rigido, setting default")
            self.__disco_rigido = 200

    def __str__(self):
        return (
            f"Il pc ha queste caratteristiche:\n"
            f"ram : {self.__ram}GB ; cpu : {self.__cpu} ; disco rigido : {self.__disco_rigido}GB"
        )

pc1 = Computer(48, "Intel i5", 3500)
print(pc1)
pc2 = Computer(16, "Amd", 600)
print(pc2)

if pc1.get_ram() > pc2.get_ram():
    print(pc1)
else:
    print(pc2)