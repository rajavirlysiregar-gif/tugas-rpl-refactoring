# main.py (Kondisi Awal: Banyak Code Smells)
def hitung(q, p):
    # menghitung total
    tot = q * p
    if tot > 100000:
        tot = tot - (tot * 0.1) # diskon

    # tambah pajak
    pjk = tot * 0.11
    akhir = tot + pjk
    print("Total:", akhir)
    return akhir

hitung(2, 60000)