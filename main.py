import os
from dotenv import load_dotenv
import google.generativeai as genai
import PyPDF2
import json

load_dotenv()

genai.configure(api_key=os.getenv("GEMNAI_API_KEY"))

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
        print("Extracted Information:")
        print(extracted_info)
        return extracted_info
    except Exception as e:
        print(f"Error extracting details: {str(e)}")
        raise

def process_invoice_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
        
        extracted_details = extract_invoice_details(text)
        return extracted_details
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        raise

def save_extracted_info(extracted_info, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(extracted_info)

# Example usage
pdf_path = 'c669abb4-f485-4880-8973-cc7fdfeee22e.pdf'
output_file = 'extracted_invoice_details.md'

try:
    result = process_invoice_pdf(pdf_path)
    save_extracted_info(result, output_file)
    print(f"Invoice details extracted successfully and saved to {output_file}")
except Exception as e:
    print(f"Failed to process invoice: {str(e)}")