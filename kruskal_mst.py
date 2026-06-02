"""
Modul 11 - Greedy Algorithm
Case 3b: Minimum Spanning Tree - Algoritma Kruskal
Membangun MST dengan memilih sisi dengan bobot terkecil yang
tidak membentuk siklus, hingga semua simpul terhubung.
Menggunakan Union-Find (Disjoint Set) untuk deteksi siklus.
"""


def kruskal_mst(edges, num_nodes):
    """
    Fungsi untuk mencari Minimum Spanning Tree menggunakan Algoritma Kruskal.
    
    Parameters:
        edges (list): Daftar sisi dalam format (node1, node2, weight)
        num_nodes (int): Jumlah simpul dalam graf
    
    Returns:
        float: Total bobot dari Minimum Spanning Tree
    """
    # Inisialisasi parent untuk Union-Find
    parent = {i: i for i in range(num_nodes)}
    
    def find(x):
        """Mencari root dari suatu simpul (dengan path compression)."""
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # Path compression
            x = parent[x]
        return x
    
    def union(x, y):
        """Menggabungkan dua himpunan, mengembalikan True jika berhasil."""
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x
            return True
        return False  # Berarti membentuk siklus
    
    # Urutkan sisi berdasarkan bobot (greedy choice)
    edges_sorted = sorted(edges, key=lambda x: x[2])
    total_weight = 0
    mst_edges = []
    
    for u, v, weight in edges_sorted:
        if union(u, v):
            total_weight += weight
            mst_edges.append((u, v, weight))
    
    return total_weight, mst_edges


# =============================================
# Contoh Penggunaan
# =============================================
if __name__ == "__main__":
    print("=" * 50)
    print("MINIMUM SPANNING TREE - ALGORITMA KRUSKAL")
    print("=" * 50)
    
    # Daftar sisi: (node1, node2, bobot)
    # Simpul direpresentasikan dengan angka: 0=A, 1=B, 2=C, 3=D
    edges = [
        (0, 1, 2),  # A-B dengan bobot 2
        (0, 2, 3),  # A-C dengan bobot 3
        (1, 2, 1),  # B-C dengan bobot 1
        (1, 3, 1),  # B-D dengan bobot 1
        (2, 3, 4),  # C-D dengan bobot 4
    ]
    num_nodes = 4
    
    print(f"\nDaftar Sisi (edges):")
    print(f"{'Sisi':<15} {'Bobot':<10}")
    print("-" * 25)
    node_names = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
    for u, v, w in edges:
        print(f"{node_names[u]}-{node_names[v]:<12} {w:<10}")
    
    total, mst_edges = kruskal_mst(edges, num_nodes)
    
    print(f"\nSisi yang dipilih dalam MST:")
    print(f"{'Sisi':<15} {'Bobot':<10}")
    print("-" * 25)
    for u, v, w in mst_edges:
        print(f"{node_names[u]}-{node_names[v]:<12} {w:<10}")
    
    print(f"\nTotal bobot MST (Kruskal): {total}")
    
    # Penjelasan
    print("\n" + "-" * 40)
    print("Langkah-langkah Algoritma Kruskal:")
    print("1. Urutkan semua sisi berdasarkan bobot:")
    print("   - B-C (1), B-D (1), A-B (2), A-C (3), C-D (4)")
    print("2. Pilih B-C (1): tidak siklus -> ambil")
    print("3. Pilih B-D (1): tidak siklus -> ambil")
    print("4. Pilih A-B (2): tidak siklus -> ambil")
    print("5. Pilih A-C (3): akan membentuk siklus -> skip")
    print("6. Pilih C-D (4): akan membentuk siklus -> skip")
    print(f"7. Total bobot: 1 + 1 + 2 = {total}")
