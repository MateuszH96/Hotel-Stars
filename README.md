# Wytyczne
1. Każda klasa ma osobny plik
2. Funkcje/Metody są rodzielone 2 znakami końca linii
3. Nazewnictwo
    - posługujemy się językiem angielski
    - stosujemy notację wielbłądzią do nazewnictwa obiektów, zmienych, funckji np. thisIsNameOfObject, thisIsNameOfVariable, thisIsNameOfFunction
    - nazwy klas zapisujemy od wielkiej litery np. class Player
    - nazwy stałych zapisujemy wielkimi literami oddzielonymi znakiem '_' np. NAME_OF_CONST_VALUE
4. Unikamy przypisywania wartości np. liczbowych w głównym pliku, dla konkretnego modułu będzie osobny plik ze stałymi

ModuleConst.py
```
INITIAL_COST_VALUE = 50000
```
```
ModuleMain.py
costRoom = INITIAL_COST_VALUE
```
5. Do tworzenia dokumentacji używamy [Sphinx](https://pythonhosted.org/an_example_pypi_project/sphinx.html)

```
def sumOfValues(a,c,d):
    """This Function returns sum of 3 numbers

    Args:
        a (int): This is a 'a' value responsible for...
        c (int): This is a 'c' value responsible for...
        d (int): This is a 'd' value responsible for...

    Returns:
        int: sum of input values
    """
    return a+c+d
```