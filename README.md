# Excel Data Validator & Cleaner

A Python automation tool for validating, cleaning, and exporting Excel data.
This project is designed as a practical example of data automation using pandas.

## Features
- Load Excel files from a configurable path
- Validate required columns
- Detect and remove invalid or empty rows
- Sort data if needed
- Export cleaned data to a new Excel file
- Clear console feedback during execution

## Project Structure
excel-data-validator/
│
├── data/
│ ├── input.xlsx # Raw input Excel file
│ └── output.xlsx # Cleaned output file
│
├── src/
│ └── main.py # Main application logic
│
├── requirements.txt
├── README.md
└── .gitignore

## Input
The project uses `data/input.xlsx` as a sample input file for demonstration and testing purposes.

## Output
The cleaned and validated file will be generated as `data/output.xlsx`.

## Requirements
- Python 3.9+
- pandas
- openpyxl

## Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/excel-data-validator.git
cd excel-data-validator
2. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies:
pip install -r requirements.txt

## Usage
1. Place your Excel file inside the data/ folder and name it input.xlsx.
2. Run the script:
```bash
python src/main.py
3. The cleaned file will be saved as:
data/output.xlsx

## توضیح فارسی

این پروژه یک اسکریپت پایتون برای اعتبارسنجی و پاک‌سازی فایل‌های اکسل است.

هدف پروژه، بررسی داده‌های ورودی، حذف ردیف‌های نامعتبر و آماده‌سازی داده‌ها برای استفاده در تحلیل یا سیستم‌های دیگر است.

### قابلیت‌ها:
- خواندن فایل اکسل ورودی
- بررسی وجود ستون‌های ضروری
- حذف ردیف‌های ناقص یا نامعتبر
- مرتب‌سازی داده‌ها
- ذخیره خروجی پاک‌سازی‌شده در فایل اکسل جدید

این پروژه به‌عنوان یک نمونه‌کار در حوزه اتوماسیون و پردازش داده با پایتون طراحی شده است.