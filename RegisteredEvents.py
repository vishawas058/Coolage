import pymysql
from flask import Flask, request

app = Flask(__name__)

# Simulated inclusion of 'utils/header.php'
def header():
    # In the original PHP, this file would include header HTML.
    return "<!-- header content included by utils/header.php -->\n"

# Simulated inclusion of 'utils/styles.php'
def styles():
    # In the original PHP, this file would include styles.
    return "<!-- styles content included by utils/styles.php -->\n"

# Simulated inclusion of 'utils/footer.php'
def footer():
    # In the original PHP, this file would include footer HTML.
    return "\n<!-- footer content included by utils/footer.php -->"

@app.route('/events', methods=['POST'])
def events():
    # Including header and styles
    output = ""
    output += header()
    output += styles()

    usn = request.form.get('usn')

    # Including db1 equivalent (from classes/db1.php)
    conn = pymysql.connect(host='localhost', user='root', password='password', db='dbname', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql_query = ("SELECT * FROM registered r,staff_coordinator s ,event_info ef ,student_coordinator st,events e "
                         "where e.event_id= ef.event_id and e.event_id= s.event_id and e.event_id= st.event_id and r.usn= %s and r.event_id=e.event_id")
            cursor.execute(sql_query, (usn,))
            result = cursor.fetchall()
    finally:
        conn.close()

    output += '''
<div class = "content">
            <div class = "container">
            <h1> Registered Events</h1>
             '''
    if len(result) > 0:
        output += ''' 
                <table class="table table-hover" >
                    <thead>
                        <tr>
                            
                            <th>Event_name</th>             
                           <th>Student Co-ordinator</th>
                            <th>Staff Co-ordinator</th>
                           
                            <th>Date</th>
                        
                            <th>Time</th>
                            <th>location </th>
                          
                        </tr>
                    </thead>
                    <tbody>
                    '''
        i = 0
        for row in result:
            output += '<tr>'
            output += '<td>' + str(row['event_title']) + '</td>'
            output += '<td>' + str(row['st_name']) + '</td>'
            output += '<td>' + str(row['name']) + '</td>'
            output += '<td>' + str(row['Date']) + '</td>'
            output += '<td>' + str(row['time']) + '</td>'
            output += '<td>' + str(row['location']) + '</td>'
            output += '</tr>'
            i += 1
        output += '''
                    </tbody>
                </table>
                    '''
    else:
        output += 'Not Yet Rgistered any events'
                    
    output += '''
                
               
            </div>
        </div>
        <!-- $result = mysqli_query($conn, ); -->
        <div class = "content">
            <div class = "container">
            <h1>Not Registered Events</h1>
             '''
    if len(result) > 0:
        output += ''' 
                <table class="table table-hover" >
                    <thead>
                        <tr>
                            
                            <th>Event_name</th>             
                           <th>Student Co-ordinator</th>
                            <th>Staff Co-ordinator</th>
                           
                            <th>Date</th>
                        
                            <th>Time</th>
                            <th>location </th>
                          
                        </tr>
                    </thead>
                    <tbody>
                    '''
        i = 0
        for row in result:
            output += '<tr>'
            output += '<td>' + str(row['event_title']) + '</td>'
            output += '<td>' + str(row['st_name']) + '</td>'
            output += '<td>' + str(row['name']) + '</td>'
            output += '<td>' + str(row['Date']) + '</td>'
            output += '<td>' + str(row['time']) + '</td>'
            output += '<td>' + str(row['location']) + '</td>'
            output += '</tr>'
            i += 1
        output += '''
                    </tbody>
                </table>
                    '''
    else:
        output += 'NOT able fetch'
                    
    output += '''
                
               
            </div>
        </div>
        ''' + footer()
    
    return output

if __name__ == '__main__':
    app.run(debug=True)
