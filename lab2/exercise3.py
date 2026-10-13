# (morning, afternoon, night) for Saturday, then the same for Sunday
temperatures = (22, 31, 25, 21, 33, 26)

print("Recorded temperatures:")
for temp in temperatures:
    print(temp, "°C")

print("Highest temperature:", max(temperatures), "°C")
print("Lowest temperature :", min(temperatures), "°C")