from unittest import TestCase
from rich_simple_term_menu import TerminalMenu
from rich.console import Console

class TestTerminalMenu(TestCase):
    def test_show(self):
        console = Console()
        options = ["[bold gold1]entry 1", "entry 2", "entry 3"]
        terminal_menu = TerminalMenu(options, print_entry_fn=lambda x: console.print(x, end=''))
        # terminal_menu = TerminalMenu(options, print_entry_fn=lambda x: print(x, end=''))
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")


if __name__ == '__main__':
    t = TestTerminalMenu()
    t.test_show()
