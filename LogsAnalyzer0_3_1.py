from pathlib import Path
import time
import logging
from logging.handlers import RotatingFileHandler

#konfiguracja logów
def configure_logger():
    #utworzenie pliku w folderze aplikacji
    log_dir = Path(__file__).parent
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "app.log"

    #nadanie identyfikatora logów
    logger = logging.getLogger('LogsAnalyzer')

    #nadanie minimalnego poziomu logów
    logger.setLevel(logging.INFO)

    #sprawdzenie czy logger ma już przypisane handlery
    if logger.handlers:
        return logger
    
    #format logów
    formatter = logging.Formatter(
        fmt="%(actime)s|%(levelname)s|%(name)s[%(message)s]",
        datefmt="%Y-%m-%d %H:%M%S"
    )

    #konfiguracja pliku logów
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1_000_000, #1MB
        backupCount=3,
        encoding='utf-8'
    )

    #poziom logowania
    file_handler.setLevel(logging.INFO)
    #format loga
    file_handler.setFormatter(formatter)

    #podpięcie handlera do loggera
    logger.addHandler(file_handler)
    
    return logger

logger = configure_logger()

logger.info("Start Aplikacji")

#Zapis do zmiennej informacji o aktualnym katalogu projektu i dodanie na końcu ingo o pliku jaki chcemy otworzyć
#file_path = Path(__file__).parent / "logs.txt"

file_path = Path(r"c:\Users\adria\OneDrive\Desktop\Python\MyProjects\ZgadnijLiczbe\app.log")

#Utworzenie pustego pliku aby zapobiec błędowi
if not file_path.exists():
    file_path.touch()
    logger.error(f'Plik {file_path} nie istniał, został utworzony')

while True:
    tryb = input("Chcesz przejrzeć logi (1) czy otrzymać ich analizę (2) czy zczytywać logi w czasie rzeczywistym (3)?")

    #Otwarcie i odczytanie informacji z pliku
    with open(file_path, "r", encoding='utf-8') as log:
        logs = log.read()
        logger.info(f'Nastąpiło otwarcie i odczytanie danych z pliku {file_path}')

        #podział całego tekstu na listę gdzie każdy jej element to jedna linia z pliku
        logs = logs.splitlines()
        logger.info('Nastąił podział linii logów')

    #nadanie wartości 0 przed każdorazowym wywołaniem if'ów
    count = 0

    #tryb = 1 wykazanie logów
    if tryb == "1":
        logger.info('Uruchomienie trybu 1 - wykaz logów')
         #input na otrzymanie od użytkownika instrukcji jakie logi chce otrzymać
        dec = input("Jakie logi chcesz wykazać? (1-całość/2-INFO/3-ERROR/4-WARNING/5-DEBUG)")

        dec_list = ['1','2','3','4','5']

        #pętla po liniach, każdy element z listy zapisany osobną zmienną
        for log_line in logs:


            #if'y wykazujące konkretne dane jakich zarząda użytkownik
            if dec == "1":
                print(log_line)
            elif dec == '2' and 'INFO' in log_line:
                print(log_line)
            elif dec == "3" and "ERROR" in log_line:
                print(log_line)
            elif dec == "4" and "WARNING" in log_line:
                print(log_line)
            elif dec == "5" and "DEBUG" in log_line:
                print(log_line)
            elif not dec in dec_line:
                logger.warning(f'Błędny wybór drybu przez użytkownika, wybrany został tryb {dec}')
                print('Wybrałeś zły tryb, operacja zostaje przerwana')
                break
            else:
                logger.error('Brak danych w pliku logów')
                print('Brak wybranych logów w pliku logów, operacja zostaje anulowana')





    #tryb = 2 podliczenie ilości logów
    elif tryb == '2':
        #decyzja użytkownika które logi chce podliczyć
        dec = input("Które logi chcesz zweryfikować? (1-INFO/2-ERROR/3-WARNING/4-DEBUG)")

        #pętla po logach
        for log_line in logs:
            #name = ''
            #if'y wykonujące liczenie i zapis nazwy loga
            if dec == '1' and 'INFO' in log_line:
                count = count + 1
                name = 'INFO'
            elif dec == '2' and 'ERROR' in log_line:
                count = count + 1
                name = 'ERROR'
            elif dec == '3' and 'WARNING' in log_line:
                count = count + 1
                name = 'WARNING'
            elif dec == '4' and 'DEBUG' in log_line:
                count = count + 1
                name = 'DEBUG'
            # else:
            #     print("Błędnie podane wartości lub brak logów")
            #     break
            
        #if name != '':
        #wykaz ilości wystąpień  
        print("Ilość wystąpień logu", name, "to:", count)
        print('Czy chcesz wykonać szczegółową analizę logów', name, '? (T/N)')
        det = input()

        #kontynuacja
        if det.lower() == 't':

            #utworzenie słownika
            analysis = {}

            #pętla po logach i odseparowanie ich po |
            for log_line in logs:
                if name in log_line:
                    rec = log_line.split('|')

                    #pobranie ostatniego elementu listy
                    log_name = rec[-1]

                    #print(log_name)

                    #dodanie wpisów do słownika
                    if log_name in analysis:
                        analysis[log_name] = analysis[log_name] + 1
                    else:
                        analysis[log_name] = 1

            #utworzenie list z każdego rekordu
            items = list(analysis.items())

            #wydruk komunikatu
            print()
            print("Wynik analizy poniżej logu", name, "poniżej: ")

            #wydruk każdego rekordu z listy
            for keys in items:  
                print(keys[0], ': ', keys[-1])

    elif tryb == '3':
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file.seek(0,2)

                while True:
                    line = file.readline()

                    if not line:
                        time.sleep(0.5)
                        continue
                    print(line.strip())
        except KeyboardInterrupt:
            print('\nZatrzymano czytanie logów, następuje wyłączenie logowania')
            

    con = input("Czy chcesz kontynuować? (T/N)")
    
    if con.lower() != 't':
        break
