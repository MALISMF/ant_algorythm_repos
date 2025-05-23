# Ant Colony Algorithm

Этот проект реализует алгоритм муравьиной колонии для поиска кратчайшего пути в графе (например, для задачи коммивояжёра).

## Структура проекта

- `ant_alg.py` — основной файл, реализующий алгоритм муравьиной колонии и демонстрацию его работы на небольшом графе.
- `graph.py` — класс для представления графа, его вершин и рёбер.
- `edge.py` — класс для рёбер графа, с поддержкой феромонов и привлекательности.
- `route.py` — класс для маршрута (пути), используемого муравьями.

## Описание

Алгоритм имитирует поведение муравьёв, которые ищут кратчайший путь между городами, оставляя феромоны на рёбрах графа. С течением времени феромоны испаряются, а наиболее короткие маршруты получают больше феромонов, что увеличивает вероятность их выбора в будущем.

### Основные параметры алгоритма:
- **num_ants** — количество муравьёв
- **num_cities** — количество городов (вершин)
- **num_iterations** — количество итераций
- **alpha** — влияние феромонов
- **beta** — влияние привлекательности (обратной длины)
- **rho** — коэффициент испарения феромонов
- **q** — количество феромонов, добавляемых на рёбра

## Как использовать

1. Установите зависимости (если используются, например, `matplotlib`, `numpy`).
2. Запустите `ant_alg.py`:
   ```bash
   python ant_alg.py
   ```
3. В консоли появится информация о кратчайшем найденном маршруте.

## Пример графа

В проекте уже задан пример графа с вершинами `a`, `b`, `c`, `d`, `f`, `g` и рёбрами между ними.

## Зависимости

- Python 3.x
- matplotlib
- numpy

Установить зависимости можно командой:
```bash
pip install matplotlib numpy
```

