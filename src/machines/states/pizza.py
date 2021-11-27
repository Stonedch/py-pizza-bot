import enum


class PizzaStates(enum.Enum):
    starting = 'Вы хотите купить пиццу?'
    size_options = 'Какую вы хотите пиццу? Большую или маленькую?'
    payment_options = 'Как вы будете платить?'
    confirmation = 'confirmation'
    thanks = 'Спасибо за заказ!'
