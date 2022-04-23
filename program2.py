def add_integers(num):
        return (num - 1) % 9 + 1 if num > 0 else 0

print(add_integers(38))
print(add_integers(59))