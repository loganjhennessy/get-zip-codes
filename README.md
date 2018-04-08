# Get Zip Codes

Simple command-line utility that wraps the 
[zipcodeapi](https://www.zipcodeapi.com) to get a list of zip codes for a given
city, state combination. The result can be stored as a `.json` file or writen
to Google Cloud Datastore.

All output is written to stdout.

## Installation

```bash
git clone https://github.com/loganjhennessy/get-zip-codes.git
cd get-zip-codes
pip install -e .
```

## Usage

Example of outputting to file:

```bash
getzipcodes reno nv -f renozips.json
```

Example of outputting to Datastore:

```bash
getzipcodes reno nv -d
```

## Example Output

```JSON
{
    "city": "reno",
    "state": "nv",
    "zipcodes": [
        "89501",
        "89502",
        "89503",
        "89504",
        "89505",
        "89506",
        "89507",
        "89508",
        "89509",
        "89510",
        "89511",
        "89512",
        "89513",
        "89515",
        "89519",
        "89520",
        "89521",
        "89523",
        "89533",
        "89555",
        "89557",
        "89570",
        "89595",
        "89599"
    ]
}
```