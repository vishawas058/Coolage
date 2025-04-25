#!/usr/bin/env python3
# Required dependencies and imports
from flask import Flask, request
import sqlite3

app = Flask(__name__)

# === Begin of classes/db1.php equivalent ===
# This function simulates the included database connection file 'classes/db1.php'
def get_db_connection():
    # For this translation, we are using sqlite3 as the database.
    # A database file named 'database.db' is assumed to exist with the required schema.
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create a global connection variable similar to PHP's $conn
# In a real implementation, proper connection management would be required.
conn = get_db_connection()
# === End of classes/db1.php equivalent ===

# === Begin of utils/styles.php equivalent ===
def get_styles():
    # This function simulates the 'utils/styles.php' include
    # It returns the CSS link tags as a string.
    return '''<link rel="stylesheet" type="text/css" href="styles.css">'''
# === End of utils/styles.php equivalent ===

# === Begin of utils/header.php equivalent ===
def get_header():
    # This function simulates the 'utils/header.php' include
    return '''<header>
    <h1>Site Header</h1>
</header>'''
# === End of utils/header.php equivalent ===

# === Begin of utils/footer.php equivalent ===
def get_footer():
    # This function simulates the 'utils/footer.php' include
    return '''<footer>
    <p>Site Footer</p>
</footer>'''
# === End of utils/footer.php equivalent ===

@app.route('/', methods=['GET', 'POST'])
def update_staff_coordinator():
    # In PHP: $id=$_GET['id'];
    id = request.args.get('id', '')
    if request.method == 'POST':
        # In PHP: if (isset($_POST["update"]))
        if "update" in request.form:
            # In PHP: $name=$_POST["st_name"];
            name = request.form.get("st_name", "")
            # In PHP: $phone=$_POST["phone"];
            phone = request.form.get("phone", "")
            # In PHP: $sql="UPDATE staff_coordinator set phone='$phone',name='$name' where stid='$id'";
            sql = "UPDATE staff_coordinator set phone='" + phone + "',name='" + name + "' where stid='" + id + "'"
            try:
                # Execute the SQL query using the global connection
                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()
                # In PHP: if($conn->query($sql)===true)
                # If successful, output the success javascript alert and redirect
                return '''<script>
        alert(' Updated Successfully');
        window.location.href='stu_cordinator.php';
        </script>'''
            except Exception as e:
                # In PHP's else: output the failure redirect javascript
                return '''<script>
        window.location.href='updateStudent.php';
        </script>'''
    # GET method: Render the HTML form with preserved formatting and includes.
    return '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Sanchanala 2k20</title>
        <title></title>
        {styles}<!--css links. file found in utils folder-->
        
    </head>
    <body>
    {header}
    <div class ="content"><!--body content holder-->
            <div class = "container">
                <div class ="col-md-6 col-md-offset-3">
    <form method="POST">
<label>Staff co-ordinator name</label><br>
    <input type="text" name="st_name" required class="form-control"><br><br>
    <label>Staff co-ordinator phone</label><br>
    <input type="text" name="phone" required class="form-control"><br><br>
    <button type="submit" name="update" class = "btn btn-default ">Update</button>
    </div>
    </div>
    </div>
    </form>
    

    {footer}
    </body>
</html>'''.format(styles=get_styles(), header=get_header(), footer=get_footer())

if __name__ == '__main__':
    app.run(debug=True)
