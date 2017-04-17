from flask import Flask, Response, request
import requests
import hashlib
import redis
import html

app = Flask(__name__)
# SET REDIS STRING CONNECTION AND DATABASE
cache = redis.StrictRedis(host='redis')

salt = "jgkH02e8lM"
default_name = 'Ebury'


@app.route('/', methods=['GET', 'POST'])
def mainpage():

    name = default_name
    if request.method == 'POST':
        name = html.escape(request.form['name'], quote=True)

    salted_name = salt + name
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest()
    header = '<html><head><title>Ebury Login</title></head><body>'
    body = '''<form method="POST">
              Hello <input type="text" name="name" value="{0}">
              <input type="submit" value="submit">
              </form>
              <p>You look like a:
              <img src="/monster/{1}"/>
              '''.format(name, name_hash)
    footer = '</body></html>'

    return header + body + footer


@app.route('/monster/<name>')
def get_identicon(name):

    name = html.escape(name, quote=True)
    image = cache.get(name)
    if image is None:
        print ("Cache miss", flush=True)
        # SET DNMONSTER IMAGE CONNECTION TO USE ON HOST VARIABLE
        r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
        image = r.content
        cache.set(name, image)

    return Response(image, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')