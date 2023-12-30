def create_force_profile(force_user: str, force_side: str, forcebook: dict):
    for side, users in forcebook.items():
        if force_user in users:
            return
    force_book.setdefault(force_side, []).append(force_user)


def switch_force_side(forcebook: dict, force_user: str, force_side: str):
    for key, users in forcebook.items():
        if force_user in users:
            users.remove(force_user)
            forcebook.setdefault(force_side, []).append(force_user)
            return key

    create_force_profile(force_user, force_side, forcebook)


force_book = {}
line = input()
while line != 'Lumpawaroo':
    if '|' in line:
        side, user = line.split(' | ')
        create_force_profile(user, side, force_book)
    elif '->' in line:
        user, side = line.split(' -> ')
        switch_force_side(force_book, user, side)
        print(f'{user} joins the {side} side!')
    line = input()
for side, members in force_book.items():
    if members:
        print(f'Side: {side}, Members: {len(members)}')
        for member in members:
            print(f'! {member}')
