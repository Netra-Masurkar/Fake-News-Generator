import random

#list of Indian Places
Subjects=[
    "Shahrukh khan",
    "Virat Kohli",
    "Nirmala Sitharam",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

#list of Indian Actions
Actions=[
    "launches",
    "cancels",
    "dances in ",
    "declares war on "
    "eats",
    "orders",
    "celebrates"
]

#List of Indian Places or Things
Places=[
    "at red fort",
    "in mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at ganga Ghat",
    "at village road",
    "in Pune Metro station"
]

while True:
    subject=random.choice(Subjects)
    action=random.choice(Actions)
    place=random.choice(Places)

    headline=f"BREAKING:{subject} {action} {place}".strip().lower()
    print("\n"+ headline)

    user_input=input("\nDo you want another headline ? (Yes/No)")
    if user_input=="no":
        break

print("\n Thanks for using Fake News Headline Generator.Have a fun day")