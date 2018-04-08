# Get Zip Codes

Simple service that wraps the [zipcodeapi](https://www.zipcodeapi.com) to get
a list of zip codes for a given city, state combination. The result can be
stored as a `.json` file or writen to Google Cloud Datastore

## Usage

Example output to file:
```bash
getzipcodes reno nv -f renozips.json
```

Example output to Datastore
```bash
getzipcodes reno nv -d
```
