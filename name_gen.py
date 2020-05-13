import random

names = dict()
group = dict()


def get_name(group_name):
    ret = ""
    first = True
    for e in group[group_name]:
        if not first:
            ret += " "
        ret += random.choice(names[e])
        first = False
    return ret


group["Elfen_Kind"] = ["Elfen_Kindernamen", "Elfen_Familiennamen"]
group["Elfen_Mann"] = ["Elfen_Männernamen", "Elfen_Familiennamen"]
group["Elfen_Frau"] = ["Elfen_Frauennamen", "Elfen_Familiennamen"]


def elfen_name(female=True, child=False):
    """Elfen werden so lange als Kinder angesehen, bis sie sich selbst zu Erwachsenen erklären,
was meist kurz nach ihrem hundertsten Geburtstag stattfindet. In der Zeit davor ruft man sie bei
ihrem Kindernamen.
Mit dem Erklären des Erwachsenseins sucht sich jeder Elf einen neuen Namen aus.
Trotzdem mag es Vorkommen, dass ihn diejenigen, die ihn bereits als Kind oder Jugendlichen
kannten, weiterhin mit seinem Kindernamen anreden. Der Erwachsenenname jedes Elfen ist eine
einzigartige Kreation, auch wenn ihm mitunter die Namen von respektierten Individuen oder
Familienmitgliedern eingewoben werden. Es gibt nur wenige Unterschiede zwischen Männer- und Frauennamen.
Die Zusammenfassung weiter unten spiegelt nur generelle Tendenzen wider.
Außerdem trägt jeder Elf einen Familiennamen, typischerweise eine Kombination aus anderen elfischen Worten.
Manche Elfen, die mit Menschen reisen, übersetzen ihre Familiennamen in die Gemeinsprache,
andere belassen ihn in der elfischen Version.
    """
    if child:
        return get_name("Elfen_Kind")
    if female:
        return get_name("Elfen_Frau")
    return get_name("Elfen_Mann")


group["Halbling_Mann"] = ["Halblinge_Männernamen", "Halblinge_Familiennamen"]
group["Halbling_Frau"] = ["Halblinge_Frauennamen", "Halblinge_Familiennamen"]


def halblings_name(female=True):
    """
    Ein Halbling besitzt einen Vornamen, einen Familiennamen und möglicherweise einen Spitznamen. Bei Familiennamen handelt
es sich oft um Spitznamen, die so treffend waren, dass sie über Generationen hinweg weitergegeben wurden.
    """
    if female:
        return get_name("Halbling_Frau")
    return get_name("Halbling_Mann")


group["Calishitischer_Mann"] = ["Calishitische_Männernamen", "Calishitische_Familiennamen"]
group["Calishitische_Frau"] = ["Calishitische_Frauennamen", "Calishitische_Familiennamen"]


def mensch_calishit_name(female=True):
    """
    Kleiner und schmächtiger gebaut als die meisten anderen Menschen, besitzen die Calishiten
    dunkelbraune Haut, Haare und Augen. Man findet sie hauptsächlich im Südwesten Faerüns.
    """
    if female:
        return get_name("Calishitische_Frau")
    return get_name("Calishitischer_Mann")


group["Chondathanischer_Mann"] = ["Chondathanische_Männernamen", "Chondathanische_Familiennamen"]
group["Chondathanische_Frau"] = ["Chondathanische_Frauennamen", "Chondathanische_Familiennamen"]


def mensch_chondathaner_tethyrianer_name(female=True):
    """Chondathaner sind ein schlanker Menschenschlag mit gelbbrauner Haut und dunklem Haar,
    das beinahe blond oder fast schwarz sein kann. Die meisten sind groß und besitzen grüne
    oder braune Augen, auch wenn dies nicht auf jeden zutrifft. Menschen chondathanischer
    Herkunft beherrschen die zentralen Länder von Faerün und diejenigen um die See des
    Sternenregens.

    Weit verteilt über die Schwertküste am westlichen Rand von Faerün siedeln die Tethyrianer.
    Sie sind ein Volk von mittlerer Größe und ihre dunkle Haut wird heller, je weiter man nach
    Norden kommt. Haar- und Augenfarben variieren stark, am häufigsten jedoch gibt es braune
    Haare und blaue Augen. Die Tethyrianer verwenden hauptsächlich chondathanische Namen.
    """
    if female:
        return get_name("Chondathanische_Frau")
    return get_name("Chondathanischer_Mann")


