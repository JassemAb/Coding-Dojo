from flask import Flask, render_template, request, redirect
from users import User

app=Flask(__name__)

@app.route('/')
def index():
 return redirect('/users')

@app.route('/users')
def users():
 return render_template("users.html", users=User.get_all())

@app.route('/user/new')
def new():
 return render_template("new_user.html")

@app.route('/user/create', methods=['POST'])
def create():
 print(request.form)
 User.save(request.form)
 return redirect('/users')

@app.route('/user/edit/<int:id>')
def show(id):
 data={
  "id":id
 }
 return render_template("show_user.html",user=User.get_one(data))

@app.route('user/show/<int:id>')
def show(id):
 data={
  "id":id
 }
 return  render_template("show_user.html",user=User.get_one(data))

if __name__=="__main__":
 app.run(debug=True)