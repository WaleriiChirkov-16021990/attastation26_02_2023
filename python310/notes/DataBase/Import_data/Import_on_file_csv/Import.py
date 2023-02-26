import csv
from python310.notes.Models.Note import Note


def importFromFile():
    notes = []
    with open('task1/Notes.csv', 'r') as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            note = Note(row[0], row[1], row[2], row[3])
            notes.append(note)
    print("Notes imported!")
    return notes