# ENV allpy310
# pip install faker


from faker import Faker
fake = Faker()

def generate_profiles(num_profiles):
    profiles = []
    for _ in range(num_profiles):
        profile = {
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "birth_date": fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=85),
            "company": fake.company(),
            "text": fake.text()
        }
        profiles.append(profile)
    return profiles

if __name__ == "__main__":
    num_profiles_to_generate = 5  # Количество fake-профилей
    profiles = generate_profiles(num_profiles_to_generate)

    for i, profile in enumerate(profiles, start=1):
        print(f"Profile {i}:")
        print(f"Name: {profile['name']}")
        print(f"Address: {profile['address']}")
        print(f"Email: {profile['email']}")
        print(f"Birth Date: {profile['birth_date']}")
        print(f"Company: {profile['company']}")
        print(f"Text: {profile['text']}\n")
