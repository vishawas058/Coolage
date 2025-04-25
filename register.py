from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Utility function to simulate 'utils/styles.php'
def get_styles():
    #css links. file found in utils folder
    return '''<!--css links. file found in utils folder-->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">'''

# Utility function to simulate 'utils/header.php'
def get_header():
    return '''<!--header content from utils/header.php-->
<header>
    <h1>Sanchalana2k20</h1>
</header>'''

# Utility function to simulate 'utils/footer.php'
def get_footer():
    return '''<!--footer content from utils/footer.php-->
<footer>
    <p>&copy; Sanchalana2k20</p>
</footer>'''

# Utility function to simulate database connection from 'classes/db1.php'
def get_db_connection():
    conn = sqlite3.connect('database.db')
    # Ensuring that rows are returned as dictionaries
    conn.row_factory = sqlite3.Row
    # Create table if it doesn't exist. 'usn' set as PRIMARY KEY to mimic uniqueness.
    conn.execute('''CREATE TABLE IF NOT EXISTS participent (
                        usn TEXT PRIMARY KEY,
                        name TEXT,
                        branch TEXT,
                        sem INTEGER,
                        email TEXT,
                        phone TEXT,
                        college TEXT
                    )''')
    conn.commit()
    return conn

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST" and "update" in request.form:
        usn = request.form.get("usn")
        name = request.form.get("name")
        branch = request.form.get("branch")
        sem = request.form.get("sem")
        email = request.form.get("email")
        phone = request.form.get("phone")
        college = request.form.get("college")
        
        # Mimicking: if( !empty($usn) || !empty($name) || !empty($branch) || !empty($sem) || !empty($email) || !empty($phone) || !empty($college) )
        if (usn != "" or name != "" or branch != "" or sem != "" or email != "" or phone != "" or college != ""):
            conn = get_db_connection()
            try:
                INSERT = "INSERT INTO participent (usn,name,branch,sem,email,phone,college) VALUES(?, ?, ?, ?, ?, ?, ?)"
                # Convert 'sem' to int for insertion as number.
                conn.execute(INSERT, (usn, name, branch, int(sem), email, phone, college))
                conn.commit()
                conn.close()
                # Mimicking JavaScript alert and redirect in PHP echo block
                return '''<script>
alert('Registered Successfully!');
window.location.href='usn.php';
</script>'''
            except Exception as e:
                conn.close()
                return '''<script>
alert(' Already registered this usn');
window.location.href='usn.php';
</script>'''
        else:
            return '''<script>
alert('All fields are required');
window.location.href='register.php';
</script>'''
    
    # HTML content of the registration form page
    html_content = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Sanchalana2k20</title>
        {{ styles }}
        
    </head>
    <body>
    {{ header }}
    <div class ="content"><!--body content holder-->
            <div class = "container">
                <div class ="col-md-6 col-md-offset-3">
    <form method="POST">

   
        <label>Student USN:</label><br>
        <input type="text" name="usn" class="form-control" required><br><br>

        <label>Student Name:</label><br>
        <input type="text" name="name" class="form-control" required><br><br>

        <label>Branch:</label><br>
        <input type="text" name="branch" class="form-control" required><br><br>

        <label>Semester:</label><br>
        <input type="text" name="sem" class="form-control" required><br><br>

        <label>Email:</label><br>
        <input type="text" name="email"  class="form-control" required ><br><br>

        <label>Phone:</label><br>
        <input type="text" name="phone"  class="form-control" required><br><br>

        <label>College:</label><br>
        <input type="text" name="college"  class="form-control" required><br><br>

        <button type="submit" name="update" required>Submit</button><br><br>
        <a href="usn.php" ><u>Already registered ?</u></a>

    </div>
    </div>
    </div>
    </form>
    

    {{ footer }}
    </body>
</html>
'''
    return render_template_string(html_content, styles=get_styles(), header=get_header(), footer=get_footer())

@app.route('/usn', methods=['GET'])
def usn():
    # Dummy page to represent 'usn.php'
    return '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>USN Page</title>
    </head>
    <body>
        <h2>This is the USN page.</h2>
    </body>
</html>'''

if __name__ == '__main__':
    app.run(debug=True)
    
