from lesson2Cus import Customer, CreditCardPayment, CryptoPayment, OrderManager

buyer = Customer(name:='Алексей', initial_balance:=5000)
visa_card = CreditCardPayment('4276550011223344')

OrderManager.checkout(buyer, card_sum=4000, payment_method=visa_card)

crypto_wallet = CryptoPayment("0x51C...3a9")
OrderManager.checkout(buyer, card_sum=1500, payment_method=crypto_wallet)