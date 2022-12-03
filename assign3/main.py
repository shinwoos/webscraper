numbers = [1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8, "🔥", 9, "⭐️", 10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16]


while "💖" in numbers:
    numbers.remove("💖")
    numbers.remove("🔥")
    numbers.remove("⭐️")

sum_numbers = sum(numbers)
print(sum_numbers)