from os import system, name


clr = lambda: system('cls' if name == 'nt' else 'clear')

questions = [
    ['How many planets are there in the solar system?', '8'],
    ['How many continents are there?', '7'],
    ['What is the largest planet in our solar system?', 'Jupiter'],
    ['Which planet is known as the Red Planet?', 'Mars'],
    ['How many legs does a spider have?', '8'],
    ['What is the capital of France?', 'Paris'],
    ['How many fingers are on one hand?', '5'],
    ['What color is the sky on a clear day?', 'Blue'],
    ['What is 9 divided by 3?', '3'],
    ['What is the largest ocean on Earth?', 'Pacific']
]
