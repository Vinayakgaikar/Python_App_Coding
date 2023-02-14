from flask import Flask ,redirect , url_for , request

app=Flask(__name__)

#The route() function of the Flask class is a decorator,
# which tells the application which URL should call the associated function.

#@app.route('/')
#def hello_world():
#    return "hello world"


# To build a URL by adding own variable
@app.route('/success/<name>')
def success(name):
   return 'Welcome %s' % name

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
    

## main driver function
if __name__=='__main__':
    app.run(debug=True)

