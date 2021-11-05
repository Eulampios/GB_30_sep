from math import ceil


class Cell:
    cells_total = 0

    def __init__(self, count: int = 1):
        if count < 1:
            raise ValueError(f"Нужно указать количество клеток больше 0. Указано: {count}")
        if type(count) != int:
            raise TypeError(f"Нужно указать целое количество клеток. Указано: {count}")
        self._count = count
        Cell.cells_total += 1
        self._name = f"№{Cell.cells_total}"

    def __add__(self, cell):
        return Cell(self._count + cell._count)

    def __sub__(self, cell):
        if self._count <= cell._count:
            raise ValueError(f"У вычитаемой клетки меньше ячеек: {self._count} <= {cell._count}")
        return Cell(self._count - cell._count)

    def __mul__(self, cell):
        return Cell(self._count * cell._count)

    def __floordiv__(self, cell):
        return Cell(self._count // cell._count)

    def __truediv__(self, cell):
        return Cell(self._count // cell._count)

    def make_order(self, row_length):
        max_row_length = "*" * row_length
        remain = self._count % row_length
        total_rows = ceil(self._count / row_length)
        return "\n".join([
            max_row_length if (remain != 0) and (i < total_rows) else "*" * (remain)
            for i in range(1, total_rows + 1)
        ])

    def __str__(self):
        return f"Клетка {self._name} имеет ячеек: {self._count}"


cell_list = [
    Cell(59),
    Cell(14),
]

cell_list.append(cell_list[0] + cell_list[1])
cell_list.append(cell_list[0] - cell_list[1])
cell_list.append(cell_list[0] / cell_list[1])
cell_list.append(cell_list[0] // cell_list[1])
cell_list.append(cell_list[0] * cell_list[1])

for cell in cell_list:
    print(cell, "Вывод ячеек по рядам:", cell.make_order(10), "\n", sep='\n')
