# test_task_04_12_2024
Mushrooms/Baskets TASK

Здравствуйте!
Небольшое описание работы моего API.

1. Гриб не может существовать вне корзины - когда созадем гриб, сразу помещаем его в корзину.
2. Каждый гриб (строка таблицы грибы) - "уникальный предмет" - Мухомор_1, Мухомор_2 и тд
3. Если гриб удаляется из корзины - строка удаляется из таблицы Грибы.

Все входные данные валидируются либо кастомными схемами, либо стандартными типами данных.
Все выходные данные - кастомными схемами при необходимости.
Для хранения данных используется PostgreSQL.
файл .env загрузил намеренно для демонстрации.