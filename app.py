from flask import Flask, request,render_template_string
import random
app = Flask(__name__)
jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "Why couldn't the bicycle stand up by itself? It was two-tired.",
    "What do you get when you cross a cow and a duck? Milk and quackers!",
    "Why are ghosts bad at lying? Because they are too transparent.",
    "Why don't programmers like nature? It has too many bugs.",
    "What’s orange and sounds like a parrot? A carrot."
]
HTML_TEMPLATE = '''
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background: #e3e3e3;
            margin: 10px 0;
            padding: 15px;
            border-radius: 5px;
        }
        .number {
            font-weight: bold;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="joke-container">
        <h1>Random Jokes</h1>
        <ul>
            {% for number, joke in jokes.items() %}
                <li><span class="number">{{ number }}:</span> {{ joke }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
'''
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"
@app.route('/jokes', methods=['GET'])
def get_jokes():
    num_jokes = int(request.args.get('num', 5)) 
    if num_jokes > len(jokes):         
        num_jokes = len(jokes)
    selected_jokes = random.sample(jokes, num_jokes)
    numbered_jokes = {i + 1: joke for i, joke in enumerate(selected_jokes)}
    return render_template_string(HTML_TEMPLATE, jokes=numbered_jokes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)