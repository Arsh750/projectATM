from flask import Flask, render_template, request, redirect, url_for, flash, session
from UserManager_class import UserManager
from Account_class import account
from Transaction_class import Transaction
from cards_class import Cards

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flash messages

# Initialize UserManager
user_manager = UserManager()

# Home route
@app.route("/")
def home():
    return render_template("login.html")

# User registration route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        name = request.form["name"]
        email = request.form["email"]
        message = user_manager.register_user(username, password, name, email)
        flash(message)
        if "successfully" in message:
            return redirect(url_for("home"))
    return render_template("register.html")

# User login route
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    message = user_manager.login_user(username, password)
    flash(message)
    if "Welcome" in message:
        session["username"] = username  # Set the session key here
        return redirect(url_for("dashboard"))
    return redirect(url_for("home"))

# Dashboard route
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Account management route
@app.route("/account", methods=["GET", "POST"])
def account_management():
    if request.method == "POST":
        action = request.form["action"]
        amount = float(request.form.get("amount", 0))
        if action == "deposit":
            flash(account_obj.deposit(amount))
        elif action == "withdraw":
            flash(account_obj.withdraw(amount))
    return render_template("account.html", account=account_obj)

# Transaction management route
@app.route("/transaction", methods=["GET", "POST"])
def transaction_management():
    if request.method == "POST":
        transaction_type = request.form["transaction_type"]
        amount = float(request.form["amount"])
        remarks = request.form["remarks"]
        transaction = Transaction(
            transaction_id="TXN123",
            cid="CID123",
            transaction_type=transaction_type,
            transaction_amount=amount,
            remarks=remarks,
        )
        flash(f"Transaction successful: {transaction.transaction_id}")
    return render_template("transaction.html")

# Card management route
@app.route("/cards", methods=["GET", "POST"])
def card_management():
    if request.method == "POST":
        card_type = request.form["card_type"]
        card_id = request.form["card_id"]
        card = Cards(card_id=card_id, card_type=card_type)
        flash(card.activate_card()) # This will now call the activate_card method
    return render_template("cards.html")

@app.route("/logout")
def logout():
    # Clear the session data
    if "username" in session:
        session.pop("username", None)
        flash("You have been logged out.")
    else:
        flash("No active session found.")
    return redirect(url_for("home"))

if __name__ == "__main__":
    # Create a sample account object for demonstration
    account_obj = account("admin", "password123")
    app.run(debug=True)