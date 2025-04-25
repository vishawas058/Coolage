from flask import Flask, render_template_string
import mysql.connector

app = Flask(__name__)

# Establish database connection (equivalent to include_once 'classes/db1.php')
# Replace with your actual database connection parameters
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="your_database"
)

# Function to mimic require 'utils/styles.php'
def styles():
    # css links. file found in utils folder
    return '''
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    '''

# Function to mimic include 'utils/adminHeader.php'
def adminHeader():
    return '''
    <header>
        <h2>Admin Header</h2>
    </header>
    '''

# Function to mimic include 'utils/footer.php'
def footer():
    return '''
    <footer>
        <p>Footer content</p>
    </footer>
    '''

@app.route("/")
def staff_coordinator():
    # Execute the SQL query (equivalent to PHP mysqli_query)
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM staff_coordinator s ,events e where e.event_id= s.event_id"
    cursor.execute(query)
    result = cursor.fetchall()

    # HTML template preserving exact original formatting and comments
    html_template = '''<!DOCTYPE html>
<html>

<head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Sanchanala 2k20</title>
        <title></title>
        {{ styles }}<!--css links. file found in utils folder-->
        
    </head>

<body>{{ adminHeader }}
<div class = "content">
<div class = "container">
<h1>Staff Co-ordinator details</h1>
{% if result|length > 0 %}
 <table class="table table-hover" >
  
  <tr>
    <th>Name</th>
    <th>Phone</th>
    <th>Event</th>
    <th></th>
  </tr>
{% for row in result %}
<tr>
    <td>{{ row["name"] }}</td>
    <td>{{ row["phone"] }}</td>
    <td>{{ row["event_title"] }}</td>
    <td> <a href="updateStaff.php?id={{ row["event_id"] }}" class = "btn btn-default"> Update</a></td>
   
</tr>
{% endfor %}
</table>
{% else %}
    No result found
{% endif %}
</div>
</div>
 </body>
{{ footer }}
</html>'''

    # Render the template with the query result and included parts
    return render_template_string(html_template, result=result, styles=styles(), adminHeader=adminHeader(), footer=footer())

if __name__ == '__main__':
    app.run(debug=True)
