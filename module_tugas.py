import time
import os
import math

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def write(a,b):
        clear()
        print(a, end="", flush=True)
        for i in range(b):
            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(0.5)
            print("\r" + a + "   \r" + a, end="", flush=True)
        time.sleep(0.5)

def bio():
    clear()
    nama = input("Masukkan nama: ")
    kelas = input("Masukkan kelas: ")
    jenis_kelamin = input("Masukkan jenis kelamin: ")
    usia = input("Masukkan usia: ")
    alamat = input("Masukkan alamat: ")
    clear()
    print(f"""
=============================
BIODATA
=============================
Nama           : {nama}
Kelas          : {kelas}
Jenis Kelamin  : {jenis_kelamin}
Usia           : {usia}
Alamat         : {alamat}
=============================
    """)
    input("\nTekan ENTER untuk kembali ke menu...")

def circle():
    clear()
    r = float(input("Masukkan jari-jari lingkaran (cm): "))
    luas = math.pi * r * r
    clear()
    print(f"Luas lingkaran adalah: {luas:.2f} cm²")
    input("\nTekan ENTER untuk kembali ke menu...")

def temp():
    while True:
        clear()
        print(f"""
=============================
KONVERSI SUHU
=============================
1. Celcius ke Fahrenheit
2. Fahrenheit ke Celcius
3. Celcius ke Kelvin
4. Kelvin ke Celcius
5. Fahrenheit ke Kelvin
6. Kelvin ke Fahrenheit
              
0. Stop
=============================
        """)   
        pilihan = input("\nPilih jenis konversi: ")
        match pilihan:
            case "1":
                c = float(input("Masukkan suhu dalam Celcius: "))
                f = (c * 9/5) + 32
                print(f"Hasil: {f:.2f} °F")
            case "2":
                f = float(input("Masukkan suhu dalam Fahrenheit: "))
                c = (f - 32) * 5/9
                print(f"Hasil: {c:.2f} °C")
            case "3":
                c = float(input("Masukkan suhu dalam Celcius: "))
                k = c + 273.15
                print(f"Hasil: {k:.2f} K")
            case "4":
                k = float(input("Masukkan suhu dalam Kelvin: "))
                c = k - 273.15
                print(f"Hasil: {c:.2f} °C")
            case "5":
                f = float(input("Masukkan suhu dalam Fahrenheit: "))
                k = (f - 32) * 5/9 + 273.15
                print(f"Hasil: {k:.2f} °C")
            case "6":
                k = float(input("Masukkan suhu dalam Kelvin: "))
                f = (k - 273.15) * 9/5 + 32
                print(f"Hasil: {f:.2f} °C")
            case "0" | "exit" | "quit":
                write("Kembali ke menu", 1)
                break
            case _:
                print("Pilihan tidak valid!")
                break
        input("\nTekan ENTER untuk mengulang...")

def genap():
    clear()
    try:
        start_input = input("Masukkan angka awal (default 1): ")
        end_input = input("Masukkan angka akhir (default 25): ")
        start = int(start_input) if start_input else 1
        end = int(end_input) if end_input else 26
        if start > end:
            print("Angka awal lebih besar dari angka akhir, ditukar otomatis.")
            start, end = end, start
        result = [i for i in range(start, end + 1) if i % 2 == 0]
        print(f"\nAngka genap dari {start} sampai {end}: {result}")
    except ValueError:
        print("Input harus berupa angka! Coba lagi.")

    input("\nTekan ENTER untuk kembali ke menu...")

def ganjil():
    clear()
    try:
        start_input = input("Masukkan angka awal (default 26): ")
        end_input = input("Masukkan angka akhir (default 50): ")
        start = int(start_input) if start_input else 26
        end = int(end_input) if end_input else 51
        if start > end:
            print("Angka awal lebih besar dari angka akhir, ditukar otomatis.")
            start, end = end, start
        result = [i for i in range(start, end + 1) if i % 2 != 0]
        print(f"\nAngka ganjil dari {start} sampai {end}: {result}")
    except ValueError:
        print("Input harus berupa angka! Coba lagi.")

    input("\nTekan ENTER untuk kembali ke menu...")

def prima():
    clear()
    angka = int(input("Masukkan angka: "))
    if angka < 2:
        print(f"{angka} BUKAN bilangan prima")
    else:
        prima = True
        for i in range(2, int(math.sqrt(angka)) + 1):
            if angka % i == 0:
                prima = False
                break

        if prima:
            print(f"{angka} adalah BILANGAN PRIMA")
        else:
            print(f"{angka} BUKAN bilangan prima")
    input("\nTekan ENTER untuk kembali ke menu...")

def sort_up():
    clear()
    data = input("Masukkan beberapa angka (pisahkan dengan koma, contoh: 5,8,3,1):")
    angka = [float(i.strip()) for i in data.split(",")]
    print("\n🔼 Urutan dari kecil ke besar:")
    print(sorted(angka))
    input("\nTekan ENTER untuk kembali ke menu...")

def sort_down():
    clear()
    data = input("Masukkan beberapa angka (pisahkan dengan koma, contoh: 5,8,3,1):")
    angka = [float(i.strip()) for i in data.split(",")]
    print("\n🔽 Urutan dari besar ke kecil:")
    print(sorted(angka, reverse=True))
    input("\nTekan ENTER untuk kembali ke menu...")

def average():
    clear()
    data = input("Masukkan beberapa angka (pisahkan dengan koma, contoh: 5,8,3,1):")
    nilai = [float(i.strip()) for i in data.split(",")]
    rata = (sum(nilai)) / (len(nilai))
    clear()
    print(f"Rata-rata nilai: {rata:.2f}")
    if rata >= 85 and rata <= 100:
        print("Kategori: Sangat Baik")
    elif rata >= 75 and rata < 85:
        print("Kategori: Baik")
    elif rata >= 65 and rata < 75:
        print("Kategori: Cukup")
    elif rata < 74 and rata >= 0:
        print("Kategori: Kurang")
    else:
        print("Tidak falid (harus 0-100)")
    input("\nTekan ENTER untuk kembali ke menu...")