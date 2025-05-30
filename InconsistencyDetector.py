# Detects inconsistant data
from datetime import datetime, timedelta

def detect_inconsistencies(invoices):
    """
    Flags inconsistencies based on repeat submissions by the same consumer
    within a 12-month period.
    """
    submission_history = {}
    processed_data = []

    for invoice, original_row in invoices:
        name = invoice.consumer_name
        date_str = invoice.submission_date

        try:
            submission_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            original_row["inconsistency_flagged"] = "1"
            original_row["inconsistency_reason"] = "Invalid submission_date format"
            processed_data.append(original_row)
            continue

        flagged = False
        reason = ""

        if name in submission_history:
            previous_date = submission_history[name]
            if submission_date - previous_date < timedelta(days=365):
                flagged = True
                reason = "Repeat submission within 12 months"

        original_row["inconsistency_flagged"] = "1" if flagged else "0"
        original_row["inconsistency_reason"] = reason
        submission_history[name] = submission_date
        processed_data.append(original_row)

    return processed_data
