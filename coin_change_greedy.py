"""
Modul 11 - Greedy Algorithm
Case 1: Coin Change (Greedy)
Mencari jumlah minimum koin untuk membentuk sejumlah nilai tertentu
dengan memilih koin bernilai terbesar terlebih dahulu.
"""

def coin_change_greedy(amount, coins):
    """
    Fungsi untuk menyelesaikan masalah Coin Change dengan pendekatan Greedy.
    
    Parameters:
        amount (int): Jumlah uang yang ingin dikembalikan
        coins (list): Daftar denominasi koin yang tersedia
    
    Returns:
        list: Daftar koin yang digunakan
    """
    # Urutkan koin dari terbesar ke terkecil (greedy choice)
    coins.sort(reverse=True)
    result = []
    
    # Iterasi setiap denominasi koin
    for coin in coins:
        # Ambil koin sebanyak mungkin selama masih muat
        while amount >= coin:
            amount -= coin
            result.append(coin)
    
    return result


# =============================================
# Contoh Penggunaan
# =============================================
if __name__ == "__main__":
    # Contoh 1: Sistem koin standar (solusi optimal)
    print("=" * 50)
    print("COIN CHANGE - GREEDY ALGORITHM")
    print("=" * 50)
    
    amount = 57
    coins = [25, 10, 5, 1]
    
    print(f"\nJumlah uang: {amount}")
    print(f"Denominasi koin: {coins}")
    
    change = coin_change_greedy(amount, coins)
    print(f"Koin yang digunakan: {change}")
    print(f"Jumlah koin: {len(change)}")
    
    # Contoh 2: Sistem koin lain
    print("\n" + "-" * 40)
    amount2 = 67
    coins2 = [100, 50, 20, 10, 5, 2, 1]
    
    print(f"\nJumlah uang: {amount2}")
    print(f"Denominasi koin: {coins2}")
    
    change2 = coin_change_greedy(amount2, coins2)
    print(f"Koin yang digunakan: {change2}")
    print(f"Jumlah koin: {len(change2)}")
    
    # Contoh 3: Kasus dimana greedy TIDAK optimal
    # Sistem koin: 1, 3, 4 - untuk amount 6, greedy pilih 4,1,1 (3 koin)
    # Solusi optimal sebenarnya: 3,3 (2 koin)
    print("\n" + "-" * 40)
    print("\n[Catatan] Kasus dimana greedy TIDAK menghasilkan solusi optimal:")
    amount3 = 6
    coins3 = [4, 3, 1]
    
    print(f"Jumlah uang: {amount3}")
    print(f"Denominasi koin: {coins3}")
    
    change3 = coin_change_greedy(amount3, coins3)
    print(f"Koin yang digunakan (greedy): {change3}")
    print(f"Jumlah koin (greedy): {len(change3)}")
    print("Solusi optimal sebenarnya: [3, 3] (2 koin)")
    print("-> Greedy tidak selalu optimal, tergantung sistem koin!")
