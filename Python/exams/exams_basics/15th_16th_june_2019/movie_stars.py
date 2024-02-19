budget_for_actors = float(input())
money_left = budget_for_actors
while True:
    name_actor = input()
    if name_actor == 'ACTION':
        break

    if len(name_actor) <= 15:
        actor_pay = float(input())
        money_left -= actor_pay
    else:
        money_left -= money_left * 0.2

    if money_left <= 0:
        break

if money_left >= 0:
    print(f'We are left with {money_left:.2f} leva.')
else:
    print(f'We need {abs(money_left):.2f} leva for our actors.')
