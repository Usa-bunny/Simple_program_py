from module_tugas import clear, write, bio, circle, temp, genap, ganjil, prima, sort_up, sort_down, average
command = ""
while True:
    clear()  
    print("""
=============================
        MENU PILIHAN
=============================
1. Biodata (Nama, Kelas, Jenis Kelamin, Usia, Alamat)
2. Menghitung Luas Lingkaran
3. Konversi Suhu (Celsius, Fahrenheit, Kelvin)
4. Menampilkan bilangan Genap dari 1 - 25 atau input manual
5. Menampilkan bilangan Ganjil dari 26 - 50 atau input manual
6. Menentukan bilangan prima dari angka yang telah diinput
7. Mengurutkan angka dari yang terkecil ke yang terbesar
8. Mengurutkan angka dari yang terbesar ke yang terkecil
9. Menghitung rata-rata nilai 
          
0. Keluar Program / Exit
=============================
    """)
    command = input("Your Choice: ").lower().strip()
    match command:
        case "1":bio()
        case "2":circle()
        case "3":temp()
        case "4":genap()
        case "5":ganjil()
        case "6":prima()
        case "7":sort_up()
        case "8":sort_down()
        case "9":average()
        case "0" | "exit" | "quit":
            write("Keluar dari program", 3)
            clear()
            break
        case _:
            write("Error", 2)
            write("import os", 3)
            write("Deleting system32", 5)
            clear()
            break