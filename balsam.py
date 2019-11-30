
import random

adverb = [
    "einfach",
    "äußerst",
    "überaus",
    "durchaus",
    "im besten Sinne",
    "ohne Frage",
    "relativ",
    "atemberaubend",
    "unglaublich",
    "regelrecht",
    "definitiv",
    "radikal",
    "leicht",
    "maximal",
    "positiv",
    "selten",
    "spürbar",
    "stark",
    "schamlos",
    "krass",
    "echt",
    "übertrieben",
    "mindestens",
    "(alle sagen das!)",
    "nichts anderes als",
    "- das darf man wohl sagen -",
    "allen Unwiedrigkeiten zu trotz",
    "derbe",
    "absolut",
    "eigentlich",
    "im kantschen Sinne",
    "wenn man es genau nimmt",
    "erfrischend",
    "sehr",
    "zutiefst",
    "ein wenig",
    "überwiegend",
    "selbst in schwachen Momenten",
    "gerade wenn man es am wenigsten erwartet",
    "seit Jahren schon",
    "auch für Experten",
    "gelegentlich", 
    "gewaltig",
    "gründlich"

    ]

adjektiv = [
    "mit nichts anderem vergleichbar",
    "das wovon ich meinen Enkeln noch erzählen werde",
    "nachahmenswürdig",
    "gern gesehen",
    "preisverdächtig",
    "präsentabel",
    "eines Kultusministers würdig",
    "kultiviert",
    "ausgefeilt",
    "mondän",
    "filigran",
    "kompliziert",
    "ausgeklügelt",
    "differenziert",
    "von großem Tiefgang",
    "hip",
    "angesagt",
    "jazzig",
    "feierlich",
    "freiheitlich",
    "delikat",
    "gewagt",
    "großartig",
    "das Beste vom Besten",
    "eine Reise wert",
    "was für Kenner",
    "schön",
    "sexy",
    "entwickelt",
    "überentwickelt",
    "wunderbar",
    "angenehm",
    "atemberaubend",
    "intelligent",
    "Balsam für die Seele",
    "fesselnd",
    "faszinierend",
    "umwerfend",
    "der Grund für so viel Gutes",
    "einfühlsam",
    "groovy",
    "sauber",
    "wertvoll",
    "feminin",
    "unglaublich",
    "ordentlich",
    "hochwertig",
    "edel",
    "geil",
    "bezaubernd",
    "liebenswert",
    "lieblich",
    "profund",
    "dramatisch",
    "logisch",
    "ausgezeichnet",
    "weltberühmt",
    "zuckersüß",
    "die Rettung",
    "unterschätzt",
    "magisch",
    "positiv",
    "animalisch",
    "anmutig",
    "anregend",
    "anspruchsvoll",
    "anziehend",
    "aphrodisierend",
    "athletisch",
    "attraktiv",
    "aufreizend",
    "außergewöhnlich",
    "außerordentlich",
    "bedeutend",
    "beeindruckend",
    "beflügelt",
    "befreiend",
    "begehrenswert",
    "begeisternd",
    "beglückend",
    "berauschend",
    "berühmt",
    "besonders",
    "bewundernswert",
    "brillant",
    "charismatisch",
    "charmant",
    "dominant",
    "duftend",
    "dynamisch",
    "echt",
    "ehrlich",
    "einfühlsam",
    "einzigartig",
    "ekstatisch",
    "elegant",
    "emotional",
    "empfehlenswert",
    "entzückend",
    "erfrischend",
    "erhellend",
    "erotisch",
    "erregend",
    "erstaunlich",
    "erstklassig",
    "exklusiv",
    "extravagant",
    "exzellent",
    "fabelhaft",
    "fantastisch",
    "faszinierend",
    "fein",
    "fesselnd",
    "frisch",
    "geheimnisvoll",
    "geschmackvoll",
    "gigantisch",
    "grandios",
    "grenzenlos",
    "harmonisch",
    "heißblütig",
    "herrlich",
    "hervorragend",
    "hübsch",
    "humorvoll",
    "ideal",
    "imponierend",
    "krass",
    "intensiv",
    "interessant",
    "komfortabel",
    "königlich",
    "eine Kostbarkeit",
    "kraftvoll",
    "kunstvoll",
    "lebhaft",
    "luxuriös",
    "mächtig",
    "märchenhaft",
    "mitreißend",
    "mysteriös",
    "ein Mythos",
    "perfekt",
    "persönlich",
    "phänomenal",
    "phantastisch",
    "pikant",
    "potent",
    "prächtig",
    "das pralle Leben",
    "rasant",
    "reizend",
    "selbstlos",
    "selbstsicher",
    "sensationell",
    "sensibel",
    "spannend",
    "spektakulär",
    "stilvoll",
    "sympathisch",
    "traumhaft",
    "überlegen",
    "überwältigend",
    "unfassbar",
    "unglaublich",
    "unsterblich",
    "unwiderstehlich",
    "verblüffend",
    "verführerisch",
    "verlockend",
    "vital",
    "warm",
    "wild",
    "wohlklingend",
    "wohlriechend",
    "zärtlich",
    "zuverlässig",
    "zwischenmenschlich",
    ]