group["Damaranischer_Mann"] = ["Damaranische_Männernamen", "Damaranische_Familiennamen"]
group["Damaranische_Frau"] = ["Damaranische_Frauennamen", "Damaranische_Familiennamen"]


def mensch_damaraner_name(female=True):
    """Die primär im Nordwesten von Faerün angesiedelten Damaraner sind von mittlerer Größe
    und Statur. Ihre Haut ist von heller bis gelbbrauner Farbe, ihr Haar für gewöhnlich braun
oder schwarz. Die Augenfarbe variiert, auch wenn braune Augen am häufigsten sind."""
    if female:
        return get_name("Damaranische_Frau")
    return get_name("Damaranischer_Mann")


group["Illuskanischer_Mann"] = ["Illuskanische_Männernamen", "Illuskanische_Familiennamen"]
group["Illuskanische_Frau"] = ["Illuskanische_Frauennamen", "Illuskanische_Familiennamen"]


def mensch_illuskaner_name(female=True):
    """Illuskaner sind ein großes hellhäutiges Volk mit blauen bis hin zu stahlgrauen Augen.
     Die meisten haben rabenschwarzes Haar, nur diejenigen im äußersten Nordwesten besitzen
     blondes, rotes oder hellbraunes."""
    if female:
        return get_name("Illuskanische_Frau")
    return get_name("Illuskanischer_Mann")


group["Mulanischer_Mann"] = ["Mulanische_Männernamen", "Mulanische_Familiennamen"]
group["Mulanische_Frau"] = ["Mulanische_Frauennamen", "Mulanische_Familiennamen"]


def mensch_mulan_name(female=True):
    """Vorherrschend an der östlichen und südöstlichen Küste der Inneren See leben die schlanken,
    groß gewachsenen und bernsteinhäutigen Mulan. Sie haben braune oder hellbraune Augen
und ihre Haarfarbe reicht von Schwarz bis Dunkelbraun, wobei in Ländern, in denen die Mulan
regieren, die Adeligen und viele andere ihre Köpfe blank rasiert tragen."""
    if female:
        return get_name("Mulanische_Frau")
    return get_name("Mulanischer_Mann")


group["Rashemischer_Mann"] = ["Rashemi_Männernamen", "Rashemi_Familiennamen"]
group["Rashemische_Frau"] = ["Rashemi_Frauennamen", "Rashemi_Familiennamen"]


def mensch_rashemi_name(female=True):
    """Am häufigsten findet man die Rashemi im Osten der Inneren See und oft gemischt lebend
    mit den Mulan. Sie neigen zu einem kleinen, stämmigen und muskulösen Körperbau. Für
gewöhnlich besitzen sie dunkle Haut, dunkle Augen und dickes schwarzes Haar."""
    if female:
        return get_name("Rashemische_Frau")
    return get_name("Rashemischer_Mann")


group["Shou_Mann"] = ["Shou_Familiennamen","Shou_Männernamen"]
group["Shou_Frau"] = ["Shou_Familiennamen","Shou_Frauennamen"]


def mensch__name(female=True):
    """Die Shou sind die zahlreichste und mächtigste ethnische Gruppe in Kara-Tur, das weit
im Osten Faerüns liegt. Sie haben gelblich-bronzefarbene Haut, schwarze Haare und dunkle Augen.
Die Nachnamen werden für gewöhnlich vor den Vornamen genannt.

Ausgabe ist <<Nachname>> <<Vorname>>
"""
    if female:
        return get_name("_Frau")
    return get_name("_Mann")


group["Turami_Mann"] = ["Turami_Männernamen", "Turami_Familiennamen"]
group["Turami_Frau"] = ["Turami_Frauennamen", "Turami_Familiennamen"]


def mensch_turami_name(female=True):
    """Das an der Südküste der Inneren See beheimatete Volk der Turami ist im Allgemeinen
    groß und kräftig gebaut. Es besitzt dunkle, mahagonifarbene Haut, lockige Haare und dunkle
    Augen."""
    if female:
        return get_name("Turami_Frau")
    return get_name("Turami_Mann")


