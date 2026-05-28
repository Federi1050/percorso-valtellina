1. Crea un DataFrame con colonne nome, età, città da una lista di dizionari.
2. Leggi un file CSV e visualizza le prime 5 righe.
3. Visualizza informazioni generali sul DataFrame (tipi, valori nulli, shape).
4. Seleziona solo la colonna età e calcolane media, min e max.
5. Rinomina la colonna città in city.
6. Aggiungi una colonna seniority che vale True se età > 30.
7. Elimina la colonna seniority dal DataFrame.
8. Reimposta l'indice usando la colonna nome.
9. Salva il DataFrame in un file CSV senza l'indice.
10. Crea una Series da una lista e assegnale un indice personalizzato.

11. Filtra le righe dove età > 28.
12. Seleziona righe dove città è 'Milano' o 'Roma'.
13. Usa .query() per filtrare età tra 25 e 35.
14. Seleziona colonne nome ed età con .loc e le prime 3 righe.
15. Usa .iloc per selezionare le ultime 2 righe e la prima colonna.
16. Filtra righe dove il nome contiene la lettera 'a' (case-insensitive).
17. Seleziona le righe con i 2 valori di età più alti.
18. Filtra righe dove età non è null.
19. Usa condizioni multiple: età > 25 E città == 'Roma'.
20. Filtra con ~ (negazione): escludi chi ha città == 'Napoli'.

21. Calcola l'età media per città.
22. Conta il numero di persone per città.
23. Aggrega con più funzioni: min, max, mean su età per città.
24. Usa .agg() con dizionario per aggregare colonne diverse.
25. Aggiungi una colonna con la media dell'età per gruppo usando transform.
26. Trova il nome della persona più giovane per ogni città.
27. Usa groupby + apply per una funzione personalizzata (es. range dell'età).
28. Crea una pivot table: righe = città, valori = media età.
29. Usa cumsum per calcolare la somma cumulativa dell'età (dopo aver ordinato).
30. Raggruppa per più colonne (città e seniority).

31. Fai un inner join tra due DataFrame su colonna id.
32. Fai un left join e identifica le righe senza corrispondenza.
33. Concatena verticalmente due DataFrame con pd.concat.
34. Trasforma da wide a long con pd.melt.
35. Trasforma da long a wide con .pivot().
36. Usa stack() per impilare le colonne in un MultiIndex.
37. Usa unstack() per ritornare a formato tabulare.
38. Esplodi una colonna contenente liste con .explode().
39. Fai un cross join (prodotto cartesiano) tra due DataFrame.
40. Riorganizza le colonne mettendo nome per prima.

41. Individua e conta i valori nulli per colonna.
42. Riempi i valori nulli di età con la mediana.
43. Elimina le righe con almeno un valore nullo.
44. Rimuovi i duplicati mantenendo la prima occorrenza.
45. Converti la colonna data in tipo datetime ed estrai anno, mese e giorno.



46. Normalizza una colonna numerica tra 0 e 1 (min-max scaling).
47. Usa apply con una lambda per creare un saluto personalizzato dalla colonna nome.
48. Calcola una rolling mean su 7 periodi su una Serie temporale.
49. Crea un MultiIndex con città e nome e seleziona un sottoinsieme per città.
50. Usa .pipe() per concatenare due trasformazioni personalizzate in modo leggibile.