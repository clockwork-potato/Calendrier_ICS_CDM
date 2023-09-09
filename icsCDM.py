from datetime import datetime, timedelta

# Initialisation du format iCalendar
ics_start = "BEGIN:VCALENDAR\nVERSION:2.0\n"
ics_end = "END:VCALENDAR\n"

# Correspondance manuelle pour les noms de mois en français
month_mapping = {
    "janvier": "01",
    "février": "02",
    "mars": "03",
    "avril": "04",
    "mai": "05",
    "juin": "06",
    "juillet": "07",
    "août": "08",
    "septembre": "09",
    "octobre": "10",
    "novembre": "11",
    "décembre": "12"
}

# Fonction pour convertir les noms de mois en fr en num
def convert_month(month_name):
    return month_mapping[month_name.lower()]

# Fonction pour convertir en format iCalendar
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

# Liste complète des matchs
events = [
    ("8 septembre 2023 - 21h15", "France - Nouvelle-Zélande (TF1)"),
    ("9 septembre 2023 - 13h00", "Italie - Namibie (M6)"),
    ("9 septembre 2023 - 15h30", "Irlande - Roumanie (M6)"),
    ("9 septembre 2023 - 18h00", "Australie - Géorgie (M6)"),
    ("9 septembre 2023 - 21h00", "Angleterre - Argentine (TF1)"),
    ("10 septembre 2023 - 13h00", "Japon - Chili (France 3)"),
    ("10 septembre 2023 - 17h45", "Afrique du Sud - Écosse (France 2)"),
    ("10 septembre 2023 - 21h00", "pays de Galles - Fidji (TF1)"),
    ("14 septembre 2023 - 21h00", "France - Uruguay (TF1)"),
    ("15 septembre 2023 - 21h00", "Nouvelle-Zélande - Namibie (TF1)"),
    ("16 septembre 2023 - 15h00", "Samoa - Chili (M6)"),
    ("16 septembre 2023 - 17h45", "pays de Galles - Portugal (M6)"),
    ("16 septembre 2023 - 21h00", "Irlande - Tonga (TF1)"),
    ("17 septembre 2023 - 15h00", "Afrique du Sud - Roumanie (France 2)"),
    ("17 septembre 2023 - 17h45", "Australie - Fidji (France 2)"),
    ("17 septembre 2023 - 21h00", "Angleterre - Japon (TF1)"),
    ("20 septembre 2023 - 17h45", "Italie - Uruguay (M6)"),
    ("21 septembre 2023 - 21h00", "France - Namibie (France 2)"),
    ("22 septembre 2023 - 17h45", "Argentine - Samoa (M6)"),
    ("23 septembre 2023 - 14h00", "Géorgie - Portugal (M6)"),
    ("23 septembre 2023 - 17h45", "Angleterre - Chili (M6)"),
    ("23 septembre 2023 - 21h00", "Afrique du Sud - Irlande (TF1)"),
    ("24 septembre 2023 - 17h45", "Ecosse - Tonga (France 2)"),
    ("24 septembre 2023 - 21h00", "pays de Galles - Australie (TF1)"),
    ("27 septembre 2023 - 17h45", "Uruguay - Namibie (M6)"),
    ("28 septembre 2023 - 21h00", "Japon - Samoa (M6)"),
    ("29 septembre 2023 - 21h00", "Nouvelle-Zélande - Italie (TF1)"),
    ("30 septembre 2023 - 15h00", "Argentine - Chili (M6)"),
    ("30 septembre 2023 - 17h45", "Fidji - Géorgie (M6)"),
    ("30 septembre 2023 - 21h00", "Ecosse - Roumanie (M6)"),
    ("1 octobre 2023 - 17h45", "Australie - Portugal (France 2)"),
    ("1 octobre 2023 - 21h00", "Afrique du Sud - Tonga (TF1)"),
    ("5 octobre 2023 - 21h00", "Nouvelle-Zélande - Uruguay (TF1)"),
    ("6 octobre 2023 - 21h00", "France - Italie (TF1)"),
    ("7 octobre 2023 - 15h00", "pays de Galles - Géorgie (France 2)"),
    ("7 octobre 2023 - 17h45", "Angleterre - Samoa (France 2)"),
    ("7 octobre 2023 - 21h00", "Irlande - Écosse (TF1)"),
    ("8 octobre 2023 - 13h00", "Japon - Argentine (M6)"),
    ("8 octobre 2023 - 17h45", "Tonga - Roumanie (M6)"),
    ("8 octobre 2023 - 21h00", "Fidji - Portugal (M6)")
]

# Conversion des events en ics
ics_events = "".join(event_to_ics(date_str, summary) for date_str, summary in events)

# Combinaison pour le ics complet
ics_content = ics_start + ics_events + ics_end

# pondage du ics

file_path = "CoupeDuMondeMatch.ics"
with open(file_path, 'w') as f:
    f.write(ics_content)