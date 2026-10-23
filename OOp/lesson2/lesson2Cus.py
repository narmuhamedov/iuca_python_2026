from abc import ABC, abstractmethod

class PaymetGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float)->bool:
        pass

class CreditCardPayment(PaymetGateway):
    def __init__(self, card_number):
        self.__card_number = card_number

    def process_payment(self, amount: float)->bool:
        print(f'|Банк| Запрос к шлюзу Visa/Mastercard...')
        print(f'|Банк| Списание {amount}сом с карты ****{self.__card_number[-4:]}')
        return True

class CryptoPayment(PaymetGateway):
    def __init__(self, wallet_address:str):
        self.wallet_address = wallet_address

    def process_payment(self, amount: float)->bool:
        print(f'|Блокчейн| Проверка сети и смарт-контакта...')
        crypto_amount = amount / 100
        print(f'|Блокчейн|Перевод{crypto_amount} USDT на кошельке {self.wallet_address[:6]}....')
        return True

class Customer:
    def __init__(self, name: str, initial_balance: float):
        self.name = name
        self.__balance = initial_balance
        self.__discount = 0.05

    @property
    def balance(self) -> float:
        return self.__balance

    def top_up_balance(self, amount: float):
        if amount <= 0:
            raise ValueError('Сумма должна быть положительной')
        self.__balance += amount
        print(f'Баланс пополнен на {amount} сом')
        print(f'Текущий баланс - {self.__balance} сом')

    def calculate_total(self, amount: float) -> float:
        """Возвращает сумму с учётом скидки клиента."""
        return amount * (1 - self.__discount)

    def calculate_internal_balance(self, amount: float) -> bool:
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        return False


class OrderManager:
    @staticmethod
    def checkout(customer: Customer, card_sum: float, payment_method: PaymetGateway):
        print(f'\n----Оформление заказа для пользователя {customer.name}---')

        filan_price = customer.calculate_total(card_sum)
        print(f'Исходная сумма: {card_sum}сом с учетом скидки {filan_price} сом')

        payment_success = payment_method.process_payment(filan_price)

        if payment_success:
            print('Заказ успешно оплачен!')
        else:
            print('Ошибка оплаты!')
        


