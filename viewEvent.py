import mysql.connector
from flask import request, render_template

# Assuming 'conn' is a valid database connection
connection = mysql.connector.connect(user='username', password='password', host='localhost', database='database_name')
event_id = request.args.get('id')
query = f"SELECT * FROM events, event_info ef, student_coordinator s, staff_coordinator st WHERE type_id = {event_id} and ef.event_id=events.event_id and s.event_id=events.event_id and st.event_id=events.event_id"
cursor = connection.cursor()
cursor.execute(query)
result = cursor.fetchall()

# Assuming this is part of a Flask application with Jinja2 templates
html_content = render_template('header.html')  # header content from a separate template

html_content += '<div class="content"><div class="container"><div class="col-md-12">'

if len(result) > 0:
    index = 0
    for row in result:
        # Assuming 'events.html' is another template for rendering events
        html_content += render_template('events.html', row=row)
        index += 1

html_content += '<div class="container"><div class="col-md-12"><hr></div></div>'
html_content += '<a class="btn btn-default" href="index.py"><span class="glyphicon glyphicon-circle-arrow-left"></span> Back</a>'
html_content += '</div></div>'

html_content += render_template('footer.html')  # footer content from a separate template