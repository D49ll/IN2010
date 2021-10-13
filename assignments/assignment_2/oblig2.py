import time

import oppg1
import oppg2
import oppg3
import oppg4

start_time = time.time()
'''
Kjørefilen som er spesifisert i oppgaven.
Kaller på en print funksjon som printer oppgavenummen og kjører oppgaveskriptet
Filene fungerer separat også, så under utvikling holder det å jobbe i den filen man er i.
'''

def main():
    print(f'Oppgave 1:')
    G = oppg1.solu_func()
    e1 = time.time()

    print(f'\nOppgave 2:')
    oppg2.solu_func(G)
    e2 = time.time()
    
    print(f'\nOppgave 3:')
    oppg3.solu_func(G)
    e3 = time.time()
    
    print(f'\nOppgave 4:')
    oppg4.solu_func(G)
    e4 = time.time()

    print(f'\ntid oppg1: {round(e1-start_time,2)}s')
    print(f'tid oppg2: {round(e2-e1,2)}s')
    print(f'tid oppg3: {round(e3-e2,2)}s')
    print(f'tid oppg4: {round(e4-e3,2)}s')
    print(f'tid for alle oppgavene: {round(e4-start_time,2)}s')

if __name__ == "__main__":
    main()