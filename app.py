from flask import Flask, render_template, request
import json

app = Flask(__name__)

f = open('data.json')
pokemons = json.load(f)
# /users
# /users/mani
# URL parameters

# Query parametes
# /users/john?name=asd;age=34

# pokemons/pikachu
# pokemons/?name=pikachu


@app.route("/")
def home_page():
    name = 'mani'
    names = []
    return render_template('home.html', names=names, n=name, age=45)

# /pokemons
# /pokemons/charmander
# /pokemons?name=pikachu
# /pokemons

# /pokemons?name=charmander


@app.route("/pokemons")
def pokemons_route():
    # print(request.args['name'])
    pokemon_name = request.args.get('name')
    if pokemon_name:
        pokemon = None
        for poke in pokemons:
            if poke['name'] == pokemon_name:
                pokemon = poke
        return render_template('single_pokemon.html', pokemon=pokemon)

    names = [poke['name'] for poke in pokemons]
    return render_template('pokemons.html', names=names)


@app.route("/pokemons/<pokemon_name>")
def single_pokemon_route(pokemon_name):
    print("pokemon name: ", pokemon_name)
    pokemon = None
    for poke in pokemons:
        if poke['name'] == pokemon_name:
            pokemon = poke

    return render_template('single_pokemon.html', pokemon=pokemon)


@app.route("/about")
def about_page():
    print('query parameters: ', request.args)

    print('got a request to about page')
    return '<h1> About Page</h1>'


@app.route("/addproduct", methods=['GET', 'POST'])
def add_product_page():
    print('Method Type: ', request.method)
    is_submited = False

    if request.method == 'GET':
        print('This is get request')

    if request.method == 'POST':
        print('This is post request')
        print('form', request.form)
        name = request.form.get('product_name')
        is_submited = True
        print('Submitted name is ', name)

    return render_template('add_product.html', is_submited=is_submited)


if __name__ == "__main__":
    app.run(debug=True)
