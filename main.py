"""
Modul 11 - Greedy Algorithm
File utama untuk menjalankan semua implementasi Greedy Algorithm:
1. Coin Change
2. Fractional Knapsack
3. Prim's MST
4. Kruskal's MST

Universitas Tidar - Teknologi Informasi
Praktikum Struktur Data 2024/2025
"""

from coin_change_greedy import coin_change_greedy
from fractional_knapsack import fractional_knapsack
from prim_mst import prim_mst
from kruskal_mst import kruskal_mst


def main():
    print("=" * 60)
    print("    PRAKTIKUM STRUKTUR DATA - MODUL 11")
    print("         GREEDY ALGORITHM")
    print("=" * 60)
    
    # ========== 1. COIN CHANGE ==========
    print("\n\n" + "=" * 60)
    print("BAGIAN 1: COIN CHANGE")
    print("=" * 60)
    print("Mencari jumlah minimum koin untuk membentuk nilai tertentu")
    print("menggunakan pendekatan greedy (pilih koin terbesar dulu).\n")
    
    amount = 57
    coins = [25, 10, 5, 1]
    change = coin_change_greedy(amount, coins)
    print(f"  Amount: {amount}")
    print(f"  Coins: {coins}")
    print(f"  Hasil: {change}")
    print(f"  Jumlah koin: {len(change)}")
    
    # ========== 2. FRACTIONAL KNAPSACK ==========
    print("\n\n" + "=" * 60)
    print("BAGIAN 2: FRACTIONAL KNAPSACK")
    print("=" * 60)
    print("Mengisi ransel dengan nilai maksimal berdasarkan")
    print("rasio nilai/berat tertinggi (boleh mengambil sebagian).\n")
    
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 50
    max_val = fractional_knapsack(items, capacity)
    print(f"  Items: {items}")
    print(f"  Capacity: {capacity}")
    print(f"  Nilai maksimum: {max_val:.2f}")
    
    # ========== 3. PRIM'S MST ==========
    print("\n\n" + "=" * 60)
    print("BAGIAN 3: MINIMUM SPANNING TREE - PRIM")
    print("=" * 60)
    print("Membangun MST dengan memilih sisi terkecil dari")
    print("simpul yang sudah dikunjungi ke simpul yang belum.\n")
    
    graph = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 1)],
        'C': [('A', 3), ('B', 1), ('D', 4)],
        'D': [('B', 1), ('C', 4)]
    }
    mst_prim = prim_mst(graph, 'A')
    print(f"  Graf: A connected to B(2), C(3)")
    print(f"        B connected to A(2), C(1), D(1)")
    print(f"        C connected to A(3), B(1), D(4)")
    print(f"        D connected to B(1), C(4)")
    print(f"  Total bobot MST (Prim): {mst_prim}")
    
    # ========== 4. KRUSKAL'S MST ==========
    print("\n\n" + "=" * 60)
    print("BAGIAN 4: MINIMUM SPANNING TREE - KRUSKAL")
    print("=" * 60)
    print("Membangun MST dengan memilih sisi berbobot terkecil")
    print("yang tidak membentuk siklus (Union-Find).\n")
    
    edges = [(0, 1, 2), (0, 2, 3), (1, 2, 1), (1, 3, 1), (2, 3, 4)]
    total_kruskal, mst_edges = kruskal_mst(edges, 4)
    print(f"  Edges: (A-B:2), (A-C:3), (B-C:1), (B-D:1), (C-D:4)")
    print(f"  MST edges: {mst_edges}")
    print(f"  Total bobot MST (Kruskal): {total_kruskal}")
    
    # ========== KESIMPULAN ==========
    print("\n\n" + "=" * 60)
    print("KESIMPULAN")
    print("=" * 60)
    print("""
  Algoritma Greedy bekerja dengan prinsip:
  1. Greedy Choice Property - Pilih pilihan terbaik pada setiap langkah
  2. Optimal Substructure - Solusi optimal dibangun dari submasalah optimal
  
  Case  1 Coin Change  : Pilih koin terbesar terlebih dahulu
  Case  2 Fr. Knapsack : Pilih rasio nilai/berat tertinggi
  Case 3a Prim's MST   : Pilih sisi terkecil dari visited nodes
  Case 3b Kruskal's MST: Pilih sisi terkecil yang tidak membentuk siklus

  Catatan: Greedy tidak selalu menghasilkan solusi optimal secara global,
           namun sangat efisien dan mudah diimplementasikan.
    """)
    
    print("=" * 60)
    print("Praktikum Struktur Data 2024/2025")
    print("Universitas Tidar - Teknologi Informasi")


if __name__ == "__main__":
    main()
