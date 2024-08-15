from collections import deque

monsters_armor = deque([int(x) for x in input().split(',')])
soldiers_striking_impact = deque([int(x) for x in input().split(',')])

killed_monsters = 0

while monsters_armor and soldiers_striking_impact:
    monstr_armor = monsters_armor.popleft()
    soldr_impact = soldiers_striking_impact.pop()

    if soldr_impact >= monstr_armor:
        killed_monsters += 1

        result = soldr_impact - monstr_armor
        if result > 0:
            if soldiers_striking_impact:
                next_elmnt = soldiers_striking_impact.pop()
                new_result = next_elmnt + result
                soldiers_striking_impact.append(new_result)
            else:
                soldiers_striking_impact.append(result)

    else:
        result1 = monstr_armor - soldr_impact
        monsters_armor.append(result1)

if not monsters_armor:
    print("All monsters have been killed!")

if not soldiers_striking_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")


