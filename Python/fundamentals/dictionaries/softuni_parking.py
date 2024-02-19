def register_car(name, plate):
    if name not in parking_lot:
        parking_lot[name] = plate
        print(f'{name} registered {plate} successfully')
    else:
        print(f'ERROR: already registered with plate number {plate}')


def unregister_car(name):
    if name not in parking_lot:
        print(f'ERROR: user {name} not found')
    else:
        del (parking_lot[name])
        print(f'{name} unregistered successfully')


num_of_commands = int(input())

parking_lot = {}
for _ in range(num_of_commands):
    command = input().split()
    action, username = command[0], command[1]
    if action == 'register':
        license_plate = command[2]
        register_car(username, license_plate)
    elif action == 'unregister':
        unregister_car(username)

for username, license_plate in parking_lot.items():
    print(f'{username} => {license_plate}')
