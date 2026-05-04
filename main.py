class Universitet:
    def __init__(self, nomi, studentlar):
        self.nomi = nomi
        self.__studentlar = studentlar

    def qabul(self, n):
        self.__studentlar += n

    def bitiruv(self, n):
        self.__studentlar -= n

    def info(self):
        print(f"Nomi: {self.nomi}")
        print(f"Studentlar soni: {self.__studentlar}")


u1 = Universitet("TATU", 500)
u1.qabul(100)
u1.info()

u1.bitiruv(500)
u1.info()
