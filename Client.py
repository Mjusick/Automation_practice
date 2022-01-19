from faker import Faker


class Client:

    def __init__(self, faker: Faker):
        self.first_name: str = faker.first_name()
        self.last_name: str = faker.last_name()
        self.email: str = faker.email()
        self.password: str = faker.password()
        self.birth_date: str = faker.date_of_birth()
        self.company: str = faker.company()
        self.address_1: str = faker.street_address()
        self.address_2: str = faker.building_number()
        self.city: str = faker.city()
        self.zipcode: str = faker.postcode()
        self.country: str = faker.country()
        self.state: str = faker.state()
        self.other: str = faker.paragraph(1)
        self.phone: str = faker.bothify('#########')
        self.mobile: str = faker.bothify('#########')
        self.alias: str = faker.word()
