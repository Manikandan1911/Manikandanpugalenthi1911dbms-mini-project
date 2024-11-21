from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection setup
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  # Replace with your MySQL username
        password='Mani@1911',  # Replace with your MySQL password
        database='bus_ticket_booking'
    )
    return connection


@app.route('/')
def home():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM buses WHERE rating > 4.0 LIMIT 5")  # Example: Recommended buses
    buses = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('home.html', buses=buses)


@app.route('/buses')
def buses():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM buses")
    buses = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('buses.html', buses=buses)


@app.route('/book/<int:bus_id>', methods=['GET', 'POST'])
def book_ticket(bus_id):
    if request.method == 'POST':
        # Retrieve user details and booking information
        user_name = request.form['user_name']
        email = request.form['email']
        phone = request.form['phone']
        seats = request.form['seats']
        departure_station = request.form['departure_station']
        destination_station = request.form['destination_station']

        # Insert booking into the database
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO bookings (bus_id, user_name, email, phone, seats,
                        departure_station, destination_station)
                          VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                       (bus_id, user_name, email, phone, seats, departure_station, destination_station))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('details'))

    # Get bus details to display on the booking page
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM buses WHERE id = %s', (bus_id,))
    bus = cursor.fetchone()
    cursor.close()
    connection.close()

    return render_template('book.html', bus=bus)


@app.route('/details')
def details():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Get search query from the URL
    search_query = request.args.get('search')

    if search_query:
        # Search bookings based on user name, bus name, or email
        cursor.execute('''
            SELECT bookings.*, buses.name AS bus_name
            FROM bookings
            JOIN buses ON bookings.bus_id = buses.id
            WHERE bookings.user_name LIKE %s OR buses.name LIKE %s OR bookings.email LIKE %s
        ''', ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
    else:
        # If no search query, fetch all bookings
        cursor.execute('''
            SELECT bookings.*, buses.name AS bus_name
            FROM bookings
            JOIN buses ON bookings.bus_id = buses.id
        ''')

    bookings = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('details.html', bookings=bookings, search_query=search_query)


@app.route('/edit_booking/<int:booking_id>', methods=['GET', 'POST'])
def edit_booking(booking_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == 'POST':
        user_name = request.form['user_name']
        email = request.form['email']
        phone = request.form['phone']
        seats = request.form['seats']
        departure_station = request.form['departure_station']
        destination_station = request.form['destination_station']

        cursor.execute('''UPDATE bookings SET user_name=%s, email=%s, phone=%s, seats=%s,
                          departure_station=%s, destination_station=%s
                          WHERE id=%s''',
                       (user_name, email, phone, seats, departure_station, destination_station, booking_id))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('details'))

    cursor.execute('SELECT * FROM bookings WHERE id = %s', (booking_id,))
    booking = cursor.fetchone()
    cursor.close()
    connection.close()

    return render_template('edit_booking.html', booking=booking)


@app.route('/delete_booking/<int:booking_id>', methods=['POST'])
def delete_booking(booking_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Delete the booking from the database
    cursor.execute('DELETE FROM bookings WHERE id = %s', (booking_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('details'))


@app.route('/more_info')
def more_info():
    return render_template('more_info.html')


if __name__ == '__main__':
    app.run(debug=True)
