# Générateur d'Événements iCalendar pour les matchs de Rugby

Ce script Python génère un fichier `.ics` contenant les événements pour les matchs de rugby, permettant de les importer facilement dans la plupart des calendriers numériques.

## Fonctionnalités

- Convertit une liste de matchs et leurs dates en événements iCalendar.
- Supporte les noms de mois en français.
- Ajoute automatiquement une durée de 2 heures à chaque match.

## Comment utiliser

1. Assurez-vous que Python est installé sur votre système.
2. Copiez le script dans un fichier `.py`, par exemple `generate_ics.py`.
3. Exécutez le script avec Python pour générer le fichier `.ics`.
```python calendrier_ICS_CDM.py ```

4. Importez le fichier `.ics` généré dans votre application de calendrier préférée.

## Détails du Script

Le script est divisé en plusieurs sections principales:

- **Initialisation du format iCalendar**: Définit le squelette de base d'un fichier iCalendar.
- **Correspondance manuelle des mois**: Mappe les noms des mois en français à leurs numéros correspondants.
- **Fonctions utilitaires**: Inclut des fonctions pour convertir les dates en format iCalendar et générer les événements.
- **Liste des événements**: Contient les dates, heures, et descriptions de chaque match.
- **Génération du fichier iCalendar**: Combine tous les éléments pour créer le fichier `.ics` final.

## Exemple de Code

Le cœur du script est la fonction `event_to_ics`, qui prend une date et un résumé de l'événement pour générer un bloc d'événement iCalendar.

```python
def event_to_ics(date_str, summary):
 day, month, year, _, time = date_str.split()
 month_number = convert_month(month)
 dtstart = datetime.strptime(f"{day} {month_number} {year} {time}", '%d %m %Y %Hh%M')
 dtend = dtstart + timedelta(hours=2)
 event_format = (
     "BEGIN:VEVENT\n"
     f"DTSTART:{dtstart.strftime('%Y%m%dT%H%M00')}\n"
     f"DTEND:{dtend.strftime('%Y%m%dT%H%M00')}\n"
     f"SUMMARY:{summary}\n"
     "END:VEVENT\n"
 )
 return event_format
```
- **Ajouter dans events = [** la liste des matchs au format ' ("16 septembre 2028 - HDebut", "Nous - Versus (CHAINE)")'


