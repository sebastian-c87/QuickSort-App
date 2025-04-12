# 📌 QUICK SORT GUI – z pełnymi komentarzami i opisami
# Autor: Twój Asystent AI 🧠
# Ten program służy do sortowania liczb metodą QuickSort i pokazuje krok po kroku działanie algorytmu.
# Po uruchomieniu aplikacji należy wpisać liczby oddzielone przecinkami, np. 8,3,5,2,1

import tkinter as tk
from tkinter import messagebox, scrolledtext

# 🔄 Zmienne globalne do zapisywania liczby kroków i historii działania algorytmu
kroki = 0
historia = []

# 📌 QUICK SORT z komentarzami – funkcja rekurencyjna z zapisem działania
def quicksort_trace(arr, poziom=0):
    global kroki, historia
    kroki += 1  # Zliczamy każde wywołanie rekurencyjne

    # 🛑 Przypadek bazowy – lista jednoelementowa lub pusta
    if len(arr) <= 1:
        historia.append(f"{'  ' * poziom}✔️ Lista {arr} nie wymaga sortowania.")
        return arr
    else:
        pivot = arr[0]  # Wybieramy pivot – pierwszy element listy

        # 🔽 Dzielimy pozostałe elementy względem pivota
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]

        # 📝 Zapisujemy podział do historii działania
        historia.append(f"{'  ' * poziom}🔁 Pivot: {pivot} | <=: {less} | >: {greater}")

        # 🔁 Rekurencyjnie sortujemy podlisty
        sorted_less = quicksort_trace(less, poziom + 1)
        sorted_greater = quicksort_trace(greater, poziom + 1)

        # 📦 Łączymy posortowane wyniki
        return sorted_less + [pivot] + sorted_greater

# 📌 Funkcja wywoływana po kliknięciu przycisku "Sortuj"
def uruchom_sortowanie():
    global kroki, historia
    kroki = 0
    historia = []

    dane = entry.get()  # Pobieramy dane wpisane przez użytkownika

    try:
        # 🧮 Zamieniamy ciąg tekstowy na listę liczb
        liczby = list(map(int, dane.strip().split(',')))
    except ValueError:
        messagebox.showerror("Błąd", "Podaj tylko liczby oddzielone przecinkami.")
        return

    # ▶️ Uruchamiamy algorytm QuickSort
    wynik = quicksort_trace(liczby)

    # ✅ Wyświetlenie wyniku końcowego
    wynik_label.config(text=f"✅ Posortowana lista: {wynik}")
    kroki_label.config(text=f"📊 Liczba wykonanych kroków: {kroki}")
    podsumowanie_label.config(text=f"ℹ️ Posortowano {len(liczby)} elementów w {kroki} krokach.")

    # 📜 Wypełniamy pole tekstowe szczegółową historią
    historia_pole.config(state='normal')
    historia_pole.delete(1.0, tk.END)
    historia_pole.insert(tk.END, '\n'.join(historia))
    historia_pole.config(state='disabled')


# 📌 GUI aplikacji z opisem działania
root = tk.Tk()
root.title("🔢 QuickSort – Edukacyjna aplikacja do sortowania")
root.geometry("+0+0")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# 👋 Opis działania aplikacji (na górze)
opis_label = tk.Label(frame, text="Wpisz liczby oddzielone przecinkami, np. 5,3,8,1\nAplikacja posortuje je metodą QuickSort i pokaże każdy krok działania.", justify="left", fg="#0B4228", font=("Segoe UI", 10, "italic"))
opis_label.pack(pady=(0, 10))

# 📥 Pole do wpisania danych 
tk.Label(frame, text="Wprowadź liczby:").pack()
entry = tk.Entry(frame, width=50)
entry.pack(pady=5)

# 🔘 Przycisk wywołujący sortowanie
sort_button = tk.Button(frame, text="▶️ Sortuj", command=uruchom_sortowanie)
sort_button.pack(pady=10)

# 🧾 Etykiety wyników
wynik_label = tk.Label(frame, text="✅ Posortowana lista: ", font=("Segoe UI", 10, "bold"))
wynik_label.pack()

kroki_label = tk.Label(frame, text="📊 Liczba wykonanych kroków: ", font=("Segoe UI", 10))
kroki_label.pack()

podsumowanie_label = tk.Label(frame, text="", font=("Segoe UI", 9, "italic"), fg="gray")
podsumowanie_label.pack(pady=(0, 10))

# 📝 Pole tekstowe do historii działania
# 🧾 Nagłówek historii
tk.Label(frame, text="📜 Historia działania algorytmu:").pack()

# 📌 Legenda – co oznaczają linijki 
tk.Label(frame, text=(
    "🔎 LEGEND:\n"
    "- Pivot: liczba bazowa, względem której dzielimy listę\n"
    "- <= : liczby mniejsze lub równe pivotowi\n"
    "- >  : liczby większe niż pivot\n"
    "- ✔️  : lista nie wymaga dalszego sortowania (jest jednoelementowa lub pusta)\n"
    "- Wcięcia: oznaczają poziom zagłębienia rekurencji"
), justify="left", fg="gray", font=("Segoe UI", 7, "italic")).pack(pady=(0, 5))

# 📋 Pole tekstowe z historią
historia_pole = scrolledtext.ScrolledText(frame, width=70, height=15, wrap=tk.WORD)
historia_pole.pack()
historia_pole.config(state='disabled')


# 🔁 Uruchomienie aplikacji
root.mainloop()
