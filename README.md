# Sales-analytics-system

A Python-based sales analytics application that reads raw sales data, cleans and validates it, performs detailed analysis, enriches data using an external API, and generates a comprehensive sales report.

This project is built as part of a Masai School evaluation and follows all required guidelines and folder structure.

---

##  Features

* Encoding-safe file reading (`utf-8`, `latin-1`, `cp1252`)
* Data parsing, cleaning, and validation
* Interactive filtering options
* Sales analytics and insights
* External API integration for product enrichment
* Professional text-based report generation
* Robust error handling
* Clean console output

---

##  Project Structure

```
sales-analytics-system/
│
├── data/
│   ├── sales_data.txt
│   └── enriched_sales_data.txt
│
├── output/
│   └── sales_report.txt
│
├── utils/
│   ├── file_handler.py
│   ├── data_cleaner.py
│   ├── validator.py
│   ├── analytics.py
│   ├── api_handler.py
│   └── report_generator.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python 3.x
* requests (for API integration)
* Python Standard Library modules

---

## Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/<your-username>/sales-analytics-system.git
cd sales-analytics-system
```

###  Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run the Project

```bash
python main.py
```

---

---

##  Generated Files

### `data/enriched_sales_data.txt`

* Pipe (`|`) separated enriched sales data
* Includes API-enriched product information
* Generated automatically

### `output/sales_report.txt`

* Comprehensive sales analytics report
* Contains all **8 required sections**
* Properly formatted and aligned
* Generated automatically

---

## Report Sections Included

1. Overall Summary
2. Region-wise Performance
3. Product-wise Performance
4. Date-based Analysis
5. Customer Analysis
6. Payment / Order Insights
7. Low Performing Products
8. API Enrichment Summary

---

## ✅ Evaluation Checklist Compliance

* ✔ Correct repository name
* ✔ Proper folder structure
* ✔ Encoding-safe file handling
* ✔ Data validation & filtering
* ✔ API integration using `requests`
* ✔ All required outputs generated
* ✔ No hardcoded file paths
* ✔ Code runs end-to-end without errors


---

##  Author

**Vijay Rawal**

