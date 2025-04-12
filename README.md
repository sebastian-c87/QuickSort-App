# QuickSort GUI App (Python + Tkinter)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![GUI](https://img.shields.io/badge/GUI-tkinter-green)
![Status](https://img.shields.io/badge/Status-Edukacyjny-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

## 🇵🇱 Wersja Polska

### 📌 Opis projektu
Aplikacja edukacyjna do wizualizacji algorytmu **QuickSort**. Pozwala wprowadzić listę liczb oddzielonych przecinkami i zobaczyć krok po kroku jak algorytm dzieli, porównuje i sortuje dane.

- Napisana w Pythonie z użyciem **tkinter** (interfejs GUI)
- Pokazuje historię działania algorytmu
- Liczy liczbę wykonanych rekurencji
- Finalny wynik: lista posortowana + analiza krok po kroku

### 🚀 Uruchomienie
1. Zainstaluj Pythona 3.10+ i bibliotekę `tkinter`
2. Uruchom:
```bash
python quicksort_gui.py
```
Lub wersję `.exe` (działa bez Pythona):
```
dist/quicksort_gui.exe
```

### 🖥️ Jak korzystać
1. Wprowadź liczby oddzielone przecinkami (np. `8,3,7,1`)
2. Kliknij **Sortuj**
3. Odczytaj wynik:
   - posortowana lista
   - liczba kroków
   - historia działania algorytmu (rekurencja, pivoty, podziały)

### 📊 Złożoność QuickSort
- Średnia: `O(n log n)`
- najgorszy przypadek: `O(n^2)`
- pamięć: `O(log n)` (rekurencja)

### 🧑‍🎓 Licencja
Aplikacja edukacyjna open-source stworzona przez studenta Uniwersytetu Vistula w Warszawie. Możesz testować, modyfikować i udostępniać.

---

## 🇬🇧 English Version

### 📌 Project Description
Educational GUI application that visualizes the **QuickSort** algorithm step by step. Enter a list of numbers and see exactly how the algorithm sorts them recursively.

- Written in Python with **tkinter** for GUI
- Displays sort history and recursion structure
- Shows pivot selections and list divisions
- Outputs final sorted list + operation trace

### 🚀 Run the App
1. Make sure you have Python 3.10+ and `tkinter`
2. Run:
```bash
python quicksort_gui.py
```
Or the standalone `.exe` version:
```
dist/quicksort_gui.exe
```

### 🖥️ How to Use
1. Enter comma-separated numbers (e.g., `8,3,7,1`)
2. Click **Sort**
3. View:
   - sorted result
   - total recursion steps
   - detailed operation history (pivots, divisions, merges)

### 📊 QuickSort Complexity
- Average: `O(n log n)`
- Worst-case: `O(n^2)`
- Memory: `O(log n)` due to recursion

### 🧑‍🎓 License
Educational open-source project created by a student of Vistula University in Warsaw. Feel free to explore, modify, and share!

