from transitions import Machine, State

from .buttons import PizzaButtons
from .states import PizzaStates
from .transitions import PizzaTransitions


class PizzaMachine(Machine):
    def __init__(self):
        self.message = ''
        self.size = ''
        self.payment = ''

        Machine.__init__(
            self,
            states=PizzaStates,
            transitions=PizzaTransitions.transitions,
            initial='starting',
            after_state_change='set_message',
            ignore_invalid_triggers=True,
            auto_transitions=False,
        )

        self.set_message()

    def set_message(self, message=None):
        if self.state == PizzaStates.confirmation:
            self.message = f'Вы хотите {self.size.lower()} пиццу, оплата - {self.payment.lower()}?'
            return
        self.message = PizzaStates(self.state).value

    def set_small_size(self):
        self.size = PizzaButtons.small.value

    def set_big_size(self):
        self.size = PizzaButtons.big.value

    def set_card_payment(self):
        self.payment = PizzaButtons.card.value

    def set_cash_payment(self):
        self.payment = PizzaButtons.cash.value
