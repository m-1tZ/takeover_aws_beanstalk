from flask import Flask

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

@app.route("/")
def hello():
    return "WW91ciBwYWdlIGJlbG9uZ3MgdG8gbTF0Wg=="

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>Takover POC</title> </head>\n<body>'''
instructions = '''
    WW91ciBwYWdlIGJlbG9uZ3MgdG8gbTF0Wg==\n'''
home_link = ''
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()