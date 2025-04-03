Окей, я перепишу статью, ориентируясь на использование открытых данных и расширю ее полезными для ML/AI примерами.

```markdown
# Jupyter Notebook: Интерактивная среда для ML/AI с использованием открытых данных

## Что такое Jupyter Notebook?

Jupyter Notebook — это интерактивная среда разработки, позволяющая объединять код, визуализации и текст в едином документе. Это незаменимый инструмент для анализа данных, машинного обучения и научных исследований.

### Ключевые особенности:
- Интерактивное выполнение кода (Python, R и др.)
- Поддержка Markdown и LaTeX для создания красивых отчетов.
- Мощные библиотеки визуализации (Matplotlib, Seaborn, Plotly).
- Простота экспорта в различные форматы (HTML, PDF, слайды).
- Интерактивные виджеты для создания пользовательских интерфейсов.
- Легкая интеграция с облачными сервисами и Big Data.

---

## Установка и запуск в Google Colab

Google Colab предоставляет Jupyter Notebook прямо в вашем браузере, не требуя локальной установки!

1.  Перейдите на [colab.research.google.com](colab.research.google.com).
2.  Создайте новый блокнот (File -> New notebook).
3.  Начните кодить!  Все необходимые библиотеки (Pandas, NumPy, Scikit-learn и т.д.) уже предустановлены.

---

## Интерфейс и базовое использование

Интерфейс Colab максимально прост и интуитивен:

1.  **Ячейки с кодом:**  Пишите и выполняйте Python-код.
2.  **Ячейки Markdown:**  Оформляйте текст, добавляйте заголовки, списки, формулы и изображения.

### Горячие клавиши (в Colab):

*   **Ctrl+Enter** (или **Shift+Enter**): Выполнить ячейку и перейти к следующей.
*   **Ctrl+M A**: Вставить ячейку выше текущей.
*   **Ctrl+M B**: Вставить ячейку ниже текущей.
*   **Ctrl+M M**: Преобразовать ячейку в Markdown.
*   **Ctrl+M Y**: Преобразовать ячейку в Code.
*   **Ctrl+M D**: Удалить ячейку.

---

## Примеры использования с открытыми данными

### 1. Анализ данных о пассажирах Титаника с Pandas и Seaborn

Этот пример демонстрирует загрузку данных из открытого источника (CSV-файл на GitHub), базовый анализ с использованием Pandas и визуализацию с помощью Seaborn.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных с GitHub
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(url)

# Вывод первых строк таблицы
print("Первые 5 строк данных:")
print(titanic_df.head())

# Основная статистика
print("\nОписательная статистика:")
print(titanic_df.describe())

# Визуализация распределения выживших
sns.countplot(x='Survived', data=titanic_df)
plt.title('Распределение выживших')
plt.show()

# Зависимость выживания от класса билета
sns.countplot(x='Pclass', hue='Survived', data=titanic_df)
plt.title('Выживаемость по классам билетов')
plt.show()

# Гистограмма возраста
sns.histplot(titanic_df['Age'].dropna(), kde=True) # Dropna чтобы избавиться от отсутствующих значений
plt.title('Распределение возраста пассажиров')
plt.show()
```

### 2. Классификация изображений с помощью MNIST и Keras

Этот пример показывает, как загрузить набор данных MNIST (рукописные цифры) из Keras, построить и обучить простую нейронную сеть для классификации изображений.

```python
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers

# Загрузка данных MNIST
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Нормализация данных (масштабирование к диапазону [0, 1])
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255

# Преобразование формы данных для нейронной сети (выпрямление изображений в векторы)
x_train = x_train.reshape((-1, 28 * 28))
x_test = x_test.reshape((-1, 28 * 28))

# Определение модели
model = keras.Sequential([
    layers.Dense(512, activation="relu", input_shape=(28 * 28,)),
    layers.Dropout(0.5),
    layers.Dense(10, activation="softmax"), # 10 классов (цифры 0-9)
])

# Компиляция модели
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Обучение модели
history = model.fit(x_train, y_train, epochs=2, batch_size=32, validation_split=0.2)

# Оценка модели
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"Точность на тестовых данных: {accuracy:.4f}")

# Вывод графика обучения
plt.plot(history.history['accuracy'], label='Точность на обучающих данных')
plt.plot(history.history['val_accuracy'], label='Точность на проверочных данных')
plt.xlabel('Эпоха')
plt.ylabel('Точность')
plt.legend()
plt.show()
```

### 3. Регрессия с использованием Boston Housing Dataset и Scikit-learn

В этом примере мы используем Boston Housing Dataset для построения модели линейной регрессии.  Этот набор данных доступен непосредственно из Scikit-learn.

