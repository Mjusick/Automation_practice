from dataclasses import dataclass
from faker import Faker

faker = Faker()


@dataclass
class Client:
    first_name: str = faker.first_name()
    last_name: str = faker.last_name()
    email: str = faker.email()
    password: str = faker.password()
    birth_date: str = faker.date_of_birth()
    company: str = faker.company()
    address_1: str = faker.street_address()
    address_2: str = faker.building_number()
    city: str = faker.city()
    zipcode: str = faker.postcode()
    country: str = faker.country()
    state: str = faker.state()
    other: str = faker.paragraph(1)
    phone: str = faker.bothify('#########')
    mobile: str = faker.bothify('#########')
    alias: str = faker.word()
