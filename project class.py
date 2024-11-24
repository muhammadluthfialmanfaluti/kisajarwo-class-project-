import random
class kisahJARWO:
    def __init__(self):
        self.nama = "jarwo"

    def mulai(self):
        print("Selamat datang di Kisahku!")
        self.nama = input("Siapa namamu? ")
        print(f"Halo {self.nama}! Mari mulai petualanganmu.")
        self.jalan_cerita()

    def jalan_cerita(self):
        print("\nKamu berada di sebuah persimpangan jalan")
        print("1. Ambil jalan ke neraka")
        print("2. Ambil jalan ke surga")
        pilihan = input("Ke mana kamu akan pergi? (1/2): ")

        if pilihan == "1":
            print("Kamu memilih jalan ke neraka dan menemukan sebuah hutan misterius dan aneh")
        elif pilihan == "2":
            print("Kamu memilih jalan ke surga dan tiba di sebuah desa yang ramah.")
        else:
            print("Pilihan tidak valid. Coba lagi.")
            self.jalan_cerita()

if __name__ == "__main__":
    game = kisahJARWO()
game.mulai()


#MADE BY MUHAMMAD LUTHFI AL MANFALUTI X.5