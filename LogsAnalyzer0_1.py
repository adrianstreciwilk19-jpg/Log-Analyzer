from pathlib import Path

#Zapis do zmiennej informacji o aktualnym katalogu projektu i dodanie na końcu ingo o pliku jaki chcemy otworzyć
file_path = Path(__file__).parent / "logs.txt"

#Utworzenie pustego pliku aby zapobiec błędowi
if not file_path.exists():
    file_path.touch()

tryb = input("Chcesz przejrzeć logi (1) czy otrzymać ich analizę (2)?")

#Otwarcie i odczytanie informacji z pliku
with open(file_path, "r") as log:
    logs = log.read()
    
    #podział całego tekstu na listę gdzie każdy jej element to jedna linia z pliku
    logs = logs.splitlines()

#nadanie wartości 0 przed każdorazowym wywołaniem if'ów
count = 0

#tryb = 1 wykazanie logów
if tryb == "1":
     #input na otrzymanie od użytkownika instrukcji jakie logi chce otrzymać
    dec = input("Jakie logi chcesz wykazać? (1-całość/2-INFO/3-ERROR/4-WARNING)")

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

#tryb = 2 podliczenie ilości logów
elif tryb == '2':
    #decyzja użytkownika które logi chce podliczyć
    dec = input("Które logi chcesz zweryfikować? (1-INFO/2-ERROR/3-WARNING)")

    #pętla po logach
    for log_line in logs:

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
                rec = log_line.split(' | ')
                
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
            print(keys[0], ': ', keys[1])
