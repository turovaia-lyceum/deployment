import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                  <div class="row">
                    <div class="col-md-8 mx-auto">
                      <h1>Кто ищет, тот всегда найдет!</h1>
                       <h3 style=color:white>Вы почти выиграли!</br>
                       Осталось дружно всей командой (это важно!!) два раза хлопнуть, один раз топнуть и громко крикнуть: "Пайтон!"
                       </h3>
                    </div>
                  </div>
               </body>"""


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', port)
