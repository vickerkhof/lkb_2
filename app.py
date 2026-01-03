from flask import Flask, render_template, json

app = Flask(__name__)

# Use just the filenames. This works if they are in the same folder.
MOVES_FILE = 'moves.json'
GAMES_FILE = 'games.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/moves')
def get_moves():
    try:
        with open(MOVES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": "moves.json not found in the script folder"}, 404

@app.route('/api/games')
def get_games():
    try:
        with open(GAMES_FILE, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "result,moves,accuracy,opponent_rating\n", 404

if __name__ == '__main__':
    app.run(debug=True)
