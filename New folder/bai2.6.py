# Khai báo các xác suất của số lỗi
probabilities = {
    0: 0.2,
    1: 0.3,
    2: 0.15,
    3: 0.1,
    4: 0.1,
    5: 0.05,
    6: 0.05
}

# Tính xác suất p cho trường hợp > 6 lỗi
p = 1 - sum(probabilities.values())
probabilities["> 6"] = p

# Tính xác suất công nhân mắc từ 3 lỗi trở lên
prob_3_or_more = sum(prob for key, prob in probabilities.items() if key in [3, 4, 5, 6, "> 6"])

print(f"Xác suất công nhân mắc từ 3 lỗi trở lên: {prob_3_or_more}")

# Định nghĩa số tiền thưởng (phạt) tương ứng với số lỗi
rewards = {
    0: 10,
    1: 3,
    2: 3,
    3: 0,
    4: 0,
    5: -2,
    6: -2,
    "> 6": -4
}

# Tính kỳ vọng E(Y)
expected_value = sum(rewards[key] * probabilities[key] for key in probabilities)

# Tính E(Y^2)
expected_value_squared = sum((rewards[key] ** 2) * probabilities[key] for key in probabilities)

# Tính phương sai Var(Y)
variance = expected_value_squared - expected_value ** 2

print(f"Kỳ vọng E(Y): {expected_value}")
print(f"Phương sai Var(Y): {variance}")
