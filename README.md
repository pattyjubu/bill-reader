# bill-reader
This project is example code to read the bill by using OCR 

## Input
- Bill image (only order list)

## Output
- CSV file

## Prerequisite
- Install **tesseract** and add to environment variable
	- https://github.com/UB-Mannheim/tesseract/wiki
- PIP install
	```
	pip install opencv-python
	```
	
## How to run
- Example
	```
	(venv) C:\Patty\Learn\BillReader>python source_code/bill_reader.py C:\Patty\Learn\BillReader\test_images\test_bill
	_crop.jpg
	```