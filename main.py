# Import modules
import argparse, phonenumbers
from phonenumbers import carrier
 
# Adding an argument for the phone number
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=str, help='set the phone number')
args = parser.parse_args()
 
# Main function
def main():
 
    # Check if the user adds the argument in the terminal
    if args.number:
        target_number = phonenumbers.parse(args.number)  # Parsing the given phone number
        isp = carrier.name_for_number(target_number, 'en')  # Getting the ISP (Internet Service Provider) name
 
        # Displaying the ISP (Internet Service Provider)
        print("=====[OUTPUT]=====")
        print(f"ISP : {isp}") 
 
# Run the code in terminal
if __name__ == "__main__":
    main()
