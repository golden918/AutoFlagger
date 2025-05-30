# AutoFlagger

**AutoFlagger** is a simple Python tool that detects inconsistencies in invoice data stored in `.csv` files.

## What It Does

- Flags duplicate submissions by the same consumer within 12 months
- Detects invalid submission date formats
- Outputs a clean CSV file with added flags and reasons

## How It Works

1. Takes an input CSV file called `invoices.csv` (in the `data/` folder)
2. Runs consistency checks
3. Outputs a file called `flagged_invoices.csv` in the same folder

## How to run it

Place Incoices.csv file in the data folder.
Run the AutoFlagger.

## Example Input

```csv
consumer_name,tracking_number,submission_date,ip_address
Alice Johnson,2001,2023-01-15,192.168.1.10
Alice Johnson,2003,2023-12-20,192.168.1.10
Carol Lee,2004,invalid-date,192.168.1.12

Example Output

consumer_name,tracking_number,submission_date,ip_address,inconsistency_flagged,inconsistency_reason
Alice Johnson,2001,2023-01-15,192.168.1.10,0,
Alice Johnson,2003,2023-12-20,192.168.1.10,1,Repeat submission within 12 months
Carol Lee,2004,invalid-date,192.168.1.12,1,Invalid submission_date format
