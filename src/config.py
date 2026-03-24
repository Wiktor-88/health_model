# Ten plik służy do trzymania wartości stałych, palet barw, czcionek, motywów, itp.

# Bazy Danych
DB_PATH = '../hospital_data.db' # Ścieżka względem folderu notebooks

# Palety kolorów
COLORS = {
    'primary': '#2C3E50',           # Ciemny granatowy (główny kolor wykresów)
    'secondary': '#18BC9C',         # Morski/Turkusowy (akcenty)
    'danger': '#E74C3C',            # Czerwony (do oznaczania np. braków danych)
    'background': '#ECF0F1',        # Jasnoszary tło
    'missing_scale': 'Reds',          # Skala gradientowa dla braków danych
    'correlation_scale': 'RdBu_r',    # Do korelacji zmiennych
    'dist_colors': ['#3498DB', '#E67E22', '#9B59B6']      # Nowa paleta dla KDE i rozkładów
}

# Wykresy
PLOT_CONFIG = {
    'template': 'plotly_white',
    'font_family': 'Arial, sans-serif',
    'title_font_size': 22,
    'label_font_size': 14,
    'width': 900,
    'height': 600
}

# Dla zmiennych kategorycznych
CAT_CONFIG = {
    'high_cardinality_threshold': 10,   # Powyżej tej liczby unikalnych wartości szukamy grup
    'dominance_threshold': 95.0,        # Jeśli jedna kategoria ma >95%, kolumna jest prawie stała
    'imbalance_cmap': 'YlOrRd',         # Kolorystyka dla tabeli statystyk
    'missing_color': '#E74C3C'        # Kolor do podświetlania braków
}