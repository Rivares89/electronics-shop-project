from src.keyboard import Keyboard
from src.item import Item


def test_Keyboard():
    kb = Keyboard("White", 9000, 10)
    assert kb.name == "White"
    assert kb.price == 9000
    assert kb.quantity == 10
    assert kb.language == "EN"
    assert str(kb) == "White"

    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
