"""3482: นักล่าอสูร"""
demons = ['Spider Demon', 'Swamp Demon', 'Arrow Demon', 'Hand Demon',
          'Drum Demon', 'Mugen Train', 'Upper Moon']
weak_points = [1, 2, 1, 2, 3, 2, 3]

kills = 0
attacks = 0
next_demon = 0
retry = []

while kills < 5:
    if retry:
        current = retry.pop(0)
    else:
        current = next_demon
        next_demon += 1

    print(demons[current], flush=True)

    defeated = False
    for chance in range(2):
        attack = int(input().strip())
        attacks += 1

        if attack == weak_points[current]:
            print('kill', flush=True)
            defeated = True
            break
        if chance == 1:
            print('back', flush=True)
            retry.append(current)

    if defeated:
        kills += 1

print(attacks)
