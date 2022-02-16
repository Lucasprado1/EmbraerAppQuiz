from flask import Flask
import pymysql.cursors
from flask_restful import reqparse, abort, Api, Resource
import pymysql
import random

####### inicio conexão para o banco #######

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             database='mydb');
cursor = connection.cursor();


####### fim da conexão com banco ########


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('pergunta')
parser.add_argument('alternativa1')
parser.add_argument('alternativa2')
parser.add_argument('alternativa3')


# Todo
# shows a single todo item and lets you delete a todo item
class Perguntas(Resource):

    def get(self):
        lista = []
        for x in range(5):
            sql_query = "SELECT * FROM mydb.perguntas WHERE `idperguntas`= "+str(random.randrange(4, 19))+""
            cursor.execute(sql_query)
            data = cursor.fetchone()
            lista.append(data)
        return lista, 201

    def post(self):
        args = parser.parse_args()
        sql_query = "INSERT INTO `mydb`.`perguntas` (`conteudo_pergunta`) VALUES ('"+args['pergunta']+"')"
        cursor.execute(sql_query)
        connection.commit()
        sql_query = "SELECT `idperguntas` FROM `mydb`.`perguntas` ORDER BY `idperguntas` DESC LIMIT 1"
        cursor.execute(sql_query)
        data = cursor.fetchone()
        print(data[0])
        sql_query = "INSERT INTO `mydb`.`alternativas` (`perguntas_idperguntas`,`conteudo_alternativa`) VALUES ("+str(data[0])+" ,'"+args['alternativa1']+"')"
        cursor.execute(sql_query)
        sql_query = "INSERT INTO `mydb`.`alternativas` (`perguntas_idperguntas`,`conteudo_alternativa`) VALUES ("+str(data[0])+" ,'"+args['alternativa2']+"')"
        cursor.execute(sql_query)
        sql_query = "INSERT INTO `mydb`.`alternativas` (`perguntas_idperguntas`,`conteudo_alternativa`) VALUES ("+str(data[0])+" ,'"+args['alternativa3']+"')"
        cursor.execute(sql_query)
        connection.commit()
        return data, 201

    def delete(self):
        pass


class Alternativas(Resource):

    def post(self):
        pass

class Quiz(Resource):

    def get(self):
        pass

api.add_resource(Perguntas, '/pergunta')

if __name__ == '__main__':
    app.run(debug=True)
