import pandas

ARCHIVES_URL = "https://www.sec.gov/Archives"

def find_filing_url(filings_filepath, company_name, form_type):

    filing_address = "edgar/____________.txt"

    return f"{ARCHIVES_URL}/{filing_address}"


if __name__ == "__main__":

    print("PARSING A TXT FILE...")
