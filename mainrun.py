from flask import Flask, render_template, request
import sqlite3 
app = Flask(__name__)

@app.route('/')
def store():
  print("in\n\n\n\n\n\n\n\n\n\n\n\"")
  con = sqlite3.connect("bookstore.db")
  con.row_factory = sqlite3.Row
  cur = con.cursor()
  cur.execute("select * from bstore")
  rows = cur.fetchall()
  return render_template("store.html",rows=rows)

@app.route('/<bokid>')
def rend(bokid):
  con = sqlite3.connect("bookstore.db")
  con.row_factory = sqlite3.Row
  cur = con.cursor()
  cur.execute("select * from bstore where b_id=?",(bokid,))
  row = cur.fetchone()
	
	
  return render_template("11.html",row=row)


if __name__=='__main__':
  app.run(debug=True)








