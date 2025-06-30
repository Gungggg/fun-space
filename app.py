def luas_segitiga(alas, tinggi):
    alas = int(input("Masukkan alas segitiga: "))
    tinggi = int(input("Masukkan tinggi segitiga: "))
    luas_segitiga = 0.5 * alas * tinggi
    print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas_segitiga}.")
    
if __name__ == "__main__":
    luas_segitiga()
    print("Haloo Dunia!")