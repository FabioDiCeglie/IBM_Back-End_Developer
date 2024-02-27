# Method decorators

# Let’s say we have a python code where we want all the output to be in JSON format. It doesn’t make sense to include code for these in each of the methods as it makes the lines of code redundant. 
# In such cases, we can handle this with a decorator.


def jsonify_decorator(function):
    def modifyOutput():
        return {"output":function()}
    return modifyOutput

@jsonify_decorator
def hello():
    return 'hello world'

@jsonify_decorator
def add():
    num1 = input("Enter a number - ")
    num2 = input("Enter another number - ")
    return int(num1)+int(num2)

print(hello())
print(add())

# The method decorator is also referred to as the wrapper, which wraps the output of the function, that it decorates. In the above code sample, jsonify-decorator is the decorator method.
# We have added this decorator to hello() and add(). The output of these method calls will now be wrapped and decorated with the jsonify_decorator.

# The output of invoking the above python code will be:

# {'output': 'hello world' }
# Enter a number - 73
# Enter another number - 87
# {'outpu': 160}

# Route Decorators

from flask import Flask, request, redirect

app= Flask('App')

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return "Hello World!"

# The route decorator can also be more specific. For example, to get the details of a user whose userId is U0001, you may go to
# http://mydomain.com/userdetails/U0001. It doesn’t make sense to define a different route for each user you may be dealing with. In such cases, we define the route like this.

@app.route("/userdetails/<userid>")
def getUserDetails(userid):
    return "User Details for  "+userid

# Accessing Form Data with flask.request.form
# You can use flask.request.form to access form data that a user has submitted via a POST request. For instance, this feature can be used if you have a login form with username and password fields.

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # process login here


# Redirecting to a URL with flask.redirect
    
# Flask provides a function called flask.redirect to guide users to a different webpages (or endpoints). 
# The flask.redirect function can be useful in several scenarios. For example, you can use the flask.redirect function to redirect a user to a login page when they try to access a restricted admin page.
    
@app.route('/admin')
def admin():
    return redirect('/login')

# Generating Dynamic URLs with flask.url_for
# The flask.url_for function dynamically generates URLs for a given endpoint. Dynamically generating URLs can be particularly useful when the URL for a route is altered. 
# The flask.url_for function automatically updates the URL throughout your templates or code, minimizing manual work. For example, consider the scenario where a user is trying to access the admin page and must be redirected to the login page. 
# In this scenario, url_for('login') will retrieve the URL for the login page from the existing routes.

from flask import url_for

@app.route('/admin')
def admin():
    return redirect(url_for('login'))
@app.route('/login')
def login():
    return "<Login Page>"

# Handling different HTTP request types

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        # process POST request
        return
    if request.method == 'GET':
        # process GET request
        return

