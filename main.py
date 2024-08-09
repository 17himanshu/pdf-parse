import os
from dotenv import load_dotenv
import google.generativeai as genai
import PyPDF2
from PIL import Image
import pytesseract
import json
from flask import Flask, request, render_template, jsonify

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

load_dotenv()

genai.configure(api_key=os.getenv("GEMNAI_API_KEY"))

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def extract_invoice_details(text):
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    prompt = f"""
    You are an expert in extracting information from invoices.
    Here is the invoice text:
    
    {text}
    
    Please extract the following details:
    1. Customer Details (including name, address, phone, and email)
    2. Products (including description, HSN code, rate, quantity, and total amount)
    3. Total Amount (including taxable amount, taxes, and final payable amount)
    
    Provide the information in both a structured text format and a JSON format.
    For the Products section in the structured text format, use the following markdown table format:

    **Products:**

    | Description | HSN Code | Rate (₹) | Quantity | Total Amount (₹) |
    |-------------|----------|----------|----------|------------------|
    | [Product 1] | [Code 1] | [Rate 1] | [Qty 1]  | [Amount 1]       |

    Ensure all columns are properly aligned and currency symbols (₹) are used where appropriate.
    """

    try:
        response = model.generate_content(prompt)
        extracted_info = response.text
        return extracted_info
    except Exception as e:
        print(f"Error extracting details: {str(e)}")
        raise

def process_file(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.pdf':
        text = extract_text_from_pdf(file_path)
    elif file_extension in ['.png', '.jpg', '.jpeg']:
        text = extract_text_from_image(file_path)
    else:
        raise ValueError("Unsupported file type")
    
    return extract_invoice_details(text)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            result = process_file(file_path)
            os.remove(file_path)  # Clean up the uploaded file
            return jsonify({"result": result})
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)