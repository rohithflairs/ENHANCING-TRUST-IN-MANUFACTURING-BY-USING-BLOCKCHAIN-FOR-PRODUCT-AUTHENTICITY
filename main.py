from flask import Flask, render_template, request, redirect, url_for, session, flash
from index import BlockChain
import json

app = Flask(__name__)
app.secret_key = "alkdjfalkdjf"

@app.route("/")
def home():
	if session.get("user"):
		return render_template('home.html')
	else:
		flash("Please login to Continue")
		return redirect(url_for('login'))


@app.route("/lr")
def lr():
	session["r1"] = "r1"
	session["user"] = "admin"
	return render_template('lr.html')


@app.route("/login")
def login():
	session["r1"] = "r1"
	session["user"] = "admin"
	return render_template('login.html')

@app.route("/dashboard")
def dashboard():
	return render_template('dashboard.html')

# @app.route("/login", methods=["POST", "GET"])
# def login():
# 	if request.method == "POST":
# 		user = request.form["username"]
# 		pswd = request.form["password"]
# 		if user == "rohith":
# 			if pswd == "rohith":
# 				session["user"] = "Admin"
# 				flash("Admin Login successful")
# 				return redirect(url_for("admin"))
# 		elif user == "sai":
# 			if pswd == "sai":
# 				session["user"] = "Admin"
# 				flash("Manufacturer Login successful")
# 				return redirect(url_for("tohome"))
# 		else:
# 			flash("Invalid Login details")
# 			return redirect(url_for('login'))
# 	else:
# 		return render_template('login.html')


@app.route("/verify/<kid>", methods=["GET"])
def verify(kid):
		return render_template('verify.html', keyId=kid)


@app.route("/verify", methods=["POST"])
def success():

	post_data = request.form["keyId"]

	with open('./NODES/N1/blockchain.json', 'r') as bfile:
		n1_data = str(bfile.read())
	with open('./NODES/N2/blockchain.json', 'r') as bfile:
		n2_data = str(bfile.read())
	with open('./NODES/N3/blockchain.json', 'r') as bfile:
		n3_data = str(bfile.read())
	with open('./NODES/N4/blockchain.json', 'r') as bfile:
		n4_data = str(bfile.read())

	pd = str(post_data)

	if (pd in n1_data) and (pd in n2_data) and (pd in n3_data) and (pd in n4_data):

		with open('./NODES/N1/blockchain.json', 'r') as bfile:
			for x in bfile:
				if pd in x:
					a = json.loads(x)["data"]
					b = a.replace("'", "\"")
					data = json.loads(b)

					product_brand = data["Manufacturer"]
					product_name = data["ProductName"]
					product_batch = data["ProductBatch"]
					manuf_date = data["ProductManufacturedDate"]
					expiry_date = data["ProductExpiryDate"]
					product_id = data["ProductId"]
					product_price = data["ProductPrice"]
					product_size = data["ProductSize"]
					product_type = data["ProductType"]
		
		return render_template('success.html', brand=product_brand, name=product_name, batch=product_batch, manfdate=manuf_date, exprydate=expiry_date, id=product_id, price=product_price, size=product_size, type=product_type)
	
	else:
		return render_template('fraud.html')


@app.route("/addproduct", methods=["POST", "GET"])
def addproduct():
	if request.method == "POST":
		brand	 = request.form["brand"]
		name	 = request.form["name"]
		batch	 = request.form["batch"]
		pid	 	 = request.form["id"]
		manfdate = request.form["manfdate"]
		exprydate= request.form["exprydate"]
		price	 = request.form["price"]
		size	 = request.form["size"]
		ptype	 = request.form["type"]
		
		print(brand, name, batch, manfdate, exprydate, pid, price, size, ptype)
		bc = BlockChain()
		bc.addProduct(brand, name, batch, manfdate, exprydate, pid, price, size, ptype)
		
		flash("Product added successfully to the Blockchain")
		# return render_template('home.html')
		# return redirect(url_for('home')) #OLD LINE
		return render_template('AfterAddition.html') # NEW LINE
	else:
		# return render_template('home.html')
		return redirect(url_for('home'))


@app.route("/admin", methods=["POST", "GET"])
def admin():
	if session.get("user"):
	# if session["user"] == "admin":
			return render_template('admin.html')
	else:
		flash("Please Login before singining as Admin.")
		return redirect(url_for('login'))


	# if session["user"] == "Admin":
	# 	return render_template('admin.html')
	# else:
	# 	flash("Please Login Again")
	# 	return redirect(url_for('login'))


@app.route("/verifyNodes")
def verifyNodes():
	bc = BlockChain()
	isBV = bc.isBlockchainValid()

	if isBV:
		flash("All Nodes of Blockchain are valid")
		return redirect(url_for('admin'))
	else:
		flash("Blockchain Nodes are not valid")
		return redirect(url_for('admin'))


@app.route("/medicine")
def medicine():
	return render_template('MedicinePage.html')


@app.route("/fertilizer")
def fertilizer():
	return render_template('FertilizersPage.html')


@app.route("/shoes")
def shoes():
	return render_template('ShoesPage.html')


@app.route("/wine")
def wine():
	return render_template('WinePage.html')

@app.route("/newproduct")
def newproduct():
	return render_template('NewProductPage.html')


@app.route("/electronicproduct")
def electronicproduct():
	return render_template('electronicproduct.html')


@app.route("/cosmeticproduct")
def cosmeticproduct():
	return render_template('cosmeticproduct.html')

@app.route("/accesoriesproduct")
def accesoriesproduct():
	return render_template('accesoriesproduct.html')

@app.route("/homeproduct")
def homeproduct():
	return render_template('homeproduct.html')

@app.route("/productzone")
def productzone():
	return render_template('productzone.html')

@app.route("/team")
def team():
	return render_template('team.html')

@app.route("/contactus")
def contactus():
	return render_template('contact form/index.html')


@app.route("/tohome")
def tohome():
	if session["r1"] == "r1":
		session["user"] = "user"
		return render_template('home.html')
	else:
		flash("Please Login before singining into the Homepage.")
		return redirect(url_for('login'))
	# if session.get("user"):
	# 	return render_template('home.html')
	# else:
	# 	flash("Please Login before singining into the Homepage.")
	# 	return redirect(url_for('login'))

	# return render_template('home.html')

@app.route("/navbar")
def navbar():
	return render_template('navbar.html')

# @app.route("/navbar1css")
# def navbar1css():
# 	return render_template('navbar1css.css')

# @app.route("/navbar1js")
# def navbar1js():
# 	return render_template('navbar1js.js')


@app.route("/showallqr")
def showallqr():
	return render_template('your_html_page101.html')

@app.route("/showqr")
def showqr():
	return render_template('your_html_page.html')	


@app.route("/showallqrphp")
def showallqrphp():
	return render_template('get_images101.php')

@app.route("/showqrphp")
def showqrphp():
	return render_template('get_images.php')	


@app.route("/logout")
def logout():
	session["user"] = ""
	session["r1"] = ""
	flash("LOGGED OUT SUCCESSFULLY")
	return redirect(url_for('login'))




if __name__ == "__main__":
    app.run(debug=True)
    session["user"] = ""