group["Barovianischer_Mann"] = ["Barovianische_Männernamen", "Barovianische_Familiennamen"]
group["Barovianische_Frau"] = ["Barovianische_Frauennamen", "Barovianische_Familiennamen"]


def mensch_barovianer_name(female=True):
    """Barovianer sind tief in ihren Heimen und Traditionen verwurzelt. Sie sind fremden
    Völkern und Bräuchen gegenüber misstrauisch. Die Art, in der Barovianer mit Fremden umgehen,
    kann für Neuankömmlinge beunruhigend sein. Barovianer tendieren dazu, offen und wortlos
    zu starren, und dadurch ihre Missbilligung für das auszudrücken, mit dem sie nicht vertraut
    sind. Sie sind nicht besonders redselig gegenüber Fremden und sind dabei schon beinahe
    bewusst unhöflich. Die meisten Barovianer weisen einen Jähzorn auf. der durch ihre übliche
    Stille hochkocht, wenn sie provoziert werden. Wird einer von ihnen misshandelt, halten sie
    meistens zusammen (oft gezwungen durch die unheimlichen Umstände ihrer Welt)."""
    if female:
        return get_name("Barovianische_Frau")
    return get_name("Barovianischer_Mann")


group["Zwergen_Mann"] = ["Zwergen_Männernamen", "Zwergen_Familiennamen"]
group["Zwergen_Frau"] = ["Zwergen_Frauennamen", "Zwergen_Familiennamen"]

def zwergen_name(female=True):
    """Der Name eines Zwerges wird ihm nach strenger Tradition von einem der Klanältesten
    verliehen. Jeder anständige Zwergenname wurde schon seit Generationen wieder und wieder
    verwendet. Ein Zwergenname gehört dem Klan, nicht dem Einzelnen.
    Missbraucht ein Zwerg seinen Namen oder bringt Schande über ihn, wird er ihm entrissen
    und es ihm per Gesetz verboten, einen anderen Zwergennamen an dessen Stelle anzunehmen."""
    if female:
        return get_name("Zwergen_Frau")
    return get_name("Zwergen_Mann")

group["Drachenblütiger_Mann"] = ["Drachenblütige_Klannamen", "Drachenblütige_Männernamen"]
group["Drachenblütige_Frau"] = ["Drachenblütige_Klannamen", "Drachenblütige_Frauennamen"]

def drachenblütiger_name(female=True):
    """Drachenblütige haben einen persönlichen Namen, der ihnen bei der Geburt gegeben wird,
    doch nennen sie als Zeichen der Ehre ihren Klannamen zuerst. Der Jugendname oder Spitzname
    wird unter guten Freunden als Ausdruck der Zuneigung verwendet und könnte an ein Ereignis
    erinnern oder auf einem Wesenszug basieren.

    ausgabe: <<klanname>> <<vorname>>

    Jugendnamen: drachengeborener_jugend_name()
    """
    if female:
        return get_name("_Frau")
    return get_name("_Mann")

def drachenblütiger_jugend_name():
    return random.choice(names["Drachenblütiger_Jugendnamen"])

group["Gnomen_Mann"] = ["Gnomen_Männernamen", "Gnomen_Familiennamen"]
group["Gnomen_Frau"] = ["Gnomen_Frauennamen", "Gnomen_Familiennamen"]

def gnomen_name(female=True):
    """Gnome lieben Namen, und die meisten besitzen davon etwa ein halbes Dutzend. Die Mutter,
    der Vater, die Klanältesten, Onkel und Tanten, jeder gibt dem Neugeborenen einen
    Namen. Dazu kommen unzählige Spitznamen, die beibehalten werden - oder eben nicht.
    Gnomische Namen sind typischer­ weise Abwandlungen von Namen der Vorfahren oder
    entfernten Verwandten, auch wenn einige völlige Neuschöpfungen sind. Falls Gnome mit
    Menschen oder anderen zu tun haben,
    die „erbsenzählerisch“ in Bezug auf Namen sind, verwenden sie nicht mehr als drei:
    den Vornamen, den Klannamen und einen Spitznamen, von denen sie sich jeweils denjenigen aus­
    suchen, dessen Aussprache am lustigsten ist.

    Spitznamen: names["Gnomen_Spitznamen"]
    """
    if female:
        return get_name("Gnomen_Frau")
    return get_name("Gnomen_Mann")

