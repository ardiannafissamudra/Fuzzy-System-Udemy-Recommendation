import csv

# =================================================================
# TUGAS BESAR KECERDASAN BUATAN - SISTEM FUZZY (UDEMY DATASET)
# ANGGOTA & PERAN:
# 1. Ardian Nafis Samudra (103132400012) - Kode & Data Processing
# 2. Abdullah Ahmad Izzah (103132430024) - Data Research & Poster
# =================================================================

# 1. FUNGSI KEANGGOTAAN (FUZZIFICATION)
def fuzz_rendah(val):
    if val <= 30: return 1.0
    elif 30 < val < 42: return (42 - val) / (42 - 30)
    return 0.0

def fuzz_menengah(val):
    if val <= 38 or val >= 75: return 0.0
    elif 38 < val <= 56: return (val - 38) / (56 - 38)
    elif 56 < val < 75: return (75 - val) / (75 - 56)
    return 0.0

def fuzz_tinggi(val):
    if val <= 70: return 0.0
    elif 70 < val < 85: return (val - 70) / (85 - 70)
    return 1.0

# 2. INFERENSI (SUGENO)
def hitung_fuzzy(kualitas, harga):
    # Fuzzifikasi
    k_rendah, k_menengah, k_tinggi = fuzz_rendah(kualitas), fuzz_menengah(kualitas), fuzz_tinggi(kualitas)
    h_murah, h_normal, h_mahal = fuzz_rendah(harga), fuzz_menengah(harga), fuzz_tinggi(harga)

    # Rule Base & Defuzzifikasi (Weighted Average)
    # Output: Sangat Layak(100), Dipertimbangkan(70), Tidak Layak(40)
    rules = [
        (min(k_tinggi, h_murah), 100), (min(k_tinggi, h_normal), 100), (min(k_tinggi, h_mahal), 70),
        (min(k_menengah, h_murah), 100), (min(k_menengah, h_normal), 70), (min(k_menengah, h_mahal), 40),
        (min(k_rendah, h_murah), 70), (min(k_rendah, h_normal), 40), (min(k_rendah, h_mahal), 40)
    ]
    
    num = sum(w * z for w, z in rules)
    den = sum(w for w, z in rules)
    return num / den if den != 0 else 0

# 3. PROSES DATA UDEMY
input_file = 'udemy_courses.csv'
output_file = 'peringkat_udemy.csv'
final_results = []

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = list(csv.DictReader(f))
    # Ambil 100 data pertama
    subset = reader[:100]
    
    # Cari nilai max untuk normalisasi
    max_rev = max(float(row['num_reviews']) for row in subset)
    max_price = max(float(row['price']) for row in subset)

    for row in subset:
        # Normalisasi ke skala 1-100
        norm_kualitas = (float(row['num_reviews']) / max_rev) * 100
        norm_harga = (float(row['price']) / max_price) * 100
        
        skor = hitung_fuzzy(norm_kualitas, norm_harga)
        final_results.append({
            'course_title': row['course_title'],
            'price': row['price'],
            'reviews': row['num_reviews'],
            'skor': round(skor, 2)
        })

# Sort & Save
final_results.sort(key=lambda x: x['skor'], reverse=True)
with open(output_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['course_title', 'price', 'reviews', 'skor'])
    writer.writeheader()
    writer.writerows(final_results)

# Print Top 5
print("=== 5 KURSUS UDEMY TERBAIK (SISTEM FUZZY) ===")
for i in range(5):
    res = final_results[i]
    print(f"{i+1}. {res['course_title'][:40]}... | Skor: {res['skor']}")
