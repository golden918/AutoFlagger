# Load Invoice Data in csv
import csv
from Models import Invoice

#Loader
def load_invoices(csv_path):
    invoices = []
    with open(csv_path, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            invoice = Invoice(
                consumer_name=row.get("consumer_name", ""),
                tracking_number=row.get("tracking_number", ""),
                submission_date=row.get("submission_date", ""),
                ip_address=row.get("ip_address", "")
            )
            invoices.append((invoice, row))  # keep original row too
    return invoices

#Writter
def write_flagged_invoices(output_path, headers, data):
    with open(output_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