def gnomen_spitznamen():
    return random.choice(names["Gnomen_Spitznamen"])

group["Ork_Mann"] = ["Ork_Männernamen"]
group["Ork_Frau"] = ["Ork_Frauennamen"]

def halbork_name(female=True):
    """Halborks tragen für gewöhnlich einen Namen, der an die Kultur angepasst ist, in der sie
    aufwachsen. Möchte ein Halbork unter Menschen leben, könnte er seinen orkischen Namen
    ablegen und einen menschlichen annehmen. Manche Halborks mit menschlichem Namen tauschen
    diesen gegen einen kehlig klingenden orkischen Namen, da sie denken, dass dieser sie
    einschüchternder wirken lässt."""
    if female:
        return get_name("Ork_Frau")
    return get_name("Ork_Mann")

group["Tiefling_Mann"] = ["Tiefling_Männernamen"]
group["Tiefling_Frau"] = ["Tiefling_Frauennamen"]

def tiefling_name(female=True):
    """Meist tragen Tieflinge Namen, die dem Kulturkreis des Volkes angepasst sind, bei dem
    sie geboren wurden. Manche Tiefling-Eltern geben ihren Kindern auch Namen, die
    aus dem Infernalischen stammen und die seit Generationen weitergereicht wurden, um deren
    teuflische Abstammung zu betonen. Einige jüngere Tieflinge, die ihren Platz in der Welt
    noch nicht gefunden haben, nehmen einen Namen an, der eine ihrer Tugenden oder andere
    Konzepte beschreibt, die sie zu verkörpern versuchen. Manchen ist der gewählte Name eine
    edle Aufgabe, anderen eine düstere Bestimmung."""
    if female:
        return get_name("Tiefling_Frau")
    return get_name("Tiefling_Mann")

def tiefling_tugendname():
    return random.choice(names["Tiefling_Tugendnamen"])


# group["_Mann"] = ["_Männernamen", "_Familiennamen"]
# group["_Frau"] = ["_Frauennamen", "_Familiennamen"]
#
# def _name(female=True):
#     """"""
#     if female:
#         return get_name("_Frau")
#     return get_name("_Mann")

names["Elfen_Kindernamen"] = ["Ara", "Bryn", "Del", "Eryn", "Faen", "Innil", "Lael", "Mella", "Naill", "Naeris",
                              "Phann", "Rael", "Rinn", "Sai", "Syllin", "Thia", "Vall"]
names["Elfen_Familiennamen"] = ["Amakiir (Juwelblume)", "Amastacia (Sternblume)", "Galanodei (Mondflüstern)",
                                "Holimion (Diamanttau)", "Ilphelkiir (Juwelblüte)", "Liadon(Silberwedel)",
                                "Meliamne (Eichenfuß)", "Na'ilo (Nachthauch)", "Siannodel (Mondbach)",
                                "Xiloscient (Goldblatt)"]
names["Elfen_Männernamen"] = ["Adran", "Aelar", "Aramil",
                              "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan",
                              "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian",
                              "Mindartis", "Paelias", "Peren", "Quarion", "Riardon", "Rolen", "Soveliss",
                              "Thamior", "Tharivol", "Theren", "Varis"]
names["Elfen_Frauennamen"] = ["Adrie", "Althaea", "Anastrianna",
                              "Andraste", "Antinua", "Bethrynna", "Birel", "Caelynn", "Drusilia", "Enna",
                              "Felosial", "Ielenia", "Jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele",
                              "Mialee", "Naivara", "Quelenna", "Quillathe", "Sariel", "Shanairra",
                              "Shava", "Silaqui", "Theirastra", "Thia", "Vadania", "Valanthe", "Xanaphia"]
names["Halblinge_Männernamen"] = ["Alton", "Ander", "Cade", "Coorin", "Eldon",
                                  "Errich", "Finan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn",
                                  "Perrin", "Reed", "Roscoe", "Wellby"]
