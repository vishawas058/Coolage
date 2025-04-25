from flask import Flask, Response

app = Flask(__name__)

# The following functions simulate the PHP includes for styles, header, and footer.

def styles():
    # This function simulates the contents of 'utils/styles.php'
    # In this example, it returns a link to a stylesheet.
    return '<link rel="stylesheet" type="text/css" href="styles.css">'

def header():
    # This function simulates the contents of 'utils/header.php'
    # In this example, it returns the header HTML content.
    return '<header>\n    <h1>Site Header</h1>\n</header>'

def footer():
    # This function simulates the contents of 'utils/footer.php'
    # In this example, it returns the footer HTML content.
    return '<footer>\n    <p>Site Footer</p>\n</footer>'

@app.route("/")
def index():
    # Setting event ids for each event category
    id1 = 1  # Technical Events
    id2 = 2  # Gaming Events
    id3 = 3  # On-Stage Events
    id4 = 4  # Off-Stage Events

    # Create anchor links identical to the PHP echo statements.
    anchor_tech = f'<a class="btn btn-default"  href="viewEvent.php?id={id1}"> <span class="glyphicon glyphicon-circle-arrow-right"></span>View Technical Events</a>'
    anchor_gaming = f'<a class="btn btn-default" href="viewEvent.php?id={id2}"> <span class="glyphicon glyphicon-circle-arrow-right"></span>View Gaming Events</a>'
    anchor_onstage = f'<a class="btn btn-default" href="viewEvent.php?id={id3}"> <span class="glyphicon glyphicon-circle-arrow-right"></span>View On-Stage Events</a>'
    anchor_offstage = f'<a class="btn btn-default" href="viewEvent.php?id={id4}"> <span class="glyphicon glyphicon-circle-arrow-right"></span>View Off-Stage Events</a>'

    # The complete HTML content preserving the original PHP file structure and comments.
    html_content = """<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Sanchanala2k20</title>
        {styles_include}
      
        
    
            </head>
    <body>
        {header_include}<!--header content. file found in utils folder-->
        <div class = "content"><!--body content holder-->
            <div class = "container">
                <div class = "col-md-12"><!--body content title holder with 12 grid columns-->
                    <h1 style="color:#000080 ; font-size:42px ; font-style:bold "><strong>  Register your Favourite events:</strong></h1><!--body content title-->

            </div>
            
            
            <div class="container">
            <div class="col-md-12">
            <hr>
            </div>
            </div>
            
            <div class="row"><!--technical content-->
                <section>
                    <div class="container">
                        <div class="col-md-6"><!--image holder with 6 grid columns-->
                            <img src="images/technical.jpg" class="img-responsive">
                        </div>
                        <div class="subcontent col-md-6"><!--Text holder with 6 column grid-->
                        
                            <h1 style="color:#003300 ; font-size:38px ;" ><u><strong>Technical Events</strong></u></h1><!--title-->
                            <p><!--content-->
                                EMBRACE YOUR TECHNICAL SKILLS BY PARTICIPATING IN OUR DIFFERENT TECHNICAL EVENTS!
                            </p>
                            
                            <br><br>
                        {anchor_tech}
                             </div><!--subcontent div-->
                    </div><!--container div-->
                </section>
            </div><!--row div-->
            
            <div class="container">
            <div class="col-md-12">
            <hr>
            </div>
            </div>

            <div class="row">
                <section>
                    <div class="container">
                        <div class="col-md-6"><!--image holder with 6 grid columns-->
                            <img src="images/gaming.jpg" class="img-responsive">
                        </div>
                        <div class="subcontent col-md-6"><!--Text holder with 6 column grid-->
                            <h1 style="color:#003300 ; font-size:38px ;"><strong><u>Gaming Events</u></strong></h1><!--title-->
                            <p><!--content-->
                                EMBRACE YOUR GAMING SKILLS BY PARTICIPATING IN OUR DIFFERENT GAMING EVENTS!
                            </p>
                            
                            <br><br>
                            {anchor_gaming}
                        </div><!--subcontent div-->
                    </div><!--container div-->
                </section>
            </div><!--row div-->
            
            <div class="container">
            <div class="col-md-12">
            <hr>
            </div>
            </div>

            <div class="row">
                <section>
                    <div class="container">
                        <div class="col-md-6"><!--image holder with 6 grid columns-->
                            <img src="images/onstage.jpg" class="img-responsive">
                        </div>
                        <div class="subcontent col-md-6"><!--Text holder with 6 column grid-->
                            <h1 style="color:#003300 ; font-size:38px ;"><strong><u>On-Stage Events</strong></u></h1><!--title-->
                            <p><!--content-->
                                EMBRACE YOUR CONFIDENCE BY PARTICIPATING IN OUR DIFFERENT ON-STAGE EVENTS!
                            </p>
                            
                            <br><br>
                            {anchor_onstage}
                        </div><!--subcontent div-->
                    </div><!--container div-->
                </section>
            </div><!--row div-->
            
            <div class="container">
            <div class="col-md-12">
                <hr>
            </div>
            </div>

            <div class="row">
                <section>
                    <div class="container">
                        <div class="col-md-6"><!--image holder with 6 grid columns-->
                            <img src="images/offstage.jpg" class="img-responsive">
                        </div>
                        <div class="subcontent col-md-6"><!--Text holder with 6 column grid-->
                            <h1 style="color:#003300 ; font-size:38px ;"><strong><u>Off-Stage Events</u></strong></h1><!--title-->
                            <p><!--content-->
                                 EMBRACE YOUR TALENT BY PARTICIPATING IN OUR DIFFERENT OFF-STAGE EVENTS!
                            </p>
                            
                            
                            <br><br><br>
                            {anchor_offstage}
                        </div><!--subcontent div-->
                    </div><!--container div-->
                </section>
            </div><!--row div-->
        </div><!--body content div-->
  
        {footer_include}<!--footer content. file found in utils folder-->
    </body>
</html>""".format(styles_include=styles(),
                header_include=header(),
                footer_include=footer(),
                anchor_tech=anchor_tech,
                anchor_gaming=anchor_gaming,
                anchor_onstage=anchor_onstage,
                anchor_offstage=anchor_offstage)

    return Response(html_content, mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True)
    
