from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal

app = Flask(__name__)
application = app

# create a list of dicts from a CSV
pokemons_list = convert_to_dict("pokemon_cards.csv")

# create a list of tuples in which the first item is the rank
# (Pokemon) and the second item is the name (Pokemon)
pairs_list = []
for p in pokemons_list:
    pairs_list.append( (p['Rarity'], p['Pokemon']) )

# first route

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="Pokemon Index")

# second route

@app.route('/pokemon/<num>')
def detail(num):
    try:
        pokemon_dict = pokemons_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for Pokemon: {num}</h1>"
    # a little bonus function, imported on line 2 above
    ord = make_ordinal( int(num) )
    return render_template('pokemon.html', pokemon_dict=pokemon_dict, ord=ord, the_title=pokemon_dict['Pokemon'])


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)