from resources import add_resource, view_resources
from resources import search_resource, update_quantity

from transactions import borrow_resource, return_resource

from reports import available_resources
from reports import borrowed_resources, usage_information


def resource_menu():

    while True:

        print("\n===== RESOURCE MANAGEMENT =====")
        print("1. Add Resource")
        print("2. View Resources")
        print("3. Search Resource")
        print("4. Update Quantity")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_resource()

        elif choice == "2":
            view_resources()

        elif choice == "3":
            search_resource()

        elif choice == "4":
            update_quantity()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def transaction_menu():

    while True:

        print("\n===== BORROW / RETURN =====")
        print("1. Borrow Resource")
        print("2. Return Resource")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            borrow_resource()

        elif choice == "2":
            return_resource()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


def report_menu():

    while True:

        print("\n===== REPORTS =====")
        print("1. Available Resources")
        print("2. Borrowed Resources")
        print("3. Usage Information")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            available_resources()

        elif choice == "2":
            borrowed_resources()

        elif choice == "3":
            usage_information()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def main():

    while True:

        print("\n==============================")
        print("      CAMPUS RESOURCE DESK")
        print("==============================")
        print("1. Resource Management")
        print("2. Borrow / Return")
        print("3. Reports")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            resource_menu()

        elif choice == "2":
            transaction_menu()

        elif choice == "3":
            report_menu()

        elif choice == "4":
            print("Thank you for using Campus Resource Desk.")
            break

        else:
            print("Invalid choice.")


main()