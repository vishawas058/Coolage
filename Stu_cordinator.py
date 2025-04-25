# Required dependencies and imports
from flask import Flask
import pymysql

app = Flask(__name__)

# Simulating include_once 'classes/db1.php'
def get_db_connection():
    # Establish connection to the MySQL database
    # Replace the connection parameters with your actual database configuration if needed
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='your_database_name',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn

# Constants simulating the required includes from PHP files
STYLES = """<?php require 'utils/styles.php'; ?><!--css links. file found in utils folder-->"""
ADMIN_HEADER = """<?php include 'utils/adminHeader.php'?>"""
FOOTER = """<?php include 'utils/footer.php';?>"""

@app.route('/')
def student_coordinator():
    # Execute the SQL query equivalent to:
    # $result = mysqli_query($conn,"SELECT * FROM student_coordinator s ,events e where e.event_id= s.event_id");
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM student_coordinator s ,events e where e.event_id= s.event_id"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        conn.close()

    # Begin constructing the HTML output exactly as in PHP
    html = """<!DOCTYPE html>
<html>

<head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Sanchanala 2k20</title>
        <title></title>
        """ + STYLES + """
        
    </head>

<body>""" + ADMIN_HEADER + """
<div class = "content">
<div class = "container">
<h1>Student Co-ordinator details</h1>
"""
    # If there are rows returned, then create the table
    if len(result) > 0:
        html += """ <table class="table table-hover" >
  
  <tr>
    <th>Name</th>
    <th>Phone</th>
    <th>Event</th>
    <th></th>
  </tr>
"""
        i = 0
        for row in result:
            html += """<tr>
    <td>""" + str(row["st_name"]) + """</td>
    <td>""" + str(row["phone"]) + """</td>
    <td>""" + str(row["event_title"]) + """</td>
    <td> <a  href="updateStudent.php?id=""" + str(row["event_id"]) + """" class = "btn btn-default"> Update</a></td>
   
</tr>
"""
            i += 1
        html += """</table>
"""
    else:
        html += "No result found"
    html += """</div>
</div>
 </body>
""" + FOOTER + """
</html>"""
    return html

if __name__ == '__main__':
    app.run(debug=True)
    
