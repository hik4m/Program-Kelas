print("================Selamat Datang di Program Gabut Hikam==================")
print("||Sebelum melanjutkan program silahkan menjawab pertanyaan berikut : ||")
print("||Siapakah Ketua dan Wakil Ketua dari Kelas XI-2?                    ||")
print("||A. Rega & Nabila                                                   ||")
print("||B. Afif & Alisya                                                   ||")
print("||C. Hikam & Cahya                                                   ||")
print("||D. Damar & Duwi                                                    ||")
print("||E. Adin & Elmira                                                   ||")
print("=======================================================================")
jawaban = input("Input Jawaban Anda : ")

if jawaban.upper() == "D":
    print("========Jawaban Anda Benar, Silahkan Input Nomor Absen Anda========")
else:
    print("Anda Bukan dari kelas XI-2, Program akan dihentikan.")
    exit()

daftar_siswa = [
    ["Adin Nurimansyah", "L"],
    ["AFIN CAHYO GUMILANG", "L"],
    ["Alisandra Sabrina Putri Pratama", "P"],
    ["Alisya Putri Kusumawardani", "P"],
    ["Amanda Siti Bulgis", "P"],
    ["ANGGARA ALDODIANSYAH", "L"],
    ["Habib Taufiqul Al Yudha", "L"],
    ["APRILIA DELA SANTIKA", "P"],
    ["AQLIZA JUNIOR HIKAM R", "L"],
    ["CAHYA CANTIKA PUTRI", "P"],
    ["Chandra Adhe Saputra", "L"],
    ["DAMAR SATRIO PANULUH", "L"],
    ["Dedi yuda wardiansyah", "L"],
    ["DELLA DWI FIRNANDA", "P"],
    ["DEVTIARA SALSA MAHARANI", "P"],
    ["Duwiati Febriana Rohmah", "P"],
    ["Elmira Amalia Putri", "P"],
    ["FIQY FASTIAN MARINDRA", "L"],
    ["Firda Dwi Aulia", "P"],
    ["Isti Garnis Arianti", "P"],
    ["Maharani Ayu Setyawati", "P"],
    ["MUHADZDZIB FARAS", "L"],
    ["MUHAMMAD ANWAR AFIFUDDIN", "L"],
    ["MUTIA NUR JEFIANA", "P"],
    ["Nabila Juliya Dwi Astutik", "P"],
    ["Olga Dyta Adiya Pamekar", "P"],
    ["PUTRI GIRI RAHAYU", "P"],
    ["REGA FIRDAUS MAULANA", "L"],
    ["RISKIYA NONIK BETTYTRI S.", "P"],
    ["Rizal Baihaqi Effendi", "L"],
    ["SHELLA NOVITASARI AGNI", "P"],
    ["Shella Putri Rama Dani", "P"],
    ["SRI WAHYUNI", "P"],
    ["VANI SEPTI ANDREANI", "P"],
    ["Widiya Umi Mayasari", "P"],
    ["Wildan In'amul Muna", "L"]
]

nomor_absen = int(input("Input nomor absen kamu : "))
if nomor_absen < 1 or nomor_absen > len(daftar_siswa):
  print("Maaf, kamu bukan siswa kelas XI-2")
  exit()

nama = daftar_siswa[nomor_absen-1][0]
jenis_kelamin = daftar_siswa[nomor_absen-1][1]
if jenis_kelamin == 'L':
  jenis_kelamin = 'Laki - Laki'
else:
  jenis_kelamin = 'Perempuan'

print("========================Welcome Student===================================")
print(f"Nama                : {nama}")
print(f"Jenis Kelamin       : {jenis_kelamin}")
print("Kelas               : XI-2")
print(f"Nomor Absen         : {nomor_absen}")
print("==========================================================================")

# Daftar pelajaran
daftar_pelajaran = {
  "Senin": [
    ["Upacara", "07.00 - 07.45"],
    ["Bahasa Jawa", "07.45 - 08.30"],
    ["Bahasa Jawa", "08.30 - 09.15"],
    ["Biologi", "09.15 - 10.00"],
    ["Istirahat", "10.00 - 10.15"],
    ["PAI", "10.15 - 11.00"],
    ["Informatika", "11.00 - 11.45"],
    ["Ishoma", "11.45 - 12.30"],
    ["Bahasa Indonesia", "12.30 - 13.15"],
    ["BK", "13.15 - 14.00"],
    ["Seni Budaya", "14.00 - 14.45"],
    ["Seni Budaya", "14.45 - 15.30"]
  ],
  "Selasa": [
     ["Kimia", "07.00 - 07.45"],
     ["Kimia", "07.45 - 08.30"],
     ["Matematika", "08.30 - 09.15"],
     ["Matematika", "09.15 - 10.00"],
     ["Istirahat", "10:00 - 10:15"], 
     ['Informatika', '10:15 - 11:00'], 
     ['Informatika', '11:00 - 11:45'], 
     ['Ishoma', '11:45 - 12:30'],
     ['Biologi', '12:30 - 13:15'],
     ['Biologi', '13:15 - 14:00'],
     ['Sejarah', '14:00 - 14:45'],
     ['Sejarah', '14:45 - 15:30']
   ],
   'Rabu': [
     ['PAI', '07:00 - 07:45'],
     ['PAI', '07:45 - 08:30'],
     ['Matematika', '08:30 - 09:15'],
     ['Matematika','09:15 - 10:00'], 
     ['Istirahat', '10:00 - 10:15'],
     ['Fisika', '10:15 - 11:00'],
     ['Fisika', '11:00 - 11:45'],
     ['Ishoma', '11:45 - 12:30'],
     ['Bahasa Inggris', '12:30 - 13:15'],
     ['Bahasa Inggris', '13:15 - 14:00'],
     ['Biologi', '14:00 - 14:45'],
     ['Biologi', '14:45 - 15:30']
   ],
   'Kamis': [
     ['PPKN', '07:00 - 07:45'],
     ['PPKN', '07:45 - 08:30'],
     ['Penjasorkes', '08:30 - 09:15'],
     ['Penjasorkes','09:15 - 10:00'], 
     ['Istirahat', '10:00 - 10:15'],
     ['Kimia', '10:15 - 11:00'],
     ['Kimia', '11:00 - 11:45'],
     ['Istirahat', '11:45 - 12:30'],
     ['Informatika', '12:30 - 13:15'],
     ['Informatika', '13:15 - 13:30'],
     ['Bahasa Indonesia', '13:30 - 14:15'],
     ['Bahasa Indonesia', '14:15 - 15:00'],
   ],
   'Jumat': [
     ['Fisika', '07:00 - 07:45'],
     ['Fisika', '07:45 - 08:30'],
     ['Penjasorkes', '08:30 - 09:15'],
     ['Istirahat', '09:15 - 09:30'],
     ['Project', '09:30 - 10:15'],
     ['Ishoma', '10:15 - 11:00'],
     ['Extrakurikuler', '11:00 - 11:45'],
   ]
}

hari = input("Input Jadwal pelajaran hari [Senin-Jumat] : ")

if hari in daftar_pelajaran:
    print("==============================Daftar pelajaran==============================")
    for pelajaran in daftar_pelajaran[hari]:
        print(f"||{pelajaran[0]:<25}  || {pelajaran[1]}                            ||")
else:
    if hari.lower() == "sabtu" or hari.lower() == "minggu":
        print("Hari Libur.")
    else:
        print("Hari tidak dikenal.")

print("================================TERIMAKASIH====================================")
print("Program ini dibuat oleh Hikam")