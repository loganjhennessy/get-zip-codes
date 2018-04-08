from getzipcodes.zipcoderequest import ZipCodeRequest

import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        prog="getzipcodes",
        description="Get Zip Codes utility script. By default, the script "
                    "will output JSON-formatted zip codes for the specified "
                    "city. Note that you must set a ZIP_KEY environment"
                    "variable to your zipcodeapi.com key.")
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
    return args.city, args.state, args.file, args.datastore


def write_results(zipcodes, file, datastore):
    for z in zipcodes[:-1]:
        print(z + ",", end="")
    print(zipcodes[-1])
    if file:
        pass
    if datastore:
        pass


city, state, file, datastore = get_arguments()
zcr = ZipCodeRequest(city, state)
zipcodes = zcr.execute()
write_results(zipcodes, file, datastore)
