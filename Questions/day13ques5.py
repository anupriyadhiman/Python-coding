#A dict contains events and corresponding dates, given a date, find out what events have occurred and what are still pending.

events = {
    "Independence Day": "2022, 08, 15",
    "Republic Day": "2022, 01, 26",
    "Christmas": "2022, 12, 25",
    "New Year": "2022, 01, 01",
    "Holi": "2022, 03, 29",
    "Ganesh Chaturthi": "2022, 08, 22",
    "Diwali": "2022, 11, 04",
    "Raksha Bandhan": "2022, 08, 22",
    "Janmashtami": "2022, 08, 22",
    "Guru Nanak Jayanti": "2022, 11, 19",
    "Dussehra": "2022, 10, 14",
}

date1 = input("Enter the date: ")

for event in events:
    if date1 in events[event]:
        print(event, "has occurred")
    else:
        print(event, "has not occurred")

    


