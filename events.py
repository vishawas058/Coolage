#!/usr/bin/env python3
print("""<div class=\"container\">
<div class=\"col-md-12\">
<hr>
</div>
<div class=\"row\">
<section>
<div class=\"container\">
<div class=\"col-md-6\">

<img src=\" """)
print(row_["img_link"])
print("""\" class=\"img-responsive\">
</div>
<div class=\"subcontent col-md-6\">                        
<h1 style=\"color:#003300 ; font-size:38px ;\" ><u><strong>""")
print("<td>" + row_["event_title"] + "</td>")
print("</strong></u></h1><!--title-->\n                            <p style=\"color:#003300  ;font-size:20px \"><!--content-->\n                            ")
print("Date:" + row_["Date"] + "<br>")
print("Time:" + row_["time"] + "<br>")
print("Location:" + row_["location"] + "<br>")
print("Student Co-ordinator:" + row_["st_name"] + "<br>")
print("Staff Co-ordinator:" + row_["name"] + "<br>")
print("Event Price:" + row_["event_price"] + "<br>")
print("""                            </p>

<br><br>
""")
print("<a class=\"btn btn-default\" href=\"register.php\"> <span class=\"glyphicon glyphicon-circle-arrow-right\"></span>Register</a>")
print("""                                                        </div><!--subcontent div-->
</div><!--container div-->
</section>
</div>
</div><!--row div-->""")
