import logging 

# Import rich

from rich.console import Console
from rich.theme import Theme
from rich.traceback import install
from rich.logging import RichHandler


install()

global console
console = Console(record=True)
custom_theme = Theme({"1": "red"})
console = Console(theme=custom_theme)

logging.basicConfig(
  level="INFO",
  format="%(message)s",
  datefmt="[%X]",
  handlers=[RichHandler(rich_tracebacks=True)
  )

global log

log = logging.getLogger("rich")
