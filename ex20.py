"""Faça um programa que peça ao usuário a cidade que ele mora e retorne True caso o nome da cidade inicie com "Rio" e False caso não."""

cidade = input("Digite a sua cidade: ").strip().lower()

print(f"O nome da cidade começa com 'Rio'? {cidade[:3] == 'rio'}")

