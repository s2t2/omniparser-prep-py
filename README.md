# data-processing-hero-py

## Setup

```sh
conda create -n omniparser-env python=3.7 # (first time only)
conda activate omniparser-env
```

```sh
pip install -r requirements.txt
```

## Usage

Parsing TXT files:

```sh
python app/txt_parser.py
```

Parsing CSV Files:

```sh
pip install pandas # (first time only)
python app/csv_parser.py
```

Parsing JSON files:

```sh
# basic challenge:
python app/gradebook_parser.py
pytest test/gradebook_parser_test.py

# advanced challenge:
python app/stock_prices_parser.py
pytest test/stock_prices_parser.py
```

Parsing HTML files:

```sh
pip install beautifulsoup4 # (first time only)
python app/html_parser.py
```

```sh
#python app/pdf_parser.py
```

## Testing


```sh

pip install pytest # (first time only)
pytest
```
