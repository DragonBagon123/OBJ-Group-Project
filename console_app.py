from database import BabyNameDatabase


def get_int_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    db = BabyNameDatabase()

    while True:
        print("\n=== Baby Name Database Menu ===")
        print("1. Load SSA baby name CSV data")
        print("2. Add a new name record")
        print("3. Search for a name")
        print("4. Update a name record")
        print("5. Delete a name record")
        print("6. Show sample records")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            file_path = input("Enter CSV file path or press Enter for data/names.csv: ")

            if file_path.strip() == "":
                file_path = "names.csv"

            db.load_csv_data(file_path)

        elif choice == "2":
            name = input("Enter name: ").strip()
            sex = input("Enter sex M or F: ").strip().upper()
            count = get_int_input("Enter count: ")
            year = get_int_input("Enter year: ")

            if name == "":
                print("Name cannot be empty.")
            elif sex not in ["M", "F"]:
                print("Sex must be M or F.")
            else:
                db.add_name(name, sex, count, year)

        elif choice == "3":
            name = input("Enter name to search: ").strip()

            if name == "":
                print("Name cannot be empty.")
            else:
                db.search_name(name)

        elif choice == "4":
            record_id = get_int_input("Enter record ID to update: ")
            name = input("Enter new name: ").strip()
            sex = input("Enter new sex M or F: ").strip().upper()
            count = get_int_input("Enter new count: ")
            year = get_int_input("Enter new year: ")

            if name == "":
                print("Name cannot be empty.")
            elif sex not in ["M", "F"]:
                print("Sex must be M or F.")
            else:
                db.update_record(record_id, name, sex, count, year)

        elif choice == "5":
            record_id = get_int_input("Enter record ID to delete: ")
            confirm = input("Type yes to confirm delete: ")

            if confirm.lower() == "yes":
                db.delete_record(record_id)
            else:
                print("Delete cancelled.")

        elif choice == "6":
            db.show_sample_records()

        elif choice == "7":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()
