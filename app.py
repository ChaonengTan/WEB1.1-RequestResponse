from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """takes in 2 strings and displays a funny (but work-appropriate) story using them"""
    return f'Do you know about how Joe went on a date with a {adjective} {noun}?'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """takes in 2 numbers, multiplies them, and displays the results"""
    if number1.isdigit() and number2.isdigit():
        return f'{number1} times {number2} is {int(number1)*int(number2)}'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """repeat a string a given number of times"""
    return f'{word*int(n)}'

@app.route('/dicegame')
def dicegame():
    """chooses a random number from 1 to 6. If the user rolls a 6, they win the game; otherwise, they lose."""
    roll = random.randint(1,6)
    if roll==6:
        return 'You rolled a 6. You won!'
    else:
        return f'you rolled a {roll}. you lost.'

if __name__ == '__main__':
    app.run(debug=True)
