def greedy_algorithm(items, budget):
    ratio_list = [(item, data["calories"] / data["cost"]) for item, data in items.items()]
    ratio_list.sort(key=lambda x: x[1], reverse=True)

    total_calories = 0
    total_cost = 0
    selected_items = []

    for item, ratio in ratio_list:
        cost = items[item]["cost"]
        calories = items[item]["calories"]

        if total_cost + cost <= budget:
            selected_items.append(item)
            total_cost += cost
            total_calories += calories

    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]

    for item, data in items.items():
        cost = data["cost"]
        calories = data["calories"]

        for i in range(budget, cost - 1, -1):
            if dp[i - cost] + calories > dp[i]:
                dp[i] = dp[i - cost] + calories
                selected_items[i] = selected_items[i - cost] + [item]

    return selected_items[budget], dp[budget], sum(items[item]["cost"] for item in selected_items[budget])


# Example usage
items = {
 "pizza": {"cost": 50, "calories": 300},
 "hamburger": {"cost": 40, "calories": 250},
 "hot-dog": {"cost": 30, "calories": 200},
 "pepsi": {"cost": 10, "calories": 100},
 "cola": {"cost": 15, "calories": 220},
 "potato": {"cost": 25, "calories": 350}
}

budget = 100
selected_items, total_calories, total_cost = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм. Вибрані види їжі: {selected_items}, всього калорій: {total_calories}, вартість: {total_cost}. Співвідношення: {total_calories / total_cost}")

selected_items, total_calories, total_cost = dynamic_programming(items, budget)
print(f"Динамічне програмування. Вибрані види їжі: {selected_items}, всього калорій: {total_calories}, вартість: {total_cost}. Співвідношення: {total_calories / total_cost}")
