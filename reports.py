from storage import load_resources


def available_resources():
    resources = load_resources()

    print("\n--- Available Resources ---")

    for resource in resources:

        if resource["available"] > 0:

            print(
                resource["id"],
                resource["name"],
                "Available:",
                resource["available"]
            )


def borrowed_resources():
    resources = load_resources()

    print("\n--- Borrowed Resources ---")

    found = False

    for resource in resources:

        borrowed = resource["total"] - resource["available"]

        if borrowed > 0:

            print(
                resource["id"],
                resource["name"],
                "Borrowed:",
                borrowed
            )

            found = True

    if found == False:
        print("No resources are currently borrowed.")


def usage_information():
    resources = load_resources()

    total = 0
    available = 0
    borrowed = 0

    for resource in resources:

        total = total + resource["total"]
        available = available + resource["available"]

    borrowed = total - available

    print("\n--- Usage Information ---")
    print("Total resources:", total)
    print("Available resources:", available)
    print("Borrowed resources:", borrowed)