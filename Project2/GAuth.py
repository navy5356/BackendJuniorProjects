# Still work in progress...



people_resource = service.people()
people_document = people_resource.get(userId='me').execute()

print("ID: " + people_document['id'])
print("Display name: " + people_document['displayName'])
print("Image URL: " + people_document['image']['url'])
print("Profile URL: " + people_document['url'])