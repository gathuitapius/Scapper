from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup
import requests
import re
import mysql.connector


app = Flask('__name__')


def conn_db(host, user, password):
     database = "cars_db"
     conn = mysql.connector.connect(
          host= host,
          user = user,
          password = password
          )
     cursor = conn.cursor()
     sql = f"CREATE DATABASE IF NOT EXISTS {database}"
     
     cursor.execute(sql)

     return conn

@app.route("/")
def index():
    return "Welcome home"

@app.route("/data")
def get_data_from_URL():
    url="https://jiji.co.ke/"
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    cars = soup.findAll('div', class_='b-listing-cards__item')

    car_list = []

    for car in cars:
        # Get Car image
        img_url = car.find('div', class_='fw-card-media')
        img = img_url['style']
        img_match_1 = re.findall(r'url\((.*?)\)', img)[0]
        img_match = re.findall(r'url\((.*?)\)', img)[0]

        #Get car price
        price_div = car.find('div', class_='b-trending-card__price')
        price = int(price_div.text.split()[1].replace(",", ""))


        #Get Description
        name_tag = car.find('div', class_='fw-card-content')
        name = name_tag.find('div', class_='b-trending-card__title').text
        name_arr = name.split()
        car_name = ""
        conn = conn_db('localhost', 'root', 'root')

        for n in name_arr:
                car_name += n + ' '

        car_list.append(
            {
                "img_url" : img_match,
                "name" : car_name,
                "price": price
                })
        
        if conn:
                cursor = conn.cursor()
                cursor.execute("USE cars_db")
                sql ="""
                CREATE TABLE IF NOT EXISTS cars(
                id INT PRIMARY KEY AUTO_INCREMENT,
                img_url VARCHAR(100),
                name VARCHAR(100),
                price INT
                )
                """
                cursor.execute(sql)
                insert_sql = "INSERT INTO cars(img_url,name,price) VALUES(%s,%s,%s)"
                val = (img_match,car_name,price)
                cursor.execute(insert_sql, val)

                conn.commit()     
    return render_template("cars.html", cars=cars)



@app.route("/cars")
def get_all_items():
     conn = conn_db('localhost', 'root', 'root')
     if conn:
        cursor = conn.cursor()
        cursor.execute("USE cars_db")
        get_all_cars_sql = "SELECT * FROM cars WHERE price > 1000000"
        cursor.execute(get_all_cars_sql)
        cars = cursor.fetchall()
        
        return render_template('cars.html', cars=cars)


@app.route("/cars/<car_id>")
def get_single_car(car_id):
     id = int(car_id)
     conn = conn_db('localhost', 'root', 'root')
     if conn:
        cursor = conn.cursor()
        cursor.execute("USE cars_db")
        sql = "SELECT * FROM cars WHERE id = %s"
        cursor.execute(sql,(id,))
        
        car = cursor.fetchone()

        if car:
            car_data = {
                "id": car[0],
                "img_url": car[1],
                "name": car[2],
                "price": car[3]
            }
        else:
             return jsonify({"error" : "Car not found"})

        print(car_data)

        return render_template('single_car.html', car_data=car_data)


@app.route("/order")
def order():
    pass
     
     

if __name__ == '__main__':
    app.run(debug=True)
