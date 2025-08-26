from datetime import datetime

def age_in_days(dob_str: str) -> int:
    """
    Calculate the age of a person in days from DOB (dd/mm/yyyy).
    """
    try:
        dob = datetime.strptime(dob_str, "%d/%m/%Y")
        today = datetime.today()
        return (today - dob).days
    except ValueError:
        raise ValueError("Invalid date format! Please enter in dd/mm/yyyy format.")
    
def main():
    dob_str = input("Enter your Date of Birth (dd/mm/yyyy): ")
    try:
        days = age_in_days(dob_str)
        print(f"Your age is {days} days.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main() 