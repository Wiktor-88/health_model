import pandas as pd     # do wczytania plików
import sqlite3          # do tworzenia bazy dnaych, pracy z SQL
import os               # do rzeczy systemowych
import io               # Moduł do operacji Inmpu/Output, pozwala traktować tekst z RAMu jako fizyczny plik na dyssku


# To będzie funkcja naprawiająca plik z danymi
# Do tej pory dane były zebrane w jeden plik i drugi z etykietami
# Ta funkcja podzili wszytko na pełnoprawne pliki csv
# Jako argument będzie przyjmowała zmienna filepath, czyli lokalizacje pliku
def process_mapping_file(filepath):
    """
    Działamy na 3 różnych dataFramach
    """

    # Najpierw musimy otworzyć plik za pomocą with open()
    # filepath to lokalziacja pliku
    # 'r' oznacza ze plik tylko do odczytu, bez żadnych zmian
    # encoding tłumaczy, żeby python wyłapywał wszytko i nie wywalał się na dzinych znakach
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()       # Zamiast czytać linjka po linjce, ładujemy całość od razu do zmiennej content(zawartość)
    
   # Standaryzacja znaków nowej linii:
   # Na linuxie i windowsie działą inaczej
   # Na windowsie zamiast zwykłego \n mamy \r\n
    content = content.replace('\r\n', '\n')
    
    # Te 3 ramki dnaych są w oryginalnym pliku oddzielne linjka z samym ,
    # Więc tutaj dzielimy to na 3 tabele
    tables = content.split('\n,\n')
    
    # Normalnie pd.read_csv() oczekuje ścieżki w środku do jakeigoś miejsca na dysku
    # Z użyciem pakietu IO mozemy się tego pozbyć
    # Mamy tylko dostęp do tables[0], tables[1], tables[2]
    # Funkcja io.SStringIO bierze własnie zwykłego stringa z RAMu i daje go jako niby taki plik
    admission_type = pd.read_csv(io.StringIO(tables[0]))
    discharge_disp = pd.read_csv(io.StringIO(tables[1]))
    admission_source = pd.read_csv(io.StringIO(tables[2]))
    
    # Na koniec zwracamy poprostu trzy wczytane już pliki
    return admission_type, discharge_disp, admission_source


# Funkcja służąca to stowrzenia bazy dnaych
# Nie bierze ona żadnego argumentu, więc wystarczy, że wywołamy ją tylko raz
def create_database():
    '''
    Tworzenie bazy danych
    '''
    
    # Wczytujemy nasze dane z folderu gituba
    df_patients = pd.read_csv('.\\Data\\diabetic_data.csv')
    df_adm_type, df_discharge, df_adm_source = process_mapping_file('.\\Data\\IDS_mapping.csv')
    
    # Zamiana znaków zapytania (tutejszych braków dnaych) na NULLe, czyli Pandasowe Nan
    df_patients.replace('?', pd.NA, inplace=True)       # Parametr inplace sprawia, że zmieniamy dane od razu w tej samej zmiennej
    
    # Tworzymy połączenie z bazą danych 
    db_path = 'hospital_data.db'
    if os.path.exists(db_path):
        os.remove(db_path) # Jeżeli baza isteneje (funkcja była już wcześniej odpalana) to zostaje usunięta 
    
    # Tworzymy mowy plik - hospital_data.db jako bazę danych
    conn = sqlite3.connect(db_path)
    
    # Wrzucenie DataFramów jako tabele SQL do bazy
    # Funkcja z Pandasa to_sql wysyła DataFrame i wysyła go do bazy danych
    # Parametr index = False sprawia, żeby nie wsysłać bocznego pasaka z numeracją wierszy
    df_patients.to_sql('patients', conn, index=False)
    df_adm_type.to_sql('admission_type', conn, index=False)
    df_discharge.to_sql('discharge_disposition', conn, index=False)
    df_adm_source.to_sql('admission_source', conn, index=False)
    
    # prawdzamy czy zadziałało stworzenie bazy z danymi
    print(f"Klasa, baza dnaych jest i działą")
    
    # Testujemy teraz czy działą w środku z pomocą pzrykładowego zapytania SQL
    print("\nTestowe zapytanie SQL:")
    query = """
        SELECT 
            p.encounter_id, 
            p.age, 
            p.time_in_hospital, 
            a.description AS admission_reason
        FROM patients p
        LEFT JOIN admission_type a ON p.admission_type_id = a.admission_type_id
        LIMIT 5;
    """
    test_result = pd.read_sql_query(query, conn)
    print(test_result)
    
    # Koniec pracy
    conn.close()

if __name__ == "__main__":
    create_database()