import argparse
import json

from getzipcodes.log import get_configured_logger
from getzipcodes.zipcoderequest import ZipCodeRequest
from google.cloud import datastore

logger = get_configured_logger(__name__, "INFO")


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


def write_results(city, state, zipcodes, file, ds):
    output = {
        "city": city,
        "state": state,
        "zipcodes": zipcodes
    }
    print(json.dumps(output, indent=4))

    if file:
        with open(file, "w") as f:
            f.write(json.dumps(output, indent=4))
        logger.info("Output saved to {}".format(file))
    if ds:
        ds_client = datastore.Client()
        kind = "CityZipCodeMap"
        name = '-'.join([city, state])
        key = ds_client.key(kind, name)

        city_zip_map = datastore.Entity(key=key)
        city_zip_map["city"] = city
        city_zip_map["state"] = state
        city_zip_map["zipcodes"] = zipcodes

        ds_client.put(city_zip_map)
        logger.info("Output uploaded to {} kind with key {}.".format(kind, key))


def main():
    city, state, file, ds = get_arguments()
    zcr = ZipCodeRequest(city, state)
    zipcodes = zcr.execute()
    write_results(city, state, zipcodes, file, ds)


if __name__ == "__main__":
    main()
