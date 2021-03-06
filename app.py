from bottle import route, run

codes = {
    "A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
    "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett",
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
    "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee",
    "Z": "Zulu"
}

@route('/')
def index():
    return '<html><body>hello</body></html>'

@route('/nato')
def nato():
    return codes


@route('/nato/<letter>')
def code(letter):
    return codes[letter.capitalize()]

run(host="0.0.0.0", port="8080")
