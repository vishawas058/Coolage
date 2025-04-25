from flask import Flask, request, redirect, render_template, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        event_id = request.form['event_id']
        event_title = request.form['event_title']
        event_price = request.form['event_price']
        img_link = request.form['img_link']
        type_id = request.form['type_id']
        name = request.form['sname']
        st_name = request.form['st_name']
        date = request.form['Date']
        time = request.form['time']
        location = request.form['location']

        if event_id and event_title and event_price and img_link and type_id:
            conn = sqlite3.connect('database.db')  # Connect to your database
            cursor = conn.cursor()

            try:
                cursor.execute("INSERT INTO events(event_id, event_title, event_price, img_link, type_id) VALUES (?, ?, ?, ?, ?)",
                               (event_id, event_title, event_price, img_link, type_id))
                cursor.execute("INSERT INTO event_info(event_id, Date, time, location) VALUES (?, ?, ?, ?)",
                               (event_id, date, time, location))
                cursor.execute("INSERT INTO student_coordinator(sid, st_name, phone, event_id) VALUES (?, ?, NULL, ?)",
                               (event_id, st_name, event_id))
                cursor.execute("INSERT INTO staff_coordinator(stid, name, phone, event_id) VALUES (?, ?, NULL, ?)",
                               (event_id, name, event_id))
                conn.commit()
                flash('Event Inserted Successfully!')
                return redirect('adminPage')
            except sqlite3.IntegrityError:
                flash('Event already exists!')
                return redirect('createEventForm')
            finally:
                conn.close()
        else:
            flash('All fields are required')
            return redirect('createEventForm')

    return render_template('create_event.html')  # Render your HTML form here

if __name__ == '__main__':
    app.run(debug=True)