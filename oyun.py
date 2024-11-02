import random
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def start_game():
    global gizli_sayi, sifre, gorev, start_time
    gizli_sayi = random.randint(1, 50)
    sifre = random.choice(["19", "28", "37", "46", "55", "64", "73", "82", "91"])
    gorev = 1
    start_time = datetime.now()  # Oyunun başladığı anı kaydet
    instructions.config(text="🎯 Görev 1: Gizli Sayıyı Tahmin Et\n"
                              "1 ile 50 arasında gizli bir sayı var, bulmaya çalışın!",
                        font=("Arial", 16, "bold"), fg="black")
    start_button.pack_forget()
    setup_guess_interface(check_guess)

def setup_guess_interface(command):
    global guess_entry, guess_button
    guess_entry = tk.Entry(root, font=("Arial", 14), width=20, borderwidth=3)
    guess_entry.pack(pady=10)
    guess_button = tk.Button(root, text="Gönder", command=command, font=("Arial", 14), width=10, bg="#4CAF50", fg="white")
    guess_button.pack(pady=5)

def check_guess():
    try:
        tahmin = int(guess_entry.get())
        if tahmin < gizli_sayi:
            messagebox.showinfo("Sonuç", "Daha yüksek bir sayı deneyin!")
        elif tahmin > gizli_sayi:
            messagebox.showinfo("Sonuç", "Daha düşük bir sayı deneyin!")
        else:
            messagebox.showinfo("Sonuç", "Doğru tahmin! İlk görevi tamamladınız.")
            guess_entry.delete(0, tk.END)
            start_task_2()
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

def start_task_2():
    global gorev
    gorev = 2
    instructions.config(text="🔐 Görev 2: Şifreyi Kırın\n"
                              "Şifre 2 basamaklı bir sayı ve basamaklarının toplamı 10.",
                        font=("Arial", 16, "bold"), fg="black")
    guess_button.config(command=check_password)

def check_password():
    sifre_tahmin = guess_entry.get().strip()
    if sifre_tahmin == sifre:
        messagebox.showinfo("Sonuç", "Tebrikler! Şifreyi kırdınız.")
        guess_entry.delete(0, tk.END)
        start_task_3()
    else:
        messagebox.showinfo("Sonuç", "Yanlış şifre, tekrar deneyin.")

def start_task_3():
    global gorev
    gorev = 3
    instructions.config(text="🧠 Görev 3: Matematik Bulmacası\n"
                              "Bir sayının karesini alıp 4 çıkarın. Sonuç sıfır olmalı!",
                        font=("Arial", 16, "bold"), fg="black")
    guess_button.config(command=check_puzzle)

def check_puzzle():
    try:
        cevap = int(guess_entry.get())
        if (cevap**2 - 4) == 0:
            end_time = datetime.now()  # Oyunun bittiği zamanı kaydet
            elapsed_time = end_time - start_time
            bitis_zamani = end_time.strftime("%H:%M:%S.%f")[:-3]  # Bitiş saatini formatla
            messagebox.showinfo("Tebrikler", f"Doğru cevap! Gizli hazineye ulaştınız! 🏆\n"
                                             f"Tamamlama zamanı: {bitis_zamani}\n"
                                             f"Geçen süre: {elapsed_time}",
                                icon="info")
            root.destroy()
        else:
            messagebox.showinfo("Sonuç", "Yanlış cevap! Tekrar deneyin.")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Gizli Hazine Oyunu")
root.geometry("500x400")
root.config(bg="#f0f8ff")  # Arka plan rengi

# Talimatlar
instructions = tk.Label(root, text="🌟 Gizli Hazine Oyununa Hoş Geldiniz! 🌟\n"
                                   "Oyunu başlatmak için 'Başla' butonuna basın.",
                        font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#2c3e50")
instructions.pack(pady=20)

# Başla düğmesi
start_button = tk.Button(root, text="Başla", command=start_game, font=("Arial", 14), bg="#4CAF50", fg="white", width=10)
start_button.pack(pady=20)

root.mainloop()
