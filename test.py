from flask import Flask , request, jsonify
import mysql.connector as conn
app = Flask(__name__)

mydb = conn.connect(host = "127.0.0.1", user = "root", password = "We******e123")
cursor = mydb.cursor()

# 1 . Write a program to insert a record in sql table via api
@app.route('/load_dress', methods=['GET','POST'])
def load_dress_data():
    print("START loading data ")
    try:
        Dress_ID = request.json['Dress_ID']
        Style = request.json['Style']
        Price = request.json['Price']
        Rating = request.json['Rating']
        Size = request.json['Size']
        Season = request.json['Season']
        NeckLine = request.json['NeckLine']
        waiseline = request.json['waiseline']
        Material = request.json['Material']
        print( Dress_ID ,Style, Price ,Rating , Size  , Season  ,NeckLine  ,waiseline ,Material )
        sql = (
        "INSERT INTO sales.dress_dataset (Dress_ID,Style,Price,Rating,Size,Season,NeckLine,waiseline,Material) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        value = [ Dress_ID,Style,Price,Rating,Size,Season,NeckLine,waiseline,Material]
        cursor.execute(sql, value)
        mydb.commit()
        return ("Succcessfully Data Loaded")
    except Exception as e:
        print(e)
        return ("System is under maintanance")
    return ("Please check your data and load again")


# 2.  Write a program to update a record via api
@app.route('/update_dress', methods=['GET','POST'])
def update_dress_data():
    print("START loading data ")
    try:
        Dress_ID = request.json['Dress_ID']
        Style = request.json['Style']
        Price = request.json['Price']
        Rating = request.json['Rating']
        Size = request.json['Size']
        Season = request.json['Season']
        NeckLine = request.json['NeckLine']
        waiseline = request.json['waiseline']
        Material = request.json['Material']
        print( Dress_ID ,Style, Price ,Rating , Size  , Season  ,NeckLine  ,waiseline ,Material )

        cursor.execute("""
           UPDATE sales.dress_dataset
           SET Style=%s,Price=%s,Rating=%s,Size=%s,Season=%s,NeckLine=%s,waiseline=%s,Material=%s
           WHERE Dress_ID=%s
        """, (Style,Price,Rating,Size,Season,NeckLine,waiseline,Material,Dress_ID))
    except Exception as e:
        print(e)
        return ("Record got updated")

# 3.Write a program to delete a record via api
@app.route('/delete_dress', methods=['GET', 'POST'])
def delete_dress_data():
    print("START Delete data ")
    try:
        Dress_ID = request.json['Dress_ID']
        print(Dress_ID)
        sql_Delet_query = """Delete from sales.dress_dataset where Dress_ID = %s"""
        cursor.execute(sql_Delet_query,(Dress_ID,))

        mydb.commit()
        return ("Succcessfully Deleted data")
    except Exception as e:
        print(e)
        return ("System is under maintanance")
    return ("Please check your data and load again")

# 4 . Write a program to fetch a record via api
@app.route('/retrive_dress', methods=['GET','POST'])
def retrieve_dress_data():
    print("START Retriving data ")
    try:
        Dress_ID = request.args.get('Dress_ID', None)
        sql_Selete_query = """Select * from sales.dress_dataset where Dress_ID = %s"""
        cursor.execute(sql_Selete_query, (Dress_ID,))
        record = cursor.fetchall()
        return jsonify(str(record))
    except Exception as e:
        print(e)
        return ("System is under maintanance")
    return ("Please check your data and load again")




@app.route('/abc',methods=['GET' ,'POST'])
def test1():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify((str)(result))

@app.route('/abc1/mani',methods=['GET' ,'POST'])
def test2():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify((str)(result))


if __name__=='__main__'  :
    app.run()
