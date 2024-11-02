import random

def gizli_hazine():
    print("🌟 Gizli Hazine Oyununa Hoş Geldiniz! 🌟")
    print("Bu oyunda gizli hazineye ulaşmak için 3 zorlu görevi tamamlamanız gerekiyor.")
    print("Hazırsanız, 'başla' yazarak oyunu başlatabilirsiniz.")

    # Oyunu başlatma
    baslangic = input("Oyunu başlatmak için yaz: ").strip().lower()
    if baslangic != "başla":
        print("Oyunu başlatmak için 'başla' yazmalısınız.")
        return

    print("\n🎯 Görev 1: Gizli Sayıyı Tahmin Et")
    print("İlk göreviniz, 1 ile 50 arasında bir gizli sayıyı bulmak!")
    gizli_sayi = random.randint(1, 50)
    
    # İlk görev: Sayı Tahmin Etme
    while True:
        tahmin = int(input("Tahmininiz: "))
        if tahmin < gizli_sayi:
            print("Daha yüksek bir sayı deneyin!")
        elif tahmin > gizli_sayi:
            print("Daha düşük bir sayı deneyin!")
        else:
            print("Doğru tahmin! İlk görevi tamamladınız.")
            break

    print("\n🔐 Görev 2: Şifreyi Kırın")
    print("İkinci göreviniz, gizli hazineye ulaşmak için şifreyi bulmak.")
    print("İpucu: Şifre 4 karakterden oluşan bir sayı ve her iki basamak toplamı 10.")
    # Şifre oluşturma
    sifre = random.choice(["19", "28", "37", "46", "55", "64", "73", "82", "91"])
    while True:
        sifre_tahmin = input("Şifre tahmininiz (2 basamaklı sayı): ").strip()
        if sifre_tahmin == sifre:
            print("Tebrikler! Şifreyi kırdınız.")
            break
        else:
            print("Yanlış şifre, tekrar deneyin.")

    print("\n🧠 Görev 3: Matematik Bulmacası")
    print("Son göreviniz, aşağıdaki matematik bulmacasını çözmek:")
    print("İpucu: Bir sayının karesini alın ve 4 çıkarın.")
    while True:
        try:
            cevap = int(input("Bulmacayı çözmek için bir sayı girin: "))
            if (cevap**2 - 4) == 0:
                print("Doğru cevap! Gizli hazineye ulaştınız! 🏆")
                break
            else:
                print("Yanlış cevap! Tekrar deneyin.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    print("\n🎉 Tebrikler! Bütün görevleri başarıyla tamamlayarak gizli hazineye ulaştınız! 🎉")

# Oyunu başlat
gizli_hazine()
