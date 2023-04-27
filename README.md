fork of https://github.com/IngoMeyer441/simple-term-menu but add a new parameter: `print_entry_fn`

This parameter allow you to control how to print each entry.  
example: use `rich` to print text

```python
from rich_simple_term_menu import TerminalMenu
from rich.console import Console

console = Console()

options = ["[bold gold1]entry 1", "entry 2", "entry 3"]

# Add the new `print_entry_fn` to control how to print each entry! 
terminal_menu = TerminalMenu(options, print_entry_fn=lambda x: console.print(x, end=''))

menu_entry_index = terminal_menu.show()
print(f"You have selected {options[menu_entry_index]}!")
```