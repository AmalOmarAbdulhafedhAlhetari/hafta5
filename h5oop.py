class hesap:
    #başlangıçta verilecek değerlerdir:
    def __init__(self,say1,say2):
        self.say1=say1
        self.say2=say2
    #toplam Fonksiyounu:
    def topla(self):
        sonuc1= self.say1+self.say2
        return sonuc1

    def cikar(self):
        sonuc2= self.say1-self.say2
        return sonuc2

    def carp(self):
        sonuc3= self.say1*self.say2
        return sonuc3

    def bol(self):
        sonuc4= self.say1/self.say2
        return sonuc4

    def yazdir(self):
        print("\nsay1",self.say1, "\nsay2",self.say2,"\nsayıların toplamı:",self.topla(),"\nsayıların çıkar:", self.cikar(),"\nsayların carbımı", self.carp(),"\nsayıların bölmesi:", self.bol())

A = hesap(5,3)
A.yazdir()
