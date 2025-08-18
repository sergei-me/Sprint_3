import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

# 1. Напиши геттеры
    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items

# 2. Добавь товар в чек 
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        
        self.__name_items.append(name)
        self.__number_items += 1

# 3. Удали товар из чека
    def delete_item_from_check(self, name):
        if name not in self.name_items:
            raise NameError('Позиция отсутствует в чеке')
        
        self.__name_items.remove(name)
        self.__number_items -= 1

# 4. Посчитай общую стоимость товаров
    def check_amount(self):
        total = []
        filtered_items = filter(lambda item: item in self.__item_price, self.name_items)
        for item in filtered_items:
            total.append(self.__item_price[item])
        # if len(total) > 10:
        #     return sum(total) * 0.9
        # else:
        #     return sum(total)
        multiplier = 1.0
        if len(total) > 10:
            multiplier = 0.9
        
        return sum(total) * multiplier


# 5. Вычисли НДС для товаров со ставкой 20%
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        filtered_items = filter(lambda item: self.__tax_rate[item] == 20, self.name_items)
        for item in filtered_items:
            if self.number_items > 10:
                total.append(self.__item_price[item] * 0,9)
            else:
                total.append(self.__item_price[item])
        twenty_percent_tax = map(lambda item: item * 0.2, total)
        return sum(twenty_percent_tax)

# 6. Вычисли НДС для товаров со ставкой 10%
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        filtered_items = filter(lambda item: self.__tax_rate[item] == 10, self.name_items)
        for item in filtered_items:
            if self.number_items > 10:
                total.append(self.__item_price[item] * 0,9)
            else:
                total.append(self.__item_price[item])
        ten_percent_tax = map(lambda item: item * 0.1, total)
        return sum(ten_percent_tax)

# 7. Посчитай общую сумму налогов
    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

# 8. Верни номер телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
     
        if len(str(telephone_number)) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')

        return f'+7{telephone_number}'

# Дополнительное задание
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [
            ['часы: ', lambda now: now.hour],
            ['минуты: ', lambda now: now.minute],
            ['день: ', lambda now: now.day],
            ['месяц: ', lambda now: now.month],
            ['год: ', lambda now: now.year]
            ]
        for i, func in date:
            date_and_time.append(f'{i}{func(now)}')
        return date_and_time

# receipt = OnlineSalesRegisterCollector()
# receipt.add_item_to_cheque('кола')
# receipt.add_item_to_cheque('чипсы')
# receipt.add_item_to_cheque('молоко')
# print(receipt.name_items)
# # receipt.delete_item_from_check('кола2')
# # print(receipt.name_items)
# receipt.check_amount
# print(receipt.twenty_percent_tax_calculation())
# print(receipt.total_tax())
# print(receipt.get_telephone_number(1234567890))
# print(receipt.get_date_and_time())