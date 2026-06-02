"""
Modul 11 - Greedy Algorithm
Case 2: Fractional Knapsack (Ransel Pecahan)
Mengisi ransel dengan nilai maksimal dengan mengambil barang berdasarkan
rasio nilai terhadap berat tertinggi terlebih dahulu.
Karena boleh mengambil sebagian barang, greedy SELALU optimal.
"""

def fractional_knapsack(items, capacity):
    """
    Fungsi untuk menyelesaikan masalah Fractional Knapsack dengan pendekatan Greedy.
    
    Parameters:
        items (list): Daftar tuple (value, weight) dari setiap barang
        capacity (int/float): Kapasitas maksimum ransel
    
    Returns:
        float: Nilai maksimum yang dapat dibawa
    """
    # Urutkan item berdasarkan rasio nilai/berat secara menurun (greedy choice)
    items_sorted = sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0.0
    
    for value, weight in items_sorted:
        if capacity >= weight:
            # Ambil seluruh barang
            capacity -= weight
            total_value += value
        else:
            # Ambil sebagian barang sesuai sisa kapasitas
            total_value += value * (capacity / weight)
            break  # Ransel sudah penuh
    
    return total_value


# =============================================
# Contoh Penggunaan
# =============================================
if __name__ == "__main__":
    print("=" * 50)
    print("FRACTIONAL KNAPSACK - GREEDY ALGORITHM")
    print("=" * 50)
    
    # Data barang: (nilai, berat)
    items = [
        (60, 10),   # Barang 1: nilai 60, berat 10 -> rasio 6.0
        (100, 20),  # Barang 2: nilai 100, berat 20 -> rasio 5.0
        (120, 30)   # Barang 3: nilai 120, berat 30 -> rasio 4.0
    ]
    capacity = 50
    
    print(f"\nDaftar Barang:")
    print(f"{'Barang':<10} {'Nilai':<10} {'Berat':<10} {'Rasio':<10}")
    print("-" * 40)
    for i, (val, wt) in enumerate(items, 1):
        ratio = val / wt
        print(f"{i:<10} {val:<10} {wt:<10} {ratio:<10.2f}")
    
    print(f"\nKapasitas ransel: {capacity}")
    
    max_value = fractional_knapsack(items, capacity)
    print(f"\nNilai maksimum yang dapat dibawa: {max_value:.2f}")
    
    # Penjelasan detail
    print("\n" + "-" * 40)
    print("Penjelasan langkah-langkah:")
    print("1. Urutkan berdasarkan rasio nilai/berat tertinggi:")
    print("   - Barang 1: rasio 6.0 (diambil penuh, sisa kapasitas 40)")
    print("   - Barang 2: rasio 5.0 (diambil penuh, sisa kapasitas 20)")
    print("   - Barang 3: rasio 4.0 (diambil 20 dari 30 -> 120 * 20/30 = 80)")
    print(f"2. Total: 60 + 100 + 80 = {max_value:.2f}")
