# SSIS_Project8

Rozwiązanie służy do generowania danych za pomocą skryptu napisanego w pythonie, a następnie ładowania ich do bazy danych AdventureWorksLT2019. 

Za pomocą skryptu "input_file_2.py" generowane są dane - w tym przypadku imię i nazwisko. Dane zapisywane są do pliku tekstowego. Następnie za pomocą skryptu "copy_file_rename.py" plik jest duplikowany, do nazwy nowego pliku dodawana jest data i czas stworzonego duplikatu. 

Kolejnym krokiem rozwiązania jest załadowanie wygenerowanych danych do tabeli "Employees" (backup bazy danych AdventureWorksLT2019_3.bak zawiera tabelę Employees oraz tabelę Contact wykorzystywaną w następnym kroku). Poza danymi zawartymi w pliku, do tabeli dodawana jest również data dodania rekordu do tabeli.

Ostatnim krokiem jest dodanie danych do tabeli Contact. Poza danymi wygenerowanymi przez sktypt, do tabeli Contact dodawany jest również email osób, utworzony poprzez konkatenację imienia i nazwiska osoby.
