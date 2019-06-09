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

```sh
python app/json_parser.py
pytest test/json_parser_test.py

python app/txt_parser.py

pip install pandas # (first time only)
python app/csv_parser.py

pip install beautifulsoup4 # (first time only)
python app/html_parser.py

#python app/pdf_parser.py
```

## Testing


```sh

pip install pytest # (first time only)
pytest
```
