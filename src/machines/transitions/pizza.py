from machines.buttons import PizzaButtons
from machines.states import PizzaStates

class PizzaTransitions:
        transitions = [
            {
                'trigger': PizzaButtons.yes.value,
                'source': PizzaStates.starting.name,
                'dest': PizzaStates.size_options.name,
            },
            {
                'trigger': PizzaButtons.small.value,
                'source': PizzaStates.size_options.name,
                'dest': PizzaStates.payment_options.name,
                'after': ['set_small_size']
            },
            {
                'trigger': PizzaButtons.big.value,
                'source': PizzaStates.size_options.name,
                'dest': PizzaStates.payment_options.name,
                'after': ['set_big_size'],
            },
            {
                'trigger': PizzaButtons.card.value,
                'source': PizzaStates.payment_options.name,
                'dest': PizzaStates.confirmation.name,
                'after': ['set_card_payment'],
            },
            {
                'trigger': PizzaButtons.cash.value,
                'source': PizzaStates.payment_options.name,
                'dest': PizzaStates.confirmation.name,
                'after': ['set_cash_payment']
            },

            {
                'trigger': PizzaButtons.yes.value,
                'source': PizzaStates.confirmation.name,
                'dest': PizzaStates.thanks.name,
            },
            {
                'trigger': PizzaButtons.no.value,
                'source': PizzaStates.confirmation.name,
                'dest': PizzaStates.size_options.name,
            },
            {
                'trigger': PizzaButtons.cancel.value,
                'source': '*',
                'dest': PizzaStates.starting.name,
            },
        ]
