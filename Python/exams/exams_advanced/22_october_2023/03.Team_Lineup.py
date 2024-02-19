def team_lineup(*args):
    teams_comp = {}
    for arg in args:
        value, key = arg
        if key not in teams_comp:
            teams_comp[key] = [value]
        else:
            teams_comp[key].append(value)

    sorted_teams = sorted(teams_comp.items(), key=lambda x: (-len(x[1]), x[0]))

    output = []
    for team, players in sorted_teams:
        output.append(f"{team}:\n")
        for player in players:
            output.append(f"  -{player}\n")

    return ''.join(output)