names["Halblinge_Frauennamen"] = ["Andry", "Bree", "Callie", "Cora", "Euphemia",
                                  "Jillian", "Kithri", "Lavinia", "Lidda. Merla", "Nedda", "Paela", "Portia",
                                  "Seraphina", "Shaena", "Trym", "Vani", "Verna"]
names["Halblinge_Familiennamen"] = ["Buschsammler", "Dickdorn", "Fallkraut", "Grünflasche",
                                    "Goldbarren", "Hochhügel", "Hügelspitz", "Strammgurt",
                                    "Teeblatt", "Unterast"]
names["Calishitische_Männernamen"] = ["Aseir", "Bardeid", "Haseid", "Khemed", "Mehmen", "Sudeiman", "Zasheir"]
names["Calishitische_Frauennamen"] = ["Atala", "Ceidil", "Hama", "Jasmal", "Meilil", "Seipora", "Yasheira", "Zasheida"]
names["Calishitische_Familiennamen"] = ["Basha", "Dumein", "Jassan", "Khalid", "Mostana", "Pashar", "Rein"]
names["Chondathanische_Männernamen"] = ["Darvin", "Dorn", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn",
                                        "Randal", "Stedd"]
names["Chondathanische_Frauennamen"] = ["Arveene", "Esvele", "Jhessail", "Kerri", "Lureene", "Miri", "Rowan", "Shandri",
                                        "Tessele"]
names["Chondathanische_Familiennamen"] = ["Schlenderkopf", "Beuchemann", "Falbdrache", "Gleichholz", "Graufeste",
                                          "Tallstag"]
names["Damaranische_Männernamen"] = ["Bor", "Fodel", "Glar", "Grigor", "Igan", "Ivor", "Kosef", "Mival", "Orel",
                                     "Pavel", "Sergor"]
names["Damaranische_Frauennamen"] = ["Alethra", "Kara", "Katernin", "Mara", "Natali", "Olma", "Tana", "Zora"]
names["Damaranische_Familiennamen"] = ["Bersk", "Chernin", "Dotsk", "Kulenov", "Marsk", "Nemetsk", "Shemov", "Starag"]
names["Illuskanische_Männernamen"] = ["Ander", "Blath", "Bran", "Frath", "Geth", "Lander", "Luth", "Malcer", "Stör",
                                      "Taman", "Urth"]
names["Illuskanische_Frauennamen"] = ["Amafrey,Betha", "Cefrey", "Kethra", "Mara", "Olga", "Silifrey", "Westra"]
names["Illuskanische_Familiennamen"] = ["Blankholz", "Helder", "Hornrabe", "Knappmann", "Sturmböe", "Flusswind"]
names["Mulanische_Männernamen"] = ["Aoth", "Bareris", "Ehput-Ki", "Kethoth", "Mumed", "Ramas", "So-Kehur", "Thazar-De",
                                   "Urhur"]
names["Mulanische_Frauennamen"] = ["Arizima", "Chathi", "Nephis", "Nulara", "Murithi", "Sefris", "Thola", "Umara",
                                   "Zolis"]
names["Mulanische_Familiennamen"] = ["Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt"]
names["Rashemi_Männernamen"] = ["Borivik", "Faurgar", "Jandar", "Kanithar", "Madislak", "Ralmevik", "Shaumar",
                                "Vladislak"]
names["Rashemi_Frauennamen"] = ["Fyevarra", "Hulmarra", "Immith", "Imzel", "Navarra", "Shevarra", "Tammith", "Yuldra"]
names["Rashemi_Familiennamen"] = ["Chergoba", "Dyernina", "Iltazyara", "Murnyethara", "Stayanoga", "Ulmokina"]
names["Shou_Männernamen"] = ["An", "Chen", "Chi", "Fai", "Jiang", "Jun", "Lian", "Long", "Meng", "On", "Shan", "Shui",
                             "Wen"]
names["Shou_Frauennamen"] = ["Bai", "Chao", "Jia", "Lei", "Mei", "Qiao", "Shui", "Tai"]
names["Shou_Familiennamen"] = ["Chien", "Huang", "Kao", "Kung", "Lao", "Ling", "Mei", "Pin", "Shin", "Sum", "Tan",
                               "Wan"]
