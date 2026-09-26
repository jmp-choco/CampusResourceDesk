from storage import load_resources, save_resources


def borrow_resource():
    resources = load_resources()

    resource_id = input("Enter resource ID: ")
    quantity = int(input("Enter quantity to borrow: "))

    found = False

    for resource in resources:

        if resource["id"] == resource_id:

            found = True

            if resource["available"] >= quantity:

                resource["available"] = resource["available"] - quantity

                save_resources(resources)

                print("Resource borrowed successfully.")

            else:
                print("Resource is not available in required quantity.")

    if found == False:
        print("Resource not found.")


def return_resource():
    resources = load_resources()

    resource_id = input("Enter resource ID: ")
    quantity = int(input("Enter quantity to return: "))

    found = False

    for resource in resources:

        if resource["id"] == resource_id:

            found = True

            borrowed = resource["total"] - resource["available"]

            if quantity <= borrowed:

                resource["available"] = resource["available"] + quantity

                save_resources(resources)

                print("Resource returned successfully.")

            else:
                print("Invalid quantity.")

    if found == False:
        print("Resource not found.")