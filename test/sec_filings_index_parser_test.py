import os

from app.sec_filings_index_parser import ARCHIVES_URL, find_filing_url

def test_archives_url():
    assert ARCHIVES_URL == "https://www.sec.gov/Archives"

# CIK|Company Name|Form Type|Date Filed|Filename
# 1018724|AMAZON COM INC|10-K|2013-01-30|edgar/data/1018724/0001193125-13-028520.txt

def test_find_filing_url():
    #older_filings_index_filepath = "data/sec_filings_index_201903.txt"
    #older_filing_url = find_filing_url(older_filing_url, form_type="10-K", company="AMAZON COM INC")
    #assert(amazon_10k_filing_url) == "edgar/data/1018724/0001193125-13-028520.txt"

    filepath = os.path.join(os.path.dirname(__file__), "..", "data", "sec_filings_index_201903.txt")

    filing_url = find_filing_url(filepath, form_type="10-K", company_name="AMAZON COM INC")

    #assert(filing_url) == "edgar/data/1018724/0001018724-19-000004.txt"
    assert(filing_url) == "https://www.sec.gov/Archives/edgar/data/1018724/0001018724-19-000004.txt"
