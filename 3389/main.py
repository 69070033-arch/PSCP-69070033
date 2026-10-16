"""3389: Smart Trash Collector"""
names = ['Plastic', 'Can', 'Glass']

n = int(input())
for _ in range(n):
    weights = list(map(float, input().split()))

    report = [f"{sum(weights):.1f}"]
    if sum(weights) > 50:
        report.append('Overloaded')
    for index, weight in enumerate(weights):
        if weight > 20:
            report.append(f"Check Type {names[index]}")

    print(', '.join(report))
