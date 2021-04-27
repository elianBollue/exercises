# Write your code here
morse_tabel = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}

inverse_morse = dict((y,x) for x,y in morse_tabel.items())

def to_morse(string):
    return '   '.join([' '.join([morse_tabel[char] for char in word]) for word in string.upper().split(' ')])

def from_morse(string):
    return ' '.join([''.join([inverse_morse[char] for char in woord.split(' ')]) for woord in string.split('   ')])