names["Turami_Männernamen"] = ["Anton", "Diero", "Marcon", "Pieron", "Rimardo", "Romero", "Salazar", "Umbero"]
names["Turami_Frauennamen"] = ["Balama", "Dona", "Faila", "Jalana", "Luisa", "Marta", "Quara", "Selise", "Vonda"]
names["Turami_Familiennamen"] = ["Agosto", "Astorio", "Calabra", "Domine", "Falone", "Marivaldi", "Pisacar", "Ramondo"]
names["Barovianische_Männernamen"] = ["Alek", "Andrej", "Anton", "Balthasar", "Bogan",
                                      "Boris", "Dargos", "Darsin", "Dragomir", "Emerik", "Falkon", "Frederich",
                                      "Franz", "Gargosch", "Gorek", "Grigorij", "Hans", "Harkus", "Iwan", "Jirko",
                                      "Kobal", "Korga", "Kristofor", "Laszlo", "Liwius", "Marek", "Miroslaw",
                                      "Nikolaij", "Nimir", "Oleg", "Radowan", "Radu", "Seras", "Sergeij", "Stefan",
                                      "Tural", "Walentin", "Waltar", "Wasili", "Wladislaw", "Yesper", "Zsolt"]
names["Barovianische_Frauennamen"] = ["Alana", "Clawdia", "Danja", "Desdrelda",
                                      "Diawola", "Dorina", "Drascha", "Drilwia", "Elisabeta", "Fatima", "Grilscha",
                                      "Isabella", "Iwana", "Jarsinka", "Kala", "Katerina", "Keresa", "Korina",
                                      "Lawinia", "Magda", "Marta", "Mathilda", "Monodora", "Mirabel",
                                      "Miruna", "Nianka", "Nimira", "Oliwenka", "Ruxandra", "Sorina", "Terska",
                                      "Walentina", "Wascha", "Wensenzia", "Wiktoria", "Zondra"]
names["Barovianische_Familiennamen"] = ["Alastroij", "Antonowitsch/Antonowa",
                                        "Barthos", "Belasco", "Cantemir", "Dargowitsch/Dargowa",
                                        "Diawolow", "Diminskij", "Dilsnija", "Draskoij", "Garwiniki", "Grejenko",
                                        "Grosa", "Grigorowitsch/Grigorowa", "Iwanowitsch/Iwanowa",
                                        "Janek", "Karuschkin", "Konstantinowitsch/Konstantinowa",
                                        "Kreskow/Kreskowa", "Krijkskij", "Lansten", "Lazarescu", "Lukresh",
                                        "Lipsiege", "Martikow/Martikowa", "Mironowitsch/Mironowna",
                                        "Moldowar", "Nikolowitsch/Nikolowa", "Nimirowitsch/Nimirowa",
                                        "Oronowitsch/Oronowa", "Petrowitsch/Petrowna", "Polenskij",
                                        "Radowitsch/Radowa", "Rilskij", "Stefanowitsch/Stefanowa", "Strasni",
                                        "Swilowitsch/Swilowa", "Taltos", "Targolow/Targolowa", "Tyminskij",
                                        "Ulbrek", "Ulrich", "Vadu", "Voltanescu", "Zalenskij", "Zalken"]
names["Zwergen_Männernamen"] = ["Adrik", "Alberich", "Baeren", "Barendd", "Brottor",
                                "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint",
                                "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim",
                                "Rurik", "Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok",
                                "Ulfgar", "Veit", "Vondal"]
names["Zwergen_Frauennamen"] = ["Amber", "Artin", "Audhild", "Bardryn", "Dagnal",
                                "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunndola", "Gurdis", "Helja",
                                "Hlin", "Kathra", "Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn",
                                "Sannl", "Torbera", "Torgga", "Vistra"]
