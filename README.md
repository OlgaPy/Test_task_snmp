# SNMP_TestTask
 Задача: 
	
1 - записать данные о коммутаторе и его портах (имя, скорость, статус) в БД

Порты должны быть

а) только физические

б) включены

2 - Написать SQL запрос который выведет порты со скоростью более 100 Mb

Дано:

Коммутатор DES-1210-10 (ссылка)

IP адрес: 10.10.100.1

Community: public

Версия SNMP: 2с

результат выполнения snmpwalk IfName

IF-MIB::ifName.1 = STRING: 1/1

IF-MIB::ifName.2 = STRING: 1/2

IF-MIB::ifName.3 = STRING: 1/3

IF-MIB::ifName.4 = STRING: 1/4

IF-MIB::ifName.5 = STRING: 1/5

IF-MIB::ifName.6 = STRING: 1/6

IF-MIB::ifName.7 = STRING: 1/7

IF-MIB::ifName.8 = STRING: 1/8

IF-MIB::ifName.9 = STRING: 1/9

IF-MIB::ifName.10 = STRING: 1/10

IF-MIB::ifName.1024 = STRING: 802.1Q Encapsulation Tag 0001

IF-MIB::ifName.1506 = STRING: 802.1Q Encapsulation Tag 0483

IF-MIB::ifName.2022 = STRING: 802.1Q Encapsulation Tag 0999

IF-MIB::ifName.2023 = STRING: 802.1Q Encapsulation Tag 1000

IF-MIB::ifName.2314 = STRING: 802.1Q Encapsulation Tag 1291

IF-MIB::ifName.2506 = STRING: 802.1Q Encapsulation Tag 1483

IF-MIB::ifName.5121 = STRING: System

Для получения названий использовать ifName

Для получения скорости использовать ifSpeed

Для определения включен/выключен порт – ifOperStatus

Для определения физический/логический порт использовать регулярное выражение

Название(ifName) должно выглядеть как “1/число” например 1/2, 1/3 и т.д.

Скрипт написать на языке Perl/Python

Для взаимодействия с оборудованием использовать библиотеку Net::SNMP (для Perl)

Результат записать в БД

