# Ten plik służy do trzymania wartości stałych, palet barw, czcionek, motywów, itp.

# Bazy Danych
DB_PATH = '../hospital_data.db' # Ścieżka względem folderu notebooks

# Palety kolorów
COLORS = {
    'primary': '#2C3E50',      # Ciemny granatowy (główny kolor wykresów)
    'secondary': '#18BC9C',    # Morski/Turkusowy (akcenty)
    'danger': '#E74C3C',       # Czerwony (do oznaczania np. braków danych)
    'background': '#ECF0F1',   # Jasnoszary tło
    'missing_scale': 'Reds',     # Skala gradientowa dla braków danych
    'correlation_scale': 'RdBu_r'# Do korelacji zmiennych
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