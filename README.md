# Greeting Based on Time

This Python script, `greet_based_on_time.py`, is designed to greet the user based on the current time of the day. It determines whether it's morning, afternoon, evening, or night and prints an appropriate greeting message accordingly.

## Requirements

- Python 3.x

## Usage

1. Clone this repository or download the `greet_based_on_time.py` file.
2. Ensure you have Python installed on your system.
3. Run the script by executing the following command in your terminal:
4. The script will display a greeting message based on the current time of the day.

## Functionality

The script contains a function called `greet_based_on_time()` which:
- Retrieves the current time using the `datetime` module.
- Parses the hour component of the current time.
- Determines the appropriate greeting message based on the time of the day:
  - Morning: 00:00 to 11:59
  - Afternoon: 12:00 to 16:59
  - Evening: 17:00 to 19:59
  - Night: 21:00 to 23:59
- Prints the greeting message to the console.

## Example

For example, if you run the script at 10:30 AM, it will print:


