import numpy as np
from sklearn.neural_network import MLPClassifier


# Функция активации (шаговая функция)
def step_function(x):
    return np.where(x >= 0, 1, 0)


class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=1000):
        self.W = np.zeros(input_size + 1)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def predict(self, x):
        return step_function(np.dot(self.W, x))

    def train(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                xi = np.insert(xi, 0, 1)  # Вставка смещения (bias)
                prediction = self.predict(xi)
                self.W += self.learning_rate * (target - prediction) * xi


# Данные для обучения (XOR)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])  # Операция XOR

# Тестирование на 10 000 эпохах
perceptron_10000 = Perceptron(input_size=2, epochs=10000)
perceptron_10000.train(X, y)

print("Тестирование на 10 000 эпохах")
for xi in X:
    xi_with_bias = np.insert(xi, 0, 1)  # Вставка смещения (bias) для тестирования
    print(f"{xi} -> {perceptron_10000.predict(xi_with_bias)}")

# Тестирование на 20 000 эпохах
perceptron_20000 = Perceptron(input_size=2, epochs=20000)
perceptron_20000.train(X, y)

print("\nТестирование на 20 000 эпохах")
for xi in X:
    xi_with_bias = np.insert(xi, 0, 1)  # Вставка смещения (bias) для тестирования
    print(f"{xi} -> {perceptron_20000.predict(xi_with_bias)}")

# Тестирование на 50 000 эпохах
perceptron_50000 = Perceptron(input_size=2, epochs=50000)
perceptron_50000.train(X, y)

print("\nТестирование на 50 000 эпохах")
for xi in X:
    xi_with_bias = np.insert(xi, 0, 1)  # Вставка смещения (bias) для тестирования
    print(f"{xi} -> {perceptron_50000.predict(xi_with_bias)}")

# Данные для обучения (XOR) ================================================================
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])  # Операция XOR

# Создание и обучение MLP-классификатора
mlp = MLPClassifier(hidden_layer_sizes=(5,), activation='relu', max_iter=5000, solver='adam')
mlp.fit(X, y)

# Тестирование
print("\nМногослойный перцептрон (MLP)")
for xi in X:
    print(f"{xi} -> {mlp.predict([xi])[0]}")

"""
Однослойный перцептрон не способен решить XOR так, как XOR это нелинейно разделимая задача, 
а однослойный перцептрон может решать только линейно разделимые задачи.
"""
