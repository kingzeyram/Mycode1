from flask import *
import pymysql

app = Flask(__name__)

app.secret_key='9TkrsiwDvO'
@app.route('/')
def home():
    #establish db connection
    conn = pymysql.connect(host='localhost',user='root',password='',database='soko2')

    #cars
    cursor = conn.cursor()
    sql1 = "select * from table1 where item_category ='cars'"
    cursor.execute(sql1)
    rows = cursor.fetchall()

    #buses
    cursor = conn.cursor()
    sql2 = "select * from table1 where item_category ='buses'"
    cursor.execute(sql2)
    rows = cursor.fetchall()

    #trucks
    cursor = conn.cursor()
    sql3 = "select * from table1 where item_category ='trucks'"
    cursor.execute(sql3)
    rows = cursor.fetchall()

    return render_template('index.html')

@app.route('/blog')
def blog():

    return render_template('blog.html')

if (__name__) == ('__main__'):
    app.run(debug= True)