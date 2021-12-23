import flask 
from flask_mysqldb import MySQL
import requests
# sudo docker run --network=host --add-host host.docker.internal:127.0.0.1  -p 5000:5000 --name flask_host -v /home/msr/estudo/docker/python_host:/app/ --rm python_host

app = flask.Flask(__name__)
app.config['DEBUG'] = True

app.config['MYSQL_HOST'] = 'host.host.local'
app.config['MYSQL_USER'] = 'msr'
app.config['MYSQL_PASSWORD'] = '98653274Mm@'
app.config['MYSQL_DB'] = 'flaskhost'


mysql = MySQL(app)

@app.route('/', methods=['GET'])
def index():
  data = requests.get('https://randomuser.me/api')
  return data.json()


@app.route('/inserthost', methods=['POST'])
def inserthost():
  data = requests.get('https://randomuser.me/api')
  data = data.json()
  username = data['results'][0]['name']['first']

  cursor = mysql.connection.cursor()
  cursor.execute("""INSERT INTO users(name) VALUES(%s)""", (username,))
  mysql.connection.commit()
  cursor.close()

  return username


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port='5000')