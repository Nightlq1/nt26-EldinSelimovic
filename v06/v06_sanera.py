# Lines containing any of the words have to be deleted.
hemligt = ["secret", "password", "snmp-server community"]

# The raw file from the router. It is never committed.
filnamn = "r1-rakonfig.txt"
rensade = []
borttagna = 0

with open(filnamn) as f:
    for rad in f:
        # any() is true if at least one of the words is present in the line.
        if any(ord_ in rad for ord_ in hemligt):
            borttagna = borttagna + 1
        else:
            rensade.append(rad)

with open("r1-show-run.txt", "w") as f:
    for rad in rensade:
        f.write(rad)

print(f"Tog bort {borttagna} rader. Resultatet ligger i r1-show-run.txt.")