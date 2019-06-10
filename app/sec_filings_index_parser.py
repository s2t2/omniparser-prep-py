import os
import pandas as pd

ARCHIVES_URL = "https://www.sec.gov/Archives"

def find_filing_url(filings_filepath, company_name, form_type):
    """
    Example: find_filing_url("path/to/filings_index.txt", form_type="10-K", company_name="AMAZON COM INC")
    """

    df = pd.read_csv(filings_filepath, sep="|", skiprows=0, verbose=True)

    #breakpoint()

    #filing_row = df[df["Company Name"] == company_name]

    #filing_row = df[df["Company Name"] == company_name and df["Form Type"] == form_type] # NOPE

    #filing_row = df[df["Company Name"] == company_name][df["Form Type"] == form_type]
    #> UserWarning: Boolean Series key will be reindexed to match DataFrame index
    # https://stackoverflow.com/questions/41710789/boolean-series-key-will-be-reindexed-to-match-dataframe-index

    filing_rows = df[df["Company Name"] == company_name]
    filing_rows =  filing_rows[filing_rows["Form Type"] == form_type]

    # https://stackoverflow.com/questions/25254016/pandas-get-first-row-value-of-a-given-column
    filing = filing_rows.iloc[0].to_dict() #> {'CIK': '1018724', 'Company Name': 'AMAZON COM INC', 'Form Type': '10-K', 'Date Filed': '2019-02-01', 'Filename': 'edgar/data/1018724/0001018724-19-000004.txt'}

    filing_address = filing["Filename"] #> 'edgar/data/1018724/0001018724-19-000004.txt'

    filing_url = f"{ARCHIVES_URL}/{filing_address}" #> 'https://www.sec.gov/Archives/edgar/data/1018724/0001018724-19-000004.txt'

    return filing_url



if __name__ == "__main__":

    filings_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "sec_filings_index_201903.txt")
    print("PARSING A TXT FILE...", filings_filepath)

    company_name = "AMAZON COM INC"
    form_type="10-K"
    print("FINDING form '{form_type}' for company '{company_name}'")

    filing_url = find_filing_url(filings_filepath, company_name=company_name, form_type=form_type)
    print("FOUND:", filing_url)
    print("VISIT THAT URL TO SEE THE FILING. THANKS!")
