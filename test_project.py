from storage import load_resources, save_resources


print("Testing Campus Resource Desk")

resources = load_resources()

print("Current resources:", resources)

test_resource = {
    "id": "TEST01",
    "name": "Test Cable",
    "category": "Electronics",
    "total": 2,
    "available": 2
}

resources.append(test_resource)

save_resources(resources)

print("Test resource added.")

resources = load_resources()

print("Resources after test:")
print(resources)

print("Testing completed.")