# Default Strings
x1 = "Vogel Quax zwickt Johnys Pferd Bim."
x2 = "Sylvia wagt quick den Jux bei Pforzheim."
x3 = "Prall vom Whisky flog Quax den Jet zu Bruch."
x4 = "Jeder wackere Bayer vertilgt bequem zwo Pfund Kalbshaxen."
x5 = "Franz jagt im komplett verwahrlosten Taxi quer durch Bayern."
x6 = "Bei jedem klugen Wort von Sokrates rief Xanthippe zynisch: Quatsch!"
x7 = "Stanleys Expeditionszug quer durch Afrika wird von jedermann bewundert."


# import
import random
random.seed()

# 1 Zu durchsuchenden String eingeben
print("Bitte einen Text eingeben!")
text = input()
# Default String
if text == "0":
    x = random.randint(1,7)
    if x == 1:
        text = x1
    if x == 2:
        text = x2
    if x == 3:
        text = x3
    if x == 4:
        text = x4
    if x == 5:
        text = x5
    if x == 6:
        text = x6
    if x == 7:
        text = x7

print(text)

# Input search request
print("Nach welchem Textteil möchten Sie suchen?")
search = input()
print("Wir suchen nun im Text:", text, "nach", search,"!")

print(search, " wurde ", text.count(search), "mal gefunden")
