"""Short description of what this program does"""
from hsltimes import parser

__program__: str = "hsltimes"
__author__: str = ""
__copyright__: str = ""
__credits__: list = ["Niklas Larsson", "Ben Panyanil"]
__license__: str = ""
__version__: str = "0.0.1b0"
__maintainer__: str = ""
__email__: str = ""
__status__: str = ""


def main() -> None:
    """Main function."""
    x = parser.Parser()
    x.generate_all()


if __name__ == "__main__":
    main()
