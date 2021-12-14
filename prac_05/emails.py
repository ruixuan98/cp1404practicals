"""
CP1404 Practicals
Store users' emails and print them when prompted
"""


def main():
    emails = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        name_confirmation = input(f"Is your name {name}? (Y/N)").title()
        if name_confirmation.title() != "Y":
            name = input("Name: ").title()
        emails[email] = name
        email = input("Email: ")
    for email, name in emails.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    name = email.split("@")[0]
    parts = name.split(".")
    name = " ".join(parts).title()
    return name


main()
