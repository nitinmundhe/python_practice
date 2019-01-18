import flask

# Jinja 2  for template development for flask

myapp = flask.Flask('myapp')


@myapp.errorhandler(404)
def errorpage(argument):
    return 'Page Under construction...'


@myapp.route('/')
def index():
    return '<b> Welcome to Home Page </b>'


@myapp.route('/about')
def aboutpage():
    return '<b> About this page. </b>'


@myapp.route('/empname/<name>')
def getname(name):
    return '<b> Hello ' + str(name).capitalize() + ' </b>'


@myapp.route('/emp/<int:eid>')
def geteid(eid):
    return '<b> Emp ID is : ' + str(eid) + '</b>'


@myapp.route('/fullpath/<path:fp>')
def fullpath(fp):
    return 'Path is : ' + str(fp)


@myapp.route('/login')
def login():
    return """<form action='/verifylogin' methods=['POST']>
            User Name : <input type = 'text' name = 'name' value='abc'> <br/>
            Password :  <input type = 'password'  name = 'password' value='xyz'> <br/>
            <input type = 'Submit' value='Sign In'>
           """

@myapp.route('/verifylogin', methods = ['POST'])
def verifylogin():
    u = flask.request.form.get('name')
    p = flask.request.form.get('password')
    if not (u == 'abc' and p == 'xyz'):
        return flask.abort(401, 'Access Denied')
    else:
        import sqlite3
        con = sqlite3.connect('mydb.sqlite3')
        cur = con.cursor()
        cur.execute('select * From logdata;')
        result = cur.fetchall()
        return flask.render_template('report.html', res=result)

@myapp.route('/json')
def jsonpage():
    F = open('data.json', 'w')
    import json
    D = {'A': 10, 'B': 20}
    json.dump(D, F)
    F.close()
    F = open('data.json')
    out = json.load(F)
    F.close()
    return out

@myapp.route('/newlogin',methods = ['POST', 'GET'])
def login():
   if flask.request.method == 'POST' and flask.request.form['username'] == 'admin' :
       return redirect(url_for('success'))
   return redirect(url_for('index'))

@myapp.route('/index')
def success():
   return 'Welcome'

@myapp.route('/success')
def success():
   return 'logged in successfully'
'''


@myapp.post('/verifylogin')
def verifylogin():
    u = bottle.request.forms.get('uname')
    p = bottle.request.forms.get('pwd')
    if not (u == 'abc' and p == 'xyz'):
        return bottle.abort(401, 'Access Denied')
    else:
        print(bottle.TEMPLATE_PATH)
        bottle.TEMPLATE_PATH.append(r'C:\nitsmagic\bin')
        import sqlite3
        con = sqlite3.connect('mydb.sqlite3')
        cur = con.cursor()
        cur.execute('select * From logdata;')
        result = cur.fetchall()
        # return 'Login Success' + str(result)
        return bottle.template('report.tpl', res=result)
    # inside tpl file if code is one liner it starts with %
    # variable value display make use of {{}}
    # block of code is one liner it starts with <% %>
    # above res variable will be available inside tpl file



@myapp.error(404)
def errorpage(argument):
    return 'Page Under construction...'
   
import re
@myapp.route('/regex/<e:re:[a-z]+>')
def repage(e):
    return 'Path is : ' + str(e)

@myapp.route('/login')
def login():
    return """<form action='/verifylogin' method='post'>
            User Name : <input type = 'text' name = 'uname' value='uname'> <br/>
            Password :  <input type = 'password'  name = 'pwd' value='password'> <br/>
            <input type = 'Submit' value='Sign In'>
           """


@myapp.post('/verifylogin')
def verifylogin():
    u = bottle.request.forms.get('uname')
    p = bottle.request.forms.get('pwd')
    if not (u == 'abc' and p == 'xyz'):
        return bottle.abort(401, 'Access Denied')
    else:
        print(bottle.TEMPLATE_PATH)
        bottle.TEMPLATE_PATH.append(r'C:\nitsmagic\bin')
        import sqlite3
        con = sqlite3.connect('mydb.sqlite3')
        cur = con.cursor()
        cur.execute('select * From logdata;')
        result = cur.fetchall()
        # return 'Login Success' + str(result)
        return bottle.template('report.tpl', res=result)
    # inside tpl file if code is one liner it starts with %
    # variable value display make use of {{}}
    # block of code is one liner it starts with <% %>
    # above res variable will be available inside tpl file


@myapp.route('/json')
def jsonpage():
    F = open('data.json', 'w')
    import json
    D = {'A': 10, 'B': 20}
    json.dump(D, F)
    F.close()
    F = open('data.json')
    out = json.load(F)
    F.close()
    return out

'''

myapp.run()  # host= port=
