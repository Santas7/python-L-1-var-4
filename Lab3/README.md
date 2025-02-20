# Прикладное программирование

## Лабораторная № 3. Сериализация данных

Задание:  
Реализовать консольное приложение, которое будет производить обработку валидных данных из второй лабораторной работы.

Задачи:
1.	Реализовать алгоритм сортировки согласно выданному варианту.**Использование готовой сортировки из библиотек запрещено! Реализация должна быть своя.**
2.	Произвести сортировку отвалидированных записей по полю, тип данных которого - числовой (int, float). Если полей такого типа встречается несколько, должна быть предусмотрена возможность выбора поля. 
3.	Отсортированный набор экземпляров сериализовать в файл с использованием указанного для варианта модуля. Также провести десериализацию из файла и продемонстрировать корректное конвертирование. После десериализации полученные данные должны представлять из себя набор экземпляров класса.
4.	Реализованное консольное приложение и консольное приложение, разработанное при выполнении второй лабораторной работы - объединить в пакет.

__Модули сериализации__: pickle, yaml, json.  
__Алгоритмы сортировки__: Пузырьковая, сортировка выборкой, сортировка вставками, быстрая сортировка, сортировка Шелла, пирамидальная сортировка, сортировка слиянием, сортировка по сегментам.

Потенциально полезные ремарки:
* Можно дополнить код 2й лабораторной необходимыми методами/функциями.
* Рекомендуется освежить в голове теорию всех предложенных алгоритмов сортировки, а также понятие "вычислительная сложность". 
* Если согласно вашему варианту у вас сериализация в yaml, будьте морально готовы долго ждать сериализации. 
* Допускается сериализовать в yaml не все валидные данные, а их подвыборку, но при одном условии - вы погуглили, почему сериализация в yaml такая медленная, и способны внятно объяснить это своими словами.


Варианты заданий:

|№|ФИО|Сериализация|Сортировка|
|--|--|--|--|
|1|Барышников Владислав Сергеевич|pickle|Пузырьковая|
|2|Вольгов Даниил Иванович|yaml|Выборкой|
|3|Елагин Денис Евгеньевич|json|Вставками|
|4|Жидяев Дмитрий Владиславович|pickle|Быстрая|
|5|Коваленко Владимир Владимирович|yaml|Шелла|
|6|Ле Лок Тхо|json|Пирамидальная|
|7|Ле Хань Хоанг|pickle|Слиянием|
|8|Леонтьев Сергей Алексеевич|yaml|Сегментами|
|9|Люкшина Дарья Евгеньевна|json|Пузырьковая|
|10|Маликов Родион Александрович|pickle|Выборкой|
|11|Митерев Дмитрий Александрович|yaml|Вставками|
|12|Можгаев Степан Геннадьевич|json|Быстрая|
|13|Надеждина Виктория Михайловна|pickle|Шелла|
|14|Ненашев Дмитрий Михайлович|yaml|Пирамидальная|
|15|Памурзин Вадим Михайлович|json|Слиянием|
|16|Панюшкин Андрей Михайлович|pickle|Сегментами|
|17|Рогалев Владислав Викторович|yaml|Пузырьковая|
|18|Сахарова Дарья Владимировна|json|Выборкой|
|19|Томашайтис Павел Андреевич|pickle|Вставками|
|20|Федотов Богдан Юрьевич|yaml|Быстрая|
|21|Чегодаев Максим Андреевич|json|Шелла|

