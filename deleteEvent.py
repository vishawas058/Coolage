import mysql.connector
from flask import request, redirect, flash

id = request.args.get('id')

conn = mysql.connector.connect(user='your_user', password='your_password', host='your_host', database='your_database')
cursor = conn.cursor()

sql = f"DELETE FROM events WHERE event_id='{id}';"
sql += f"DELETE FROM event_info WHERE event_id='{id}';"
sql += f"DELETE FROM staff_coordinator WHERE event_id='{id}';"
sql += f"DELETE FROM student_coordinator WHERE event_id='{id}';"
sql += f"DELETE FROM registered WHERE event_id='{id}';"

try:
    cursor.execute(sql)
    conn.commit()
    flash('Event Deleted Successfully')
    return redirect('adminPage.py')
except mysql.connector.Error as err:
    print(f"Error deleting record: {err}")
finally:
    cursor.close()
    conn.close()