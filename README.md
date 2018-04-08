# Get Zip Codes

Simple command-line utility that wraps the 
[zipcodeapi](https://www.zipcodeapi.com) to get a list of zip codes for a given
city, state combination. The result can be stored as a `.json` file and/or
writen to Google Cloud Datastore. Either way, all output is written to stdout.

## Installation

```bash
git clone https://github.com/loganjhennessy/get-zip-codes.git
cd get-zip-codes
pip install -e .
```

## Usage

You must first [register your app](http://www.zipcodeapi.com/Register) with
[zipcodeapi](https://www.zipcodeapi.com) and obtain a key. The `getzipcodes`
utility looks for the key in the `ZIP_KEY` environment variable, so make sure
you set it accordingly. For example:

```bash
export ZIP_KEY=<your-key>
```

Example of outputting to a file:

```bash
getzipcodes reno nv -f renozips.json
```

Example of saving to Datastore:

```bash
getzipcodes reno nv -d
```

Note: You must have the `GOOGLE_APPLICATION_CREDENTIALS` environment variable
set to the location of your Google Cloud Platform credentials file. Depending
on your current GCP plan, saving to Datastore may incur a charge. Please be
cognizant and *know what you are doing* before doing so.

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