nomen = [ 
    "Nase", 
    "Oberschenkel",
    "Intellekt", 
    "Zahnfleisch",
    "Großmut",
    "Haare",
    "Kochkünste",
    "guter Geschmack",
    "Edelmut",
    "Wangeknochen",
    "Deutschkentnisse",
    "Wimpern",
    "rechte Wange",
    "Fahrrad",
    "Risotto",
    "Seele",
    "Leben",
    "Sinn für Gerechtigkeit",
    "Ideen",
    "Gnocchi",
    "Unterschenkel",
    "Knie",
    "Timing",
    "Esprit",
    "Partys",
    "Gesicht",
    "Augenbrauen",
    "Brüste",
    "Sex-Appeal",
    "Phantasie",
    "Achselhaare",
    "Ohrläppchen",
    "Inneneinrichtung",
    "Musikgeschmack",
    "Programmierstil",
    "Fahrstil",
    "Pferd",
    "Essverhalten",
    "Bildung",
    "Benehmen",
    "Ruf",
    "Pupillen",
    "Wimpern",
    "Stirnfalten",
    "Unterlippe",
    "Daumen",
    "Abendgaderobe",
    "Umgang mit Lebensmitteln",
    "Lebenserfahrung",
    "Bestimmheit",
    "Konsumverhalten",
    "Verdauung",
    "Durchaltevermögen",
    "Frustrationstoleranz",
    "Gefühl für Situationskomik",
    "Fähigkeit Regentage auszusitzen",
    "Elan",
    "Schuhwerk",
    "Schlafrythmus",
    "Telefonstimme",
    "Verachtung für Begigni",
    "Brillengestell",
    "Comicsammlung",
    "aufklappbares Modell des Millennium Falcon",
    "Hausschuhe",
    "Waden",
    "Zehennägel",
    "Tattoos",
    "Hunger auf Literatur",
    "Trinkfestigkeit",
    "Selbstironie",
    "Nachttischlampe",
    "Zimmerpflanzen",
    "Portfolio",
    "Schreibstil",
    "Einstellung zu Leistungsdruck",
    "Einfühlungsvermögen",
    "Art Brot zu toasten",
    "Gelassenheit",
    "Pünktlichkeit",
    "Flirtstil",
    "kaufmännisches Geschick",
    "Risikofreude",
    "Willenstärke",
    "Wissen zu Immunologie",
    "Stoizismus",
    "Abgebrühtheit",
    "Niveau",
    "Optimismus",
    "Bauchgefühl",
    "Auftreten",
    "Eloquenz",
    "Temperament",
    "Mundhygiene",
    "Stimme",
    "Passion für Absonderliches",
    "Wiederworte",
    "Kinnhaken",
    "Umgang mit Ignoranz",
    "Mixtapes"
    ]

artikel = ["Dein", "Deine"]
verb = ["ist", "sind"]
# ordnet nomen passende artikel und verben zu




