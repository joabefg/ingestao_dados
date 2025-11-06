from faker import Faker

# Inicializa o Faker
fake = Faker()

# Gera um ISBN-13 aleatório e formatado corretamente
isbn_aleatorio = fake.isbn13()

print(isbn_aleatorio)
# Exemplo de saída: 978-0-3021-3972-2