import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/event_details')
def event_details():
    conn = mysql.connector.connect(user='your_user', password='your_password', host='your_host', database='your_database')
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM staff_coordinator s, event_info ef, student_coordinator st, events e WHERE e.event_id = ef.event_id AND e.event_id = s.event_id AND e.event_id = st.event_id")
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('event_details.html', result=result)

if __name__ == '__main__':
    app.run()

# In the 'event_details.html' template, you would include the HTML structure and loop through the 'result' variable to display the data.