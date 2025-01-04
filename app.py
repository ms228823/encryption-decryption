from flask import Flask, render_template, request
from functions import encrypt_text, decrypt_text

app = Flask(__name__)

@app.route('/')
def index():
    # Load the index.html file from the "html" subfolder in templates
    return render_template('html/index.html')

@app.route('/process', methods=['POST'])
def process():
    operation = request.form['operation']
    print(operation)
    text = request.form['text']
    print(text)
    rail_key = int(request.form['rail_key'])
    print(rail_key)
    vigenere_key = request.form['vigenere_key']
    print(vigenere_key)
    caesar_shift = int(request.form['caesar_shift'])
    print(caesar_shift)
    
    # Perform encryption or decryption
    if operation == 'encrypt':
        # result = encrypt_system(text, caesar_shift, vigenere_key, rail_key)
        result = encrypt_text(text, rail_key, vigenere_key, caesar_shift)
        print(f"Result: {result}")
    elif operation == 'decrypt':
        # result = decrypt_system(text, caesar_shift, vigenere_key, rail_key)
        result = decrypt_text(text, rail_key, vigenere_key, caesar_shift)
        print(f"Result: {result}")
    else:
        result = "Invalid Operation"
        print(f"Result: {result}")

    # Load the result.html file from the "html" subfolder in templates
    return render_template('html/result.html', operation=operation, result=result)

if __name__ == '__main__':
    app.run(debug=True)
