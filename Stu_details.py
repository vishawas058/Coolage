# Required dependencies and imports
from flask import Flask, render_template_string
import mysql.connector
import os

# ---------------------------
# classes/db1.py equivalent code
# ---------------------------
# This section imitates the inclusion of the 'classes/db1.php' file in PHP.
# It creates a database connection using mysql.connector.
try:
    conn = mysql.connector.connect(
        host="localhost",        # Database host
        user="username",         # Database username
        password="password",     # Database password
        database="database_name" # Database name
    )
except mysql.connector.Error as err:
    print("Error: {}".format(err))
    conn = None

# ---------------------------
# utils/styles.php equivalent code
# ---------------------------
def get_styles():
    # This function returns CSS links as a string.
    # In a real scenario, the content might be read from a file.
    return '''<link rel="stylesheet" href="/static/css/bootstrap.min.css">
<link rel="stylesheet" href="/static/css/styles.css"> <!--Additional CSS links if required-->'''

# ---------------------------
# utils/adminHeader.php equivalent code
# ---------------------------
def get_admin_header():
    # This function returns the admin header HTML content.
    return '''<header>
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="#">Admin Panel</a>
            </div>
        </div>
    </nav>
</header>'''

# ---------------------------
# utils/footer.php equivalent code
# ---------------------------
def get_footer():
    # This function returns the footer HTML content.
    return '''<footer>
    <div class="container">
        <p>&copy; 2020 Sanchanala. All rights reserved.</p>
    </div>
</footer>'''

# ---------------------------
# Flask App Setup and Route Definition
# ---------------------------
app = Flask(__name__)

@app.route('/')
def index():
    # Execute the query equivalent to:
    # SELECT * FROM events,registered r ,participent p WHERE events.event_id=r.event_id and r.usn = p.usn order by event_title
    cursor = conn.cursor(dictionary=True)
    query = ("SELECT * FROM events, registered r, participent p "
             "WHERE events.event_id=r.event_id and r.usn = p.usn "
             "order by event_title")
    cursor.execute(query)
    rows = cursor.fetchall()
    
    # HTML Template preserving the original formatting and structure
    template = '''<!DOCTYPE html>
<html>

<head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Sanchanala 2k20</title>
        <title></title>
        {{ styles }}<!--css links. file found in utils folder-->
        
    </head>

<body>{{ admin_header }}
<div class = "content">
<div class = "container">
<h1>Student details</h1>
{% if rows|length > 0 %}
 <table class="table table-hover" >
  
  <tr>
  <th>USN</th>
    <th>Name</th>
    <th>Branch</th>
    <th>Sem</th>
    <th>Email</th>
    <th>Phone</th>
    <th>College</th>
    <th>Event</th>
  </tr>
{% for row in rows %}
<tr>
<td>{{ row["usn"] }}</td>
    <td>{{ row["name"] }}</td>
    <td>{{ row["branch"] }}</td>
    <td>{{ row["sem"] }}</td>
    <td>{{ row["email"] }}</td>
    <td>{{ row["phone"] }}</td>
    <td>{{ row["college"] }}</td>
    <td>{{ row["event_title"] }}</td>
   
</tr>
{% endfor %}
</table>
{% else %}
    No result found
{% endif %}
</div>
</div>
{{ footer }}; 
 </body>
</html>
'''
    # Render the template with variables
    return render_template_string(template,
                                  styles=get_styles(),
                                  admin_header=get_admin_header(),
                                  footer=get_footer(),
                                  rows=rows)

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
    
