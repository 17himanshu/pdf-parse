# Invoice Details Extraction Tool

## Overview

This project is a Python-based tool designed to extract detailed information from invoices, specifically in PDF format. The tool leverages Google Generative AI (`gemini-1.5-pro` model) to process and analyze the text extracted from PDFs, providing structured data such as customer details, product information, and the total amount due.

## Features

- **Invoice Text Extraction**: Utilizes the `PyPDF2` library to extract text from PDF files.
- **AI-Powered Information Extraction**: Employs Google Generative AI to parse the extracted text and retrieve key details like customer information, product details, and financial summaries.
- **Structured Output**: Returns the extracted data in both structured text and JSON formats.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- A Google Generative AI API key
- The following Python libraries installed:
  - `python-dotenv`
  - `google-generativeai`
  - `PyPDF2`

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/17himanshu/pdf-parse.git
    cd pdf-parse
    ```

2. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your Google Generative AI API key:

    ```plaintext
    GEMNAI_API_KEY=your_google_generative_ai_api_key
    ```

## Usage

1. Place the PDF invoice you want to process in the project directory.

2. Run the script with the path to the PDF file:

    ```bash
    python main.py /path/to/your/invoice.pdf
    ```

3. The tool will output the extracted information both in the console and as a structured text and JSON format.

## Example

```bash
python main.py ./invoices/sample_invoice.pdf
