import sys
import time


def _twe(text: str, delay=0.005):
    """
    Display text with a typewriter effect by printing characters one at a time.

    Args:
        text (str): The text to display with the typewriter effect.
        delay (float, optional): The delay in seconds between each character. Defaults to 0.005.

    Returns:
        None
    """

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