```python
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Загрузка данных
boston = load_boston()
X, y = boston.data, boston.target

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Прогнозирование на тестовых данных
y_pred = model.predict(X_test)

# Оценка модели (среднеквадратичная ошибка)
mse = mean_squared_error(y_test, y_pred)
print(f"Среднеквадратичная ошибка: {mse:.2f}")

# Визуализация результатов (сравнение фактических и предсказанных значений)
plt.scatter(y_test, y_pred)
plt.xlabel("Фактические значения")
plt.ylabel("Предсказанные значения")
plt.title("Фактические vs. Предсказанные цены на жилье")
plt.show()
```

### 4. Кластеризация с использованием Iris Dataset и K-means

Этот пример демонстрирует кластеризацию данных Iris Dataset с помощью алгоритма K-means.

```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Загрузка данных
iris = load_iris()
X = iris.data

# Создание и обучение модели K-means (3 кластера, так как в Iris Dataset 3 вида ирисов)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Получение меток кластеров для каждой точки данных
labels = kmeans.labels_

# Визуализация кластеров (используем первые два признака для простоты визуализации)
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('Кластеризация Iris Dataset с использованием K-means')
plt.show()
```

### 5. Использование TensorFlow Datasets

TensorFlow Datasets предоставляет множество готовых к использованию наборов данных, упрощая процесс загрузки и подготовки данных для TensorFlow.

```python
import tensorflow_datasets as tfds
import tensorflow as tf

# Загрузка набора данных cats_vs_dogs
(ds_train, ds_validation), ds_info = tfds.load(
    'cats_vs_dogs',
    split=['train[:80%]', 'train[80%:]'],
    as_supervised=True,
    with_info=True
)

# Функция для изменения размера изображений
def resize_image(image, label):
    image = tf.image.resize(image, (150, 150))
    return image, label

# Применение функции изменения размера к данным
ds_train = ds_train.map(resize_image)
ds_validation = ds_validation.map(resize_image)

# Настройка параметров пакетной обработки и кэширования
batch_size = 32
ds_train = ds_train.batch(batch_size).prefetch(buffer_size=tf.data.AUTOTUNE)
ds_validation = ds_validation.batch(batch_size).prefetch(buffer_size=tf.data.AUTOTUNE)

# Пример отображения нескольких изображений из набора данных
def show_batch(image_batch, label_batch):
    plt.figure(figsize=(10,10))
    for n in range(25):
        ax = plt.subplot(5,5,n+1)
        plt.imshow(image_batch[n].numpy().astype("uint8"))
        plt.title(ds_info.features['label'].int2str(label_batch[n].numpy()))
        plt.axis("off")
    plt.show()

for image_batch, label_batch in ds_train.take(1):
    show_batch(image_batch, label_batch)
```

---

## Расширенные возможности

### 1. Магические команды (работают и в Colab)

*   `%timeit`: Измерение времени выполнения кода.
*   `!ls`: Выполнение команд shell.
*   `%%writefile my_script.py`:  Сохранение содержимого ячейки в файл.

```python
%%timeit
import numpy as np
np.random.randn(1000, 1000)
```

### 2. Интерактивные виджеты

```python
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

def plot_sine(frequency=1.0):
  """Отображает график синусоиды с заданной частотой."""
  x = np.linspace(0, 2 * np.pi, 400)
  y = np.sin(frequency * x)
  plt.figure(figsize=(8, 4))
  plt.plot(x, y)
  plt.xlabel("x")
  plt.ylabel("sin(x)")
  plt.title(f"Синусоида с частотой {frequency}")
  plt.grid(True)
  plt.show()

interact(plot_sine, frequency=(0.1, 5.0, 0.1));
```

### 3. Использование GPU в Colab

Colab предоставляет бесплатный доступ к GPU!  Чтобы включить GPU, выберите Runtime -> Change runtime type -> Hardware accelerator -> GPU.

```python
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Простой пример использования GPU
with tf.device('/GPU:0'):
  a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
  b = tf.constant([7.0, 8.0, 9.0, 10.0, 11.0, 12.0], shape=[3, 2], name='b')
  c = tf.matmul(a, b)

print(c)
```

### 4. TensorBoard в Colab

TensorBoard - это мощный инструмент для визуализации обучения моделей TensorFlow.

```python
# %load_ext tensorboard # Раскомментируйте, если используете Colab

import tensorflow as tf
import datetime

# Определение callback для TensorBoard
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# Загрузка данных MNIST (пример для обучения)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Определение модели
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Обучение модели с использованием callback TensorBoard
model.fit(x=x_train, y=y_train, epochs=5, validation_data=(x_test, y_test), callbacks=[tensorboard_callback])

# %tensorboard --logdir logs/fit # Раскомментируйте, чтобы запустить TensorBoard в Colab
```

