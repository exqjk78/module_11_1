import requests
import matplotlib.pyplot as plt

response = requests.get('https://api.github.com')

print("Статус код:", response.status_code)
print("Содержимое:", response.json())




x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')

plt.title('Простая линейная графика')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()

plt.show()