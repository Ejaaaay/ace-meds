import json
import datetime
import os

DATA_FILE = "medicine_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_today_key():
    return datetime.date.today().isoformat()

def add_medicine():
    med = input("Enter medicine name: ")
    data = load_data()
    today = get_today_key()

    if today not in data:
        data[today] = {}

    data[today][med] = False  # False = not taken yet
    save_data(data)
    print(f"Added medicine: {med}")

def mark_taken():
    data = load_data()
    today = get_today_key()

    if today not in data:
        print("No medicines added today.")
        return

    meds = list(data[today].keys())
    print("\nMedicines for today:")
    for i, m in enumerate(meds, 1):
        status = "✓" if data[today][m] else "✗"
        print(f"{i}. {m} [{status}]")

    choice = int(input("\nWhich medicine was taken? (number): ")) - 1

    if 0 <= choice < len(meds):
        med = meds[choice]
        data[today][med] = True
        save_data(data)
        print(f"Marked '{med}' as taken.")
    else:
        print("Invalid choice")

def view_status():
    data = load_data()
    today = get_today_key()

    if today not in data:
        print("No medicines added for today.")
        return

    print("\nMedicine status for today:")
    for med, taken in data[today].items():
        print(f"- {med}: {'✓ Taken' if taken else '✗ Not yet'}")

def menu():
    while True:
        print("\n--- Dog Medicine Tracker ---")
        print("1. Add medicine")
        print("2. Mark medicine as taken")
        print("3. View today's status")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_medicine()
        elif choice == "2":
            mark_taken()
        elif choice == "3":
            view_status()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
