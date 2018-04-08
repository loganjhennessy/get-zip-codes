from getzipcodes.zipcoderequest import ZipCodeRequest

import argparse
import json


def get_arguments():
    parser = argparse.ArgumentParser(
        prog="getzipcodes",
        description="Get Zip Codes utility script. By default, the script "
                    "will output JSON-formatted zip codes for the specified "
                    "city to the console. Note that you must set a ZIP_KEY"
                    "environment variable to your zipcodeapi.com key.")
    parser.add_argument(
        dest="city", help="City in which to search for zip codes.")
    parser.add_argument(
        dest="state",
        help="Two-character state in which to search for zip codes.")
    parser.add_argument(
        "-f",
        "--file",
        metavar="<file.json>",
        default=False,
        help="path to file to output zip codes in JSON")
    parser.add_argument(
        "-d", "--datastore", action="store_true", help="output to datastore")

    args = parser.parse_args()
    return args.city.lower(), args.state.lower(), args.file, args.datastore


def write_results(city, state, zipcodes, file, datastore):
    output = {
        "city": city,
        "state": state,
        "zipcodes": zipcodes
    }
    print(json.dumps(output, indent=4))

    if file:
        with open(file, "w") as f:
            f.write(json.dumps(output, indent=4))
    if datastore:
        pass


def main():
    city, state, file, datastore = get_arguments()
    zcr = ZipCodeRequest(city, state)
    zipcodes = zcr.execute()
    write_results(city, state, zipcodes, file, datastore)


if __name__ == "__main__":
    main()
