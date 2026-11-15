import re

def is_valid_email(email):
    if not email or not isinstance(email, str):
        return False
    email = email.strip()
    # Простая проверка: одна @, точка после @, нет пробелов
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

tests = [
    ("", False),
    ("userexample.com", False),
    ("user@example", False),
    ("user @example.com", False),
    (" user@example.com ", True),   # после strip — валидный
    ("user@example.com", True),
    ("user@@example.com", False),
    ("user@example.", False),
]

for email, expected in tests:
    result = is_valid_email(email)
    status = "✅" if result == expected else "❌"
    print(f"{status} is_valid_email({email!r}) = {result} (ожидалось {expected})")