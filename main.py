import requests
from bs4 import BeautifulSoup
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
import time
from datetime import datetime
import pytz

# Get the timezone object for New York
current_timex = pytz.timezone('Asia/Dhaka')

# Get the current time in New York
datetime_NY = datetime.now(current_timex)
current_time =datetime_NY.strftime("%I:%M:%S %p")


from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

print(f"Script is running successfully!! {current_time}")


#Enter Your SLACK Channel Token, ID, User_ID

def send_slack_notification(course_code):
    slack_token = "xoxb-****************-wmgz1WZZS1kwj0E*********"   
    channel_id = "C06DY******"
    user_id = "U06EK*****"

    client = WebClient(token=slack_token)

    try:


        # Send a simple message to the channel
        response = client.chat_postMessage(
            channel=channel_id,
            text=f" <@{user_id}>!  {course_code} is available now! Check the website for more details."
        )

        print("Slack notification sent successfully!")
        print(response)

    except SlackApiError as e:
        print(f"Error sending Slack notification: {e.response['error']}")





# Function to scrape and check seat availability
def check_seat_availability(course_code):


    url = "https://usis.bracu.ac.bd/academia/admissionRequirement/getAvailableSeatStatus"  # Replace with the actual URL of the website

    # Make a request to the website
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table with course information
        table = soup.find('table')

        # print(table)

        # Find all rows in the table
        rows = table.find_all('tr')[1:]  # Skip the header row
        # print(rows)
        for row in rows:
            # Extract data from each row
            data = row.find_all('td')
            course_info = {
                "Course Code": data[1].text.strip(),
                "Section": data[5].text.strip(),
                "Faculty": data[3].text.strip(),
                "Seat Remaining": int(data[9].text.strip())
            }

            # print(course_info)

            # Check if the course code matches the desired code
            if course_info["Course Code"] in course_code:
                # Check if seat remaining is 1 or more
                if course_info["Course Code"] == "CSE321" and course_info['Section'] == "02"  and course_info["Seat Remaining"] >= 1:
                    # if course_info['Section'] == "04" or course_info['Section'] == "05" and course_info["Seat Remaining"] >= 1:
                    # Notify and write to a text file
                    notification = f"  {course_info['Course Code']} Section {course_info['Section']} {course_info['Faculty']} {course_info['Seat Remaining']} is available now!    at {current_time}"
                    with open("notification.txt", "a") as file:
                        file.write(notification + "\n")
                    print(notification)
                    send_slack_notification(notification)

            # if course_info["Course Code"] in course_code:
            #     # Check if seat remaining is 1 or more
            #     if course_info['Course Code'] == "CSE447" and course_info["Seat Remaining"] >= 1:
            #         # Notify and write to a text file
            #         notification = f"  {course_info['Course Code']} Section {course_info['Section']} {course_info['Faculty']} {course_info['Seat Remaining']} is available now!   at {current_time}"
            #         with open("notification.txt", "a") as file:
            #             file.write(notification + "\n")
            #         print(notification)
            #
            #         # Change this line in check_seat_availability function
            #         # send_slack_notification(course_info['Course Code'])
            #         send_slack_notification(notification)

# Check if the course code matches the desired code
            if course_info["Course Code"] in course_code:
                # Check if seat remaining is 1 or more
                if course_info["Course Code"] == "CSE422" and course_info['Section'] == "07"  and course_info["Seat Remaining"] >= 1:
                    # if course_info['Section'] == "04" or course_info['Section'] == "05" and course_info["Seat Remaining"] >= 1:
                    # Notify and write to a text file
                    notification = f"  {course_info['Course Code']} Section {course_info['Section']} {course_info['Faculty']} {course_info['Seat Remaining']} is available now!    at {current_time}"
                    with open("notification.txt", "a") as file:
                        file.write(notification + "\n")
                    print(notification)
                    send_slack_notification(notification)


            if course_info["Course Code"] in course_code:
                # Check if seat remaining is 1 or more
                if course_info["Course Code"] == "CSE422" and course_info['Section'] == "09"  and course_info["Seat Remaining"] >= 1:
                    # if course_info['Section'] == "04" or course_info['Section'] == "05" and course_info["Seat Remaining"] >= 1:
                    # Notify and write to a text file
                    notification = f"  {course_info['Course Code']} Section {course_info['Section']} {course_info['Faculty']} {course_info['Seat Remaining']} is available now!    at {current_time}"
                    with open("notification.txt", "a") as file:
                        file.write(notification + "\n")
                    print(notification)
                    send_slack_notification(notification)


# Set the courses you want to monitor
courses_to_monitor = [ "CSE321", "CSE422"]

# Set the interval for checking seat availability (in seconds)
check_interval = 0.01  # 5 minutes

while True:
    for course in courses_to_monitor:
        check_seat_availability([course])


    # Wait for the specified interval before checking again
    time.sleep(check_interval)

