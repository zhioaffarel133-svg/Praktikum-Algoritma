"""
Modul 11 - Greedy Algorithm
Case 3a: Minimum Spanning Tree - Algoritma Prim
Membangun MST dengan memulai dari satu simpul dan menambahkan
sisi dengan bobot terkecil yang menghubungkan simpul yang sudah
dikunjungi dengan simpul yang belum.
"""

import heapq


def prim_mst(graph, start):
    """
    Fungsi untuk mencari Minimum Spanning Tree menggunakan Algoritma Prim.
    
    Parameters:
        graph (dict): Representasi graf dalam bentuk adjacency list
                      {node: [(neighbor, weight), ...]}
        start: Simpul awal untuk memulai pencarian
    
    Returns:
        float: Total bobot dari Minimum Spanning Tree
    """
    visited = set()
    min_heap = [(0, start)]  # (bobot, simpul)
    total_weight = 0
    
    while min_heap:
        weight, node = heapq.heappop(min_heap)
        
        if node in visited:
            continue
        
        visited.add(node)
        total_weight += weight
        
        # Masukkan semua tetangga yang belum dikunjungi ke heap
        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))
    
    return total_weight


# =============================================
# Contoh Penggunaan
# =============================================
if __name__ == "__main__":
    print("=" * 50)
    print("MINIMUM SPANNING TREE - ALGORITMA PRIM")
    print("=" * 50)
    
    # Representasi graf dalam bentuk adjacency list
    # Format: {node: [(tetangga, bobot), ...]}
    graph = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 1)],
        'C': [('A', 3), ('B', 1), ('D', 4)],
        'D': [('B', 1), ('C', 4)]
    }
    
    print("\nRepresentasi Graf (Adjacency List):")
    print("-" * 40)
    for node, edges in graph.items():
        edges_str = ", ".join([f"({n}, {w})" for n, w in edges])
        print(f"  {node}: {edges_str}")
    
    start_node = 'A'
    total = prim_mst(graph, start_node)
    
    print(f"\nStarting node: {start_node}")
    print(f"Total bobot MST (Prim): {total}")
    
    # Penjelasan langkah-langkah
    print("\n" + "-" * 40)
    print("Langkah-langkah Algoritma Prim:")
    print("1. Mulai dari simpul A (bobot 0)")
    print("2. Pilih sisi terkecil dari A ke simpul lain: A-B (2) atau A-C (3)")
    print("3. Pilih A-B (2) -> kunjungi B")
    print("4. Dari simpul yang sudah dikunjungi (A,B),")
    print("   cari sisi terkecil ke simpul belum dikunjungi:")
    print("   - B-C (1) -> kunjungi C")  
    print("   - B-D (1) -> kunjungi D")
    print("5. MST terbentuk: A-B (2) + B-C (1) + B-D (1) = 4")