names["Zwergen_Familiennamen"] = ["Balderk", "Heldenhammer", "Starkamboss", "Dankil",
                                  "Feuerschmiede", "Frostbart", "Gorunn", "Holderhek", "Eisenfaust",
                                  "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]
names["Drachenblütige_Männernamen"] = ["Arjhan", "Balasar", "Bharash", "Donaar",
                                       "Ghesh", "Heskan. Kriv", "Medrash", "Mehen", "Nadarr", "Pandjed",
                                       "Patrin", "Rhogat", "Shamash", "Shedinn", "Tarhun", "Torinn"]
names["Drachenblütige_Frauennamen"] = ["Akra", "Biri", "Daar", "Farideh", "Harann", "Jheri",
                                       "Kava", "Korinn", "Mishann", "Nala", "Perra", "Raiann", "Sora", "Surina",
                                       "Thava", "Uadjit"]
names["Drachenblütige_Klannamen"] = ["Clethtinthiallor", "Daardendrian", "Delmirev",
                                     "Drachedandion", "Fenkenkabradon", "Kepeshkmolik", "Kerrhylon",
                                     "Kimbatuul", "Linxakasendalor", "Myastan", "Nemmonis", "Norixius",
                                     "Ophinshtalajir", "Prexijandilin", "Shestendeliath", "Turnuroth",
                                     "Verthisathurgiesh", "Yarjerit"]
names["Drachenblütiger_Jugendnamen"] = ["Kletterer", "Ohrenkrümmer", "Hüpfer", "Frommer",
                                        "Schildbeißer", "Eifriger"]

names["Gnomen_Männernamen"] = ["Aiston", "Alvyn", "Boddynock", "Brocc",
                               "Burgell", "Dimble", "Eldon", "Erky", "Fonkin", "Frug", "Gerbo", "Gimble",
                               "Glim", "Jebeddo", "Kellen. Namfoodle", "Orryn", "Roondar", "Seebo",
                               "Sindri", "Warryn", "Zook"]
names["Gnomen_Frauennamen"] = ["Bimpnottin", "Breena", "Caramip", "Carlin",
                               "Donella", "Duvamil", "Ella", "Ellyjobell", "Ellywick", "Lilli",
                               "Loopmottin", "Lorilla", "Mardnab", "Nissa", "Nyx", "Oda", "Orla", "Roywyn",
                               "Shamil", "Tana", "Waywocket", "Zanna"]
names["Gnomen_Familiennamen"] = ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig",
                                 "Ningel", "Raulnor", "Scheppen", "Timbers", "Türen"]
names["Gnomen_Spitznamen"] = ["Bierschwap", "Aschenherz", "Dachs", "Mantel",
                              "Doppelschloss", "Schuftenschläger", "Fnipper", "Ku", "Nim", "Einschuh",
                              "Pock", "Glitterstein", "Entenstolperer"]

names["Ork_Männernamen"] = ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh",
                            "Keth", "Krusk", "Mhurren", "Ront", "Shump", "Thokk"]
names["Ork_Frauennamen"] = ["Baggi", "Emen", "Engong", "Kansif", "Myev",
                            "Neega", "Ovak", "Ownka", "Shautha", "Sutha", "Vola", "Volen", "Yevelda"]

names["Tiefling_Männernamen"] = ["Akmenos", "Amnon", "Barakas",
                                 "Damakos", "Ekemon", "Iados", "Kairon", "Leucis", "Melech", "Mordai",
                                 "Morthos", "Pelaios", "Skamos", "Therai"]
names["Tiefling_Frauennamen"] = ["Akta", "Anakis", "Bryseis",
                                 "Criella", "Damaia", "Ea", "Kallista", "Lerissa", "Makaria", "Nemeia",
                                 "Orianna", "Phelaia", "Rieta"]
#names["Tiefling_Familiennamen"] = [""]
names["Tiefling_Tugendnamen"] = ["Aas", "Aufgabe", "Bedauern", "Exzellenz", "Frechheit",
                                 "Furcht", "Gebet", "Hoffnung", "Hoffnungslos", "Kredo", "Kunst",
                                 "Müde", "Musik", "Nirgendwo", "Offen", "Poesie", "Qual", "Ruhm", "Verehrung",
                                 "Vorbild", "Zufall"]
# names["_Männernamen"] = [""]
# names["_Frauennamen"] = [""]
# names["_Familiennamen"] = [""]
