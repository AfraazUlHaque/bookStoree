import razorpay
from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# --- CONFIGURATION ---
# Apni Razorpay Keys jo aapne di thi
RAZORPAY_KEY_ID = "rzp_test_S5gTqErA8nobIr"
RAZORPAY_KEY_SECRET = "OJruhDoh1Fnmomw4NhAF1XwV"

# Razorpay Client initialize karna
client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

# Folder jahan aapki book.pdf rakhi hai (static folder)
BOOK_FOLDER = os.path.join(app.root_path, 'static')

# --- ROUTES ---

@app.route('/')
def home():
    # Home page render karte waqt Key ID bhej rahe hain frontend ko
    return render_template('index.html', key_id=RAZORPAY_KEY_ID)

@app.route('/create-order', methods=['POST'])
def create_order():
    try:
        # Step 1: Razorpay ke server par ek naya order banana
        # Amount paise mein hota hai (999 * 100 = 99900)
        data = {
            "amount": 99900, 
            "currency": "INR",
            "receipt": "order_rcptid_11"
        }
        order = client.order.create(data=data)
        
        # Step 2: Order ID frontend ko wapas bhejna
        return jsonify(order)
    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route('/success')
def success():
    # Payment ke baad user is page par aayega
    return render_template('success.html')

@app.route('/download')
def download_file():
    # Yeh route asli PDF file download karwayega
    try:
        return send_from_directory(BOOK_FOLDER, 'book.pdf', as_attachment=True)
    except FileNotFoundError:
        return "Error: 'book.pdf' file static folder mein nahi mili!", 404

if __name__ == '__main__':
    # Server start karna
    app.run(debug=True)


