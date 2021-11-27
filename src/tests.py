from machines import PizzaMachine
from machines.states import PizzaStates
from machines.buttons import PizzaButtons

def test_state_machine():
    machine = PizzaMachine()

    assert machine.state == PizzaStates.starting
    assert machine.message == 'Вы хотите купить пиццу?'

    machine.trigger(PizzaButtons.yes.value)

    assert machine.state == PizzaStates.size_options
    assert machine.message == 'Какую вы хотите пиццу? Большую или маленькую?'

    machine.trigger(PizzaButtons.small.value)

    assert machine.state == PizzaStates.payment_options
    assert machine.message == 'Как вы будете платить?'

    machine.trigger(PizzaButtons.card.value)

    assert machine.state == PizzaStates.confirmation
    assert machine.message == 'Вы хотите маленькую пиццу, оплата - картой?'

    machine.trigger(PizzaButtons.yes.value)

    assert machine.state == PizzaStates.thanks
    assert machine.message == 'Спасибо за заказ!'
