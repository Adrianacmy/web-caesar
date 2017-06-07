
form = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <title></title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="style.css" rel="stylesheet">
        <style>
            form {{
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }}

        textarea {{
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }}
        </style>
    </head>
    <body>
        <form method='post'>
            <label for="rot">Rotate by:</label>
            <input id='rot' type="text" name="rot" value='0'>
            <textarea name="text">{0}</textarea>
            <input type="submit">
        </form>
    </body>
</html>

'''



from flask import Flask, request
from caesar import rotate_character, encrypt_c

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return form.format('')

@app.route('/', methods=['POST'])
def encrypt():
    #Be skeptical about user input
    try:
        rot = int(request.form['rot'])
        text = request.form['text']
    except ValueError:
        return index()

    encrypted = encrypt_c(text, rot)
    return form.format(encrypted)
   


app.run()