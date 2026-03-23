from faker import Faker

faker = Faker("pt_BR")

print("Nome aleatório:", faker.name())
print("Cidade aleatória:", faker.city())
print("Data aleatória:", faker.date())