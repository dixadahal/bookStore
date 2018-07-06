import sqlite3

con = sqlite3.connect("bookstore.db")

cur = con.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS b_img(img_name BLOB")
cur.execute("CREATE TABLE IF NOT EXISTS keeper( k_id varchar(35) PRIMARY KEY, k_pword VARCHAR(12))")
cur.execute("CREATE TABLE IF NOT EXISTS cust( c_id varchar(35) PRIMARY KEY, c_pword VARCHAR (12), c_name VARCHAR (45),c_purchased INTEGER,c_email VARCHAR (40),c_cat VARCHAR (10) ) ")
cur.execute("CREATE TABLE IF NOT EXISTS bstore( b_id BIGINT PRIMARY KEY,b_name VARCHAR (35),author_name VARCHAR(30),ratings FLOAT,book_count INTEGER, reviews TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS admin ( a_id varchar(35) PRIMARY KEY,a_pword VARCHAR (12),book_id BIGINT, cust_id BIGINT,FOREIGN KEY (book_id) REFERENCES bstore(b_id),FOREIGN KEY (cust_id) REFERENCES cust(c_id))")
#cur.execute('insert into b_img(id, name, bin) values (?,?,?)', (id, name, sqlite3.Binary(file.read())))
#
v1=1000
v2='12345'
v0=101
s1 = 'Introduction to some shinz '+str(v0)
g0 = 'Galileo'
for i in range (0,5):
	cur.execute("INSERT INTO bstore( b_id ,b_name ,author_name ,ratings,book_count ,reviews) values (?,?,?,?,?,?)",(v1,s1,'Xerxes','',v0,'Intro review'))
	v0 +=1
	v1+=1
	v2 += '+'
	s1 = 'Introduction to some shinz '+str(v0)

con.commit()
cur.close()
con.close()
