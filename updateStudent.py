#!/usr/bin/env python3
# Required dependencies and imports
from flask import Flask, request, redirect, render_template_string
import sqlite3

# Simulating the content of 'classes/db1.php' by creating a database connection function
def get_db_connection():
    # Connect to the SQLite database (database file: database.db)
    # In a production environment, replace this with the appropriate database connection
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Simulating the content of 'utils/styles.php'
styles_html = """<!--css links. file found in utils folder-->"""

# Simulating the content of 'utils/header.php'
header_html = """<!-- header content here -->"""

# Simulating the content of 'utils/footer.php'
footer_html = """<!-- footer content here -->"""

app = Flask(__name__)

@app.route('/updateStudent', methods=['GET', 'POST'])
def updateStudent():
    # Retrieving the 'id' parameter from the GET request
    id = request.args.get('id')
    # When the form is submitted via POST method
    if request.method == "POST":
        # If the "update" button is pressed, check the POST request
        if "update" in request.form:
            # Retrieve form values
            name = request.form["st_name"]
            phone = request.form["phone"]
            # Construct the SQL query exactly as in PHP code
            sql = "UPDATE student_coordinator set phone='" + phone + "',st_name='" + name + "' where sid='" + str(id) + "'"
            try:
                # Get database connection and execute the query
                conn = get_db_connection()
                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()
                conn.close()
                # If update is successful, display a JavaScript alert then redirect
                return """
<script>
alert(' Updated Successfully');
window.location.href='stu_cordinator.php';
</script>
"""
            except Exception as e:
                # If update fails, redirect to updateStudent.php using JavaScript
                return """
<script>
window.location.href='updateStudent.php';
</script>
"""
                
    # HTML content for GET method exactly preserving the original formatting and comments
    html_content = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Sanchanala 2k20</title>
        <title></title>
        """ + styles_html + """ 
        <!--css links. file found in utils folder-->
        
    </head>
    <body>
    """ + header_html + """
    <div class ="content"><!--body content holder-->
            <div class = "container">
                <div class ="col-md-6 col-md-offset-3">
    <form method="POST">
<label>Student co-ordinator name</label><br>
    <input type="text" name="st_name" required class="form-control"><br><br>
    <label>Student co-ordinator phone</label><br>
    <input type="text" name="phone" required class="form-control"><br><br>
    <button type="submit" name="update" class = "btn btn-default ">Update</button>
    </div>
    </div>
    </div>
    </form>
    

    """ + footer_html + """
    </body>
</html>
"""
    return render_template_string(html_content)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
