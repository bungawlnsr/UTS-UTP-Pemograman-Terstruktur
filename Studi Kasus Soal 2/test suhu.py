import unittest
from suhu import hitung_rata, analisis
 
DATA = [
   {"hari": "Senin", "suhu": 31},
   {"hari": "Selasa", "suhu": 33},
   {"hari": "Rabu", "suhu": 29},
   {"hari": "Kamis", "suhu": 35},
   {"hari": "Jumat", "suhu": 32},
   {"hari": "Sabtu", "suhu": 30},
   {"hari": "Minggu", "suhu": 28},
]
 
class TestSuhu(unittest.TestCase):
   def test_rata_rata(self):
       self.assertAlmostEqual(analisis(DATA)["rata"], 31.1428, places=3)
       self.assertEqual(hitung_rata(30, 32, 34), 32)
 
   def test_tertinggi_terendah(self):
       hasil = analisis(DATA)
       self.assertEqual(hasil["tertinggi"]["hari"], "Kamis")
       self.assertEqual(hasil["terendah"]["hari"], "Minggu")
 
   def test_jumlah_panas(self):
       self.assertEqual(analisis(DATA)["jumlah_panas"], 3)
 
   def test_kategori_batas(self):
       kategori = {d["hari"]: d["kategori"] for d in analisis(DATA)["detail"]}
       self.assertEqual(kategori["Jumat"], "Panas")   # tepat 32
       self.assertEqual(kategori["Senin"], "Normal")
 
   def test_batas_panas_keyword(self):
       self.assertEqual(analisis(DATA, batas_panas=30)["jumlah_panas"], 5)
 
if __name__ == "__main__":
   unittest.main()
