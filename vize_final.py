class NotHesaplama:
    def __init__(self):
        self.vize = 0
        self.final = 0
    
    def notlariAl(self):
        self.vize = float(input("Vize notunu girin: "))
        self.final = float(input("Final notunu girin: "))
    
    def ortalamaHesapla(self):
        ortalama = 0.4 * self.vize + 0.6 * self.final
        return ortalama
    
    def sonucuGoster(self):
        print("Vize Notu:", self.vize)
        print("Final Notu:", self.final)
        print("Ortalama:", self.ortalamaHesapla())

# Programın ana bölümü
if __name__ == "__main__":
    not_hesaplayici = NotHesaplama()
    not_hesaplayici.notlariAl()
    not_hesaplayici.sonucuGoster()
