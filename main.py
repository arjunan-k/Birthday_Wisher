from datetime import datetime
import pandas
import random
import smtplib

EMAIL = "appufortesting@gmail.com"
PASSWORD = "Helloappufortesting10"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthday.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connections:
        connections.starttls()
        connections.login(EMAIL, PASSWORD)
        connections.sendmail(from_addr=EMAIL, to_addrs=birthday_person["email"],
                             msg=f"Subject:Happy Birthday wishes "
                                 f"from me\n\n{new_contents}")