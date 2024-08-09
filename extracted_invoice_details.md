## Structured Text Format:

**Customer Details:**

* Name: TEST
* Address: Test, Hyderabad, TELANGANA, 500089
* Phone: 9108239284
* Email: test@gmail.com

**Products:**

| Description                      | HSN Code       | Rate (₹) | Quantity | Total Amount (₹) |
|----------------------------------|----------------|----------|----------|------------------|
| WASTE AND SCRAP OF STAINLESS STEEL | 72042190       | 95.00    | 6,790 KGS | 6,45,050.00     |

**Total Amount:**

* Taxable Amount: ₹6,45,050.00
* IGST (18.0%): ₹1,16,109.00
* TCS @ 1% 206C: ₹7,611.59
* Round Off: ₹0.41
* **Total Payable Amount:** ₹7,68,771.00 


## JSON Format:

```json
{
  "Customer Details": {
    "Name": "TEST",
    "Address": "Test, Hyderabad, TELANGANA, 500089",
    "Phone": "9108239284",
    "Email": "test@gmail.com"
  },
  "Products": [
    {
      "Description": "WASTE AND SCRAP OF STAINLESS STEEL",
      "HSN Code": "72042190",
      "Rate": 95.00,
      "Quantity": "6,790 KGS",
      "Total Amount": 645050.00
    }
  ],
  "Total Amount": {
    "Taxable Amount": 645050.00,
    "IGST": 116109.00,
    "TCS": 7611.59,
    "Round Off": 0.41,
    "Total Payable Amount": 768771.00
  }
}
``` 
