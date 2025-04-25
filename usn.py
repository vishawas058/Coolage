html_content = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Sanchanala 2k20</title>
        <title></title>
        <!--css links. file found in utils folder-->
        <link rel="stylesheet" type="text/css" href="utils/styles.css">
    </head>
    <body>
        <!--header content. file found in utils folder-->
        <div>
            <header>
                <!-- Include header content here -->
            </header>
        </div>

        <div class ="content"><!--body content holder-->
            <div class = "container">
                <div class ="col-md-6 col-md-offset-3">
                    <form action="RegisteredEvents.php" class ="form-group" method="POST">

                        <div class="form-group">
                            <label for="student_usn"> Student USN: </label>
                            <input type="text"
                                   id="student_usn"
                                   name="usn"
                                   class="form-control">
                        </div>
                        <button type="submit" class = "btn btn-default">Login</button>
                    </form>
                </div>
            </div>
        </div>
    </body>
</html>
""" 