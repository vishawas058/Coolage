from flask import Flask, request, redirect, url_for
from flask import render_template_string

# Dummy implementation for classes/db1.php equivalent in Python
class db1:
    pass

# Dummy implementation for utils/styles.php equivalent in Python
def get_styles():
    # css links. file found in utils folder
    return '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">'

# Dummy implementation for utils/header.php equivalent in Python
def get_header():
    # header content. file found in utils folder
    return '<header><h1>Header</h1></header>'

# Dummy implementation for utils/footer.php equivalent in Python
def get_footer():
    # footer content. file found in utils folder
    return '<footer><p>Footer</p></footer>'

app = Flask(__name__)

@app.route('/login_form.py', methods=['GET', 'POST'])
def login_form():
    # Check if form has been submitted
    if request.method == "POST" and "update" in request.form:
        myusername = request.form['name']
        mypassword = request.form['password']
        if mypassword == 'admin' and myusername == 'admin':
            # echo "<script>
            # alert('Login Successfull');
            # window.location.href='adminPage.php';
            # </script>";
            return render_template_string("""
<script>
alert('Login Successfull');
window.location.href='adminPage.py';
</script>
""")
        else:
            # echo "<script>
            # alert('Invalid credentials');
            # window.location.href='login_form.php';
            # </script>";
            return render_template_string("""
<script>
alert('Invalid credentials');
window.location.href='login_form.py';
</script>
""")
    # HTML output preserving exact formatting from original PHP code
    html_content = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Sanchanala 2k20</title>
        <title></title>
        <style>
            span.error{
                color: red;
            }            
        </style>  
        {{ styles }}<!--css links. file found in utils folder-->
    </head>
    <body>
        {{ header }}<!--header content. file found in utils folder-->
        <div class = "content"><!--body content holder-->
            <div class = "container">
                <div class ="col-md-6 col-md-offset-3">
                  
                    <form method="POST"><!--form-->
                      
                            <!--username field-->
                            <label>UserName:</label><br>
        <input type="text" name="name" class="form-control" required><br>
                            
                   
        <label>Password</label><br>
        <input type="password" name="password" class="form-control" required><br>
                        <button type = "submit" name="update" class = "btn btn-default">Login</button>
                    </form>
                </div><!--col md 6 div-->
            </div><!--container div-->
        </div><!--content div-->
        {{ footer }}<!--footer content. file found in utils folder-->
    </body>
</html>
"""
    return render_template_string(html_content, styles=get_styles(), header=get_header(), footer=get_footer())

@app.route('/adminPage.php')
def adminPage():
    # A simple admin page response
    admin_html = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Admin Page</title>
    </head>
    <body>
        <h1>Welcome to the Admin Page</h1>
    </body>
</html>
"""
    return admin_html

@app.route('/')
def index():
    # Redirect root URL to login form page to mimic PHP behavior
    return redirect(url_for('login_form'))

if __name__ == '__main__':
    app.run(debug=True)
