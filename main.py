# Import modules
import argparse
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import NumberParseException

# Adding argument
parser = argparse.ArgumentParser(description="Phone Number ISP Finder")
parser.add_argument("-n", "--number", type=str, required=True, help="Enter phone number with country code")
args = parser.parse_args()

def main():
    try:
        # Parse number with no default region
        target_number = phonenumbers.parse(args.number, None)

        # Validate number
        if not phonenumbers.is_valid_number(target_number):
            print("Invalid phone number!")
            return

        # Get ISP
        isp = carrier.name_for_number(target_number, "en")

        # Get location
        location = geocoder.description_for_number(target_number, "en")

        print("=====[ OUTPUT ]=====")
        print(f"Number   : {args.number}")
        print(f"Location : {location}")
        print(f"Carrier  : {isp}")

    except NumberParseException as e:
        print(f"Error parsing number: {e}")

if __name__ == "__main__":
    main()
