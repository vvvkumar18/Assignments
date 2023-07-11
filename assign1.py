from flask import Flask, request
import mysql.connector

app = Flask(__name__)
output = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kumar@1234567",
    database="database7"
)

@app.route("/")
def data1():
    return "Welcome"

@app.route('/travel', methods=['POST'])
def insert():
        data = request.get_json()
        id = data['id']
        name = data['name']
        place = data['place']
        user_drop = data['destination']
        cursor = output.cursor()
        sql = "INSERT INTO travel (id,name,place,destination) VALUES (%s, %s, %s, %s)"
        values = (id, name, place, user_drop)
        cursor.execute(sql, values)
        output.commit()
        return("Data Insert Success")


@app.route('/travel/<int:id>', methods=['PUT'])
def update(id):
        data = request.get_json()
        name = data['name']
        place = data['place']
        user_drop = data['destination']
        cursor = output.cursor()

        sql = "UPDATE travel SET name = %s, place = %s, destination = %s WHERE id = %s"
        values = (name, place, user_drop, id)
        cursor.execute(sql, values)
        output.commit()

        return("Data Update Success")

@app.route('/travel', methods=['GET'])
def select():
        cursor = output.cursor()
        sql = "SELECT id, name, place, destination FROM travel"
        cursor.execute(sql)
        result = cursor.fetchall()
        travels = []
        for row in result:
            travel = {
                "ID": row[0],
                "Name": row[1],
                "Place": row[2],
                "Destination": row[3]
            }
            travels.append(travel)

        return(travels)


    


@app.route('/travel/<int:id>', methods=['GET'])
def select_travel(id):
        sql = "SELECT id, name, place, destination FROM travel WHERE id = %s"
        value = (id,)
        cursor = output.cursor()
        cursor.execute(sql, value)
        row = cursor.fetchone()
        if row:
            travel = {
                "ID": row[0],
                "Name": row[1],
                "Place": row[2],
                "Destination": row[3]
            }
            return(travel)
        else:
            return "Travel not found", 404
       
   



    
@app.route('/travel/<int:id>', methods=['DELETE'])
def delete(id):
        cursor = output.cursor()
        sql = "DELETE FROM travel WHERE id = %s"
        value = (id,)
        cursor.execute(sql, value)
        output.commit()

        return("Data Delete Success")
    
if __name__ == '__main__':
    app.run()