nomen_typ = [
    (1, 0),
    (1, 1),
    (0, 0),
    (0, 0),
    (0, 0),
    (1, 1),
    (1, 1),
    (0, 0),
    (0, 0),
    (1, 1),
    (1, 1),
    (1, 1),
    (1, 0),
    (0, 0),
    (0, 0),
    (1, 0),
    (0, 0),
    (0, 0),
    (1, 1),
    (1, 1),
    (1, 1),
    (1, 1),
    (0, 0),
    (0, 0),
    (1, 1),
    (0, 0),
    (1, 1),
    (1, 1),
    (0, 0),
    (1, 0),
    (1, 1),
    (1, 1),
    (1, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (1, 0),
    (0, 0),
    (0, 0),
    (1, 1),
    (1, 1),
    (1, 1),
    (1, 0),
    (1, 1),
    (1, 0),
    (0, 0),
    (1, 0),
    (1, 0),
    (0, 0),
    (1, 0),
    (0, 0),
    (1, 0),
    (0, 0),
    (1, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (1, 0),
    (0, 0),
    (0, 0),
    (1, 0),
    (0, 0),
    (1, 1),
    (1, 1),
    (1, 1),
    (1, 1),
    (0, 0),
    (1, 0),
    (1, 0),
    (1, 0),
    (1, 1),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (1, 0),
    (1, 0),
    (0, 0),
    (0, 0),
    (1, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (1, 0),
    (0, 0),
    (1, 0),
    (1, 0),
    (1, 0),
    (1, 1),
    (0, 0),
    (0, 0),
    (1, 1)
    ]

def make_php():

    code =  '<?php\n\n'
    code += "$compliments = array(" 

    for i in range( 100): # get_combinations()):
        code += '\''
        code += flatter()
        code += '\'; '
    #'coffee', 'brown', 'caffeine');
    code += ");\n"
    code += "\n"
    code += "echo array_rand($compliments, 1);"
    code += "\n\n?>"
    return code

def make_javascript(n):
    code  = '<script type="text/javascript" charset="utf-8">\n'
    code += '    var randomStrings = [\n'
    for i in range(n): # get_combinations()):
        code += '        "'
        code += flatter()
        code += '",\n'
    # without last comma
    code += '    ];\n\n'
    code += '    var randomDiv = document.getElementById("myRandomDiv");\n\n'
    code += '    document.getElementById("myButton").addEventListener("click", function() {\n'
    code += '        randomIndex = Math.ceil((Math.random()*randomStrings.length-1));\n'
    code += '        newText = randomStrings[randomIndex];\n'
    code += '        randomDiv.innerHTML = newText;\n'
    code += '});\n'
    code += '</script>\n'
    return code

def print_html(part):
    if part == "head":
        html = '''
<!DOCTYPE html>
<html>

  <head>
    <meta charset="UTF-8">
    <title>Balsam für die Seele</title>
    <link rel="stylesheet" type="text/css" href="main.css">
    <link rel="shortcut icon" href="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/htc/37/cherry-blossom_1f338.png">
  

    <style type="text/css">
      #myoutercontainer { position:relative }
      #myinnercontainer { position:absolute; top:50%; height:10em; margin-top:-5em }
      h5 {text-decoration: underline;}
      div {
        height: 600px;
        padding: 0px 0;
        text-align: center;
        border: 0px dashed #f69c55;
        }
      #parent {
        padding: 5% 0;
        }
      #child {
        padding: 10% 0;
        }
      #myButton {
        font-size: xx-large;
      }
      #myRandomDiv {
        font-weight: bold;
        font-style: italic;
      }
    </style>
    </head>

    <body>'''
    if part == "div":
        html = '''
<div id="parent">
  <div id="child">
    <a id="myButton" href="#" style="text-decoration:none">🌸</a>
    <p> 
        Was ich dir immer schonmal sagen wollte:<br>
        <div id="myRandomDiv"></div>
    </p>
  </div>
</div>'''
    if part == "tail":
        html = '''
    <footer style="position:fixed; text-align:right; bottom: 20px; right: 10px; height:20px; width:100%;">
        <p>(Blume klicken!)</p>
    </footer>
    </body>

</html>'''
    return html



def flatter():
    n = random.randint(0, len(nomen) - 1)
    a, v = nomen_typ[n]
    if bool(random.getrandbits(1)):
        extra = random.choice(adverb) + " "
    else:
        extra = ""
    compliment = artikel[a] + " " + nomen[n] + " " + verb[v] + " " + extra + random.choice(adjektiv) + "."
    return compliment

def get_combinations():
    return len(nomen) * len(adjektiv) * (len(adverb) + 1)

def print_bestand():
    print("Bestand:")
    print("\tNomen:     ", len(nomen), "(" + str(len(nomen_typ)) + ")")
    print("\tAdjektive: ", len(adjektiv))
    print("\tAdverben:  ", len(adverb))
    print(str(get_combinations()) + " mögliche Kombinationen." )
    print()
    print()

def generate_some():
    print_bestand()

    print("Was ich dir immer schon mal sagen wollte:\n")

    for i in range(20):
        print(flatter() + "\n")

def make_page():
    print(print_html("head"))
    print()
    print(print_html("div"))
    print()
    print()
    print(make_javascript(200000))
    print()
    print(print_html("tail"))

generate_some()

#make_page()


# maybe include other type of sentences as for example "you make me/everybody feel **** ", "you are ****"
# inspiration: http://toykeeper.net/programs/mad/compliments
