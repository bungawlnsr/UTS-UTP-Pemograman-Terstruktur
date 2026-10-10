BATAS_PANAS = 32

def baca_data(nama_file):
      data = []
   try:
       with open(nama_file, "r") as file:
           for baris in file:
               baris = baris.strip()
               if not baris:
                   continue
               hari, suhu = baris.split(";")
               data.append({"hari": hari, "suhu": int(suhu)})
   except FileNotFoundError:
       print(f"Error: file {nama_file} tidak ditemukan")
   return data
 
def hitung_rata(*suhu):
   return sum(suhu) / len(suhu)
 
def analisis(data, batas_panas=BATAS_PANAS):
   rata = hitung_rata(*[d["suhu"] for d in data])
   tertinggi = max(data, key=lambda d: d["suhu"])
   terendah = min(data, key=lambda d: d["suhu"])
 
   kategori = lambda suhu: "Panas" if suhu >= batas_panas else "Normal"
   detail = [{**d, "kategori": kategori(d["suhu"])} for d in data]
   jumlah_panas = len([d for d in detail if d["kategori"] == "Panas"])
 
   return {
       "rata": rata,
       "tertinggi": tertinggi,
       "terendah": terendah,
       "detail": detail,
       "jumlah_panas": jumlah_panas,
   }

def tulis_laporan(hasil, nama_file="laporan_suhu.txt"):
   with open(nama_file, "w") as file:
       file.write("LAPORAN SUHU MINGGUAN\n")
       file.write("=" * 30 + "\n")
       for d in hasil["detail"]:
           file.write(f"{d['hari']:<8}: {d['suhu']} C ({d['kategori']})\n")
       file.write("=" * 30 + "\n")
       file.write(f"Rata-rata suhu : {hasil['rata']:.2f} C\n")
       t, r = hasil["tertinggi"], hasil["terendah"]
       file.write(f"Suhu tertinggi : {t['suhu']} C ({t['hari']})\n")
       file.write(f"Suhu terendah  : {r['suhu']} C ({r['hari']})\n")
       file.write(f"Jumlah hari Panas : {hasil['jumlah_panas']}\n")
 
   with open(nama_file, "r") as file:
       print(file.read())
 
def main():
   data = baca_data("suhu.txt")
   if data:
       tulis_laporan(analisis(data))
 
if __name__ == "__main__":
   main()
