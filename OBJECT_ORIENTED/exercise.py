class Hewan:
    def suara(self):
        print("Hewan Bersuara")
        
class Kambing(Hewan):
    def suara(self):
        print("Mbeeekk Mbeekk")
        
class Anjing(Hewan):
    def suara(self):
        print("Guk Guk Guk")
        
def buat_suara(hewan):
    hewan.suara()
    
kambing = Kambing()
anjing = Anjing()

buat_suara(kambing)
buat_suara(anjing)