from storage import load_resources, save_resources


def add_resource():
    resources = load_resources()

    resource_id = input("Enter resource ID: ")
    name = input("Enter resource name: ")
    category = input("Enter category: ")
    quantity = int(input("Enter quantity: "))

    resource = {
        "id": resource_id,
        "name": name,
        "category": category,
        "total": quantity,
        "available": quantity
    }

    resources.append(resource)

    save_resources(resources)

    print("Resource added successfully.")


def view_resources():
    resources = load_resources()

    if len(resources) == 0:
        print("No resources available.")
    else:
        print("\n--- Resources ---")

        for resource in resources:
            print("ID:", resource["id"])
            print("Name:", resource["name"])
            print("Category:", resource["category"])
            print("Total:", resource["total"])
            print("Available:", resource["available"])
            print("--------------------")


def search_resource():
    resources = load_resources()

    search = input("Enter resource name: ")

    found = False

    for resource in resources:

        if resource["name"].lower() == search.lower():
            print("\nResource found")
            print("ID:", resource["id"])
            print("Name:", resource["name"])
            print("Category:", resource["category"])
            print("Total:", resource["total"])
            print("Available:", resource["available"])

            found = True

    if found == False:
        print("Resource not found.")


def update_quantity():
    resources = load_resources()

    resource_id = input("Enter resource ID: ")
    new_quantity = int(input("Enter new quantity: "))

    found = False

    for resource in resources:

        if resource["id"] == resource_id:

            borrowed = resource["total"] - resource["available"]

            resource["total"] = new_quantity
            resource["available"] = new_quantity - borrowed

            found = True

    if found == True:
        save_resources(resources)
        print("Quantity updated successfully.")
    else:
        print("Resource not found.")