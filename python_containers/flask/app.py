import flask 
from flask_mysqldb import MySQL
import requests
# sudo docker run -p 3306:3306 --name mysql_api_container --rm --network flasknetwork -e MYSQL_ROOT_PASSWORD=98653274M mysql_python
# sudo docker run  -p 5000:5000 --name python_container -v /home/msr/estudo/docker/python_containers/flask/:/app/ --rm python_host

app = flask.Flask(__name__)
app.config['DEBUG'] = True

app.config['MYSQL_HOST'] = 'mysql_api_container'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '98653274M'
app.config['MYSQL_DB'] = 'flaskdocker'


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