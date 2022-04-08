print("Perhitungan Gaji Karyawan")
print("-"*30)
nama=input      ("Nama Pegawai    :")
jabatan=input   ("Jabatan         : ")
status=input    ("Menikah (Y/T)   : ")
print("-"*30)
if jabatan=="Manager":
    gajipokok=3000000
elif jabatan=="Direktur":
    gajipokok = 5000000
elif jabatan=="Staf":
    gajipokok=2000000
else:
    print("Jabatan tidak tersedia")

if status=="Y":
    anak=int(input("Banyak Anak     :"))
    if anak ==1:
        ta= 0.10* gajipokok
    elif anak ==2:
        ta=0.20 * gajipokok
    elif anak >=3:
        ta = 0.30 * gajipokok

    tk = 0.20 * gajipokok
    gajikotor = gajipokok + tk + ta
    pajak = 0.05 * gajikotor
    total=gajikotor-pajak
    print(f"Gaji Pokok          : Rp.{gajipokok:5.0f}")
    print(f"Tunjangan Keluarga  : Rp.{tk:5.0f}")
    print(f"Tunjangan Anak      : Rp.{ta:5.0f}")
    print(f"Gaji Kotor          : Rp.{gajikotor:5.0f}")
    print(f"Pajak 5%            : Rp.{pajak:5.0f}")
    print(f"Gaji Bersih         : Rp.{total:5.0f}")
elif status=="T":
    tk=0
    ta=0
    gajikotor = gajipokok + tk + ta
    pajak = 0.10 *gajikotor
    total = gajikotor - pajak
    print(f"Gaji Pokok          : Rp.{gajipokok:5.0f}")
    print(f"Tunjangan Keluarga  : Rp.{tk:5.0f}")
    print(f"Tunjangan Anak      : Rp.{ta:5.0f}")
    print(f"Gaji Kotor          : Rp.{gajikotor:5.0f}")
    print(f"Pajak 10%           : Rp.{pajak:5.0f}")
    print(f"Gaji Bersih         : Rp.{total:5.0f}")
else:
    print("Status Tidak di ketahui")
