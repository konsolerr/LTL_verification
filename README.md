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

## Пример запуска программы и работы на автомате из примера

```
$ cat tests/ltl_formulas/test1.ltl 
G (hal_init -> (X tim4_enable))
G (pin_reset_s1 -> (X pin_reset_s2))
G (pin_reset_s2 -> (X pin_reset_s3))
G (hal_init -> (F tim4_enable))
G (F prestart)
G (sleep -> (F power_on))

$ ./verification.py tests/automata/test1.xml tests/ltl_formulas/test1.ltl 
Formula "G ((hal_init) -> (X (tim4_enable)))" is valid
---
Formula "G ((pin_reset_s1) -> (X (pin_reset_s2)))" is valid
---
Formula "G ((pin_reset_s2) -> (X (pin_reset_s3)))" is valid
---
Formula "G ((hal_init) -> (F (tim4_enable)))" is valid
---
Formula "G (F (prestart))" is invalid, here goes the counter example :
Start:
	start
	start tick
	hal_init start tick
	start tick tim4_enable
	prestart
	prestart tick
	prestart shell_deinit tick
	bq_deinit prestart tick
	pin_reset_s1 prestart tick
	pin_reset_s2 prestart tick
	pin_reset_s3 prestart tick
	delay_5000 prestart tick
	power_on
	chg power_on
	cpu_on
	chg cpu_on
	bat_only
	bat_only chg
	cpu_on;
Cycle:
	chg cpu_on
	bat_only
	bat_only chg
	cpu_on;
---
Formula "G ((sleep) -> (F (power_on)))" is valid
---
```
