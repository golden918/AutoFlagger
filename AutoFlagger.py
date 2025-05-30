# main file
import os
from InvoiceLoader import load_invoices, write_flagged_invoices
from InconsistencyDetector import detect_inconsistencies

INPUT_CSV = "data/invoices.csv"
OUTPUT_CSV = "data/flagged_invoices.csv"

if not os.path.exists("data"):
    os.makedirs("data")

invoices = load_invoices(INPUT_CSV)
flagged = detect_inconsistencies(invoices)

headers = list(flagged[0].keys()) if flagged else []
write_flagged_invoices(OUTPUT_CSV, headers, flagged)

print("✅ Inconsistency analysis complete. Output saved to:", OUTPUT_CSV)

