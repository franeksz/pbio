# Program: Generator sekwencji DNA w formacie FASTA
# Kontekst: Ten skrypt generuje losową sekwencję DNA na podstawie długości, ID i opisu podanych przez użytkownika,
#          a także wstawia imię użytkownika w losowej pozycji.
# Zapisuje sekwencję do pliku w formacie FASTA i wyświetla statystyki dotyczące zawartości nukleotydów.
# Szczegółowe objaśnienie działania każdej linii znajduje się poniżej.

import random
import sys

def main():
    # ORIGINAL:
    # length = int(input('Podaj długość sekwencji: '))
    # MODIFIED (walidacja błędów: sprawdzenie poprawności formatu i zakresu):
    try:
        length = int(input('Podaj długość sekwencji: '))  # Pobranie długości sekwencji od użytkownika
    except ValueError:
        print('Błąd: długość sekwencji musi być liczbą całkowitą.')  # Obsługa niepoprawnego formatu
        sys.exit(1)  # Zakończenie programu z kodem błędu
    if length <= 0:
        print('Błąd: długość sekwencji musi być większa od zera.')  # Obsługa wartości <= 0
        sys.exit(1)

    # Pobranie ID, opisu i imienia od użytkownika
    seq_id = input('Podaj ID sekwencji: ')       # ID sekwencji
    description = input('Podaj opis sekwencji: ')  # opis sekwencji
    name = input('Podaj imię: ')                  # imię wstawiane w losowe miejsce

    # Lista możliwych nukleotydów
    nucleotides = ['A', 'C', 'G', 'T']

    # ORIGINAL:
    # dna_seq = ''.join(random.choice(nucleotides) for _ in range(length))
    # insert_pos = random.randint(0, len(dna_seq))
    # final_seq = dna_seq[:insert_pos] + name + dna_seq[insert_pos:]
    # counts = {n: final_seq.count(n) for n in nucleotides}
    # MODIFIED (separacja sekwencji DNA od imienia do statystyk):
    dna_seq = ''.join(random.choice(nucleotides) for _ in range(length))  # Generowanie podstawowej sekwencji DNA
    insert_pos = random.randint(0, len(dna_seq))                         # Losowa pozycja do wstawienia imienia
    final_seq = dna_seq[:insert_pos] + name + dna_seq[insert_pos:]       # Wstawienie imienia w sekwencję

    # Obliczenie statystyk na podstawie dna_seq (bez imienia)
    counts = {n: dna_seq.count(n) for n in nucleotides}  # Zliczanie wystąpień każdego nukleotydu
    total = sum(counts.values())                         # Suma wszystkich nukleotydów
    percents = {n: counts[n] / total * 100 for n in nucleotides}  # Procentowy udział każdego nukleotydu
    # Stosunek C+G do A+T w procentach
    cg_ratio = (counts['C'] + counts['G']) / (counts['A'] + counts['T']) * 100

    # ORIGINAL:
    # with open(f'{seq_id}.fasta', 'w') as f:
    #     f.write(f'>{seq_id} {description}\n')
    #     f.write(final_seq + '\n')
    # MODIFIED (złamanie linii co 60 znaków zgodnie z konwencją FASTA):
    wrapped = '\n'.join(final_seq[i:i+60] for i in range(0, len(final_seq), 60))  # Łamanie linii co 60 znaków

    # Zapis do pliku FASTA
    filename = f'{seq_id}.fasta'  # Nazwa pliku FASTA na podstawie ID
    with open(filename, 'w') as f:
        f.write(f'>{seq_id} {description}\n')  # Nagłówek FASTA z ID i opisem
        f.write(wrapped + '\n')                # Zapis sekwencji z przerwami co 60 znaków

    # Wyświetlenie wyników użytkownikowi
    print(f'Sekwencja została zapisana do pliku {filename}')
    print('Statystyki sekwencji:')
    for n in nucleotides:
        print(f'{n}: {percents[n]:.1f}%')  # Wyświetlenie procentowego udziału nukleotydu
    print(f'%CG: {percents['C'] + percents['G']:.1f}')  # Wyświetlenie sumarycznego %C i %G

if __name__ == '__main__':
    main()  # Uruchomienie funkcji main przy wykonaniu skryptu
