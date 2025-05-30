#Generic Invoice information class
class Invoice:
    def __init__(self, consumer_name, tracking_number, submission_date, ip_address):
        self.consumer_name = consumer_name.strip().lower()
        self.tracking_number = tracking_number
        self.submission_date = submission_date
        self.ip_address = ip_address