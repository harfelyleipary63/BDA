# Definisikan dictionary untuk menyimpan waktu pengerjaan menu
waktu_pengerjaan = {
    "nasi goreng": 10,
    "mie goreng": 8,
    "gudeg": 15,
    "sate": 20
}

# Tampilkan menu yang tersedia
print("Menu yang tersedia:")
for menu in waktu_pengerjaan:
    print(menu)

# Pilih menu yang diinginkan
menu_diinginkan = input("Masukkan nama menu yang diinginkan: ")

# Periksa apakah menu tersedia
if menu_diinginkan.lower() in waktu_pengerjaan:
    print(f"Waktu pengerjaan untuk {menu_diinginkan}: {waktu_pengerjaan[menu_diinginkan.lower()]} menit")
else:
    print("Menu tidak tersedia")