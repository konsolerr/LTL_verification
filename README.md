# Верификация автомата с помощью формул LTL-формул

## Установка
Процесс установки прост:
```
$ git clone git@github.com:konsolerr/LTL_verification.git
$ cd LTL_verification
$ ./verification.py --help
```

Возможно потребуется установка библиотек из файла requiremenets.txt
```
pip3 install -r requiremenets.txt
```

## Работа программы

Запускаемый файл verification.py принимает два аргумента: путь до файла с xml-автоматом, и путь до файла, 
который содержит формулы LTL-логики.

В папке tests находятся описания двух автоматов, и набор формул для каждого из них.

1. Первый автомат представляет собой 4 вершины, соединенные по кругу: start -> A -> B -> C. При событии GO автомат переходит в следующее состояние. Из вершин B и C существует переход по событию SKIP, который позволяет перепрыгнуть через одну вершину (соответственно в start и A). Из вершины A есть переход по событию BACK в вершину C. Выходных воздействий автомат не содержит.
2. Второй автомат -- автомат из примера https://docs.google.com/document/d/1nUaRnyy4cL5SgwDCfFBZLZiXETVISTsDWTk6-gUnEsk/edit

## Формат файла LTL-формул

Формат простой: каждая строка файла -- отдельная формула, которая должна быть проверена. Формулы поддерживают следующие операции: "&&", "||", "->", "!", "X", "F", "G", "U", "R", идентификаторы пропозициональных переменных должны быть в lowercase. Все именя состояний, событий и выходный воздействий начального автомата приводятся в lowercase.

## Пример работы и запуска

```
$ ./verification.py tests/automata/test0.xml tests/ltl_formulas/test0.ltl 
Formula "F (c)" is invalid, here goes the counter example :
Start:
;
Cycle:
	start
	go start
	a
	a go
	b
	b skip;
---
Formula "G (((a) && (go)) -> (X (b)))" is valid
---
Formula "F (start)" is valid
---
Formula "F (a)" is invalid, here goes the counter example :
Start:
;
Cycle:
	start
	back start
	c
	c go;
---
Formula "F (b)" is invalid, here goes the counter example :
Start:
;
Cycle:
	start
	back start
	c
	c go;
---
Formula "G ((a) -> (F (b)))" is valid
---
Formula "a" has not temporal operator from (U, F, G, R). 
So nothing to verify really
---
Formula "G (F (c))" is invalid, here goes the counter example :
Start:
	start
	go start
	a
	a go
	b
	b skip
	start;
Cycle:
	go start
	a
	a go
	b
	b skip
	start;
---
```
