from pathlib import Path
from prompt_toolkit import prompt
import sys
import time


def read_file(file: Path | str):
    """
    The function `read_file` reads a file line by line and yields each line as a string.

    :param file: The `file` parameter in the `read_file` function can accept either a `Path` object or a
    string representing the file path
    :type file: Path | str
    """
    with open(file, "r") as f:
        for line in f:
            yield line


def write_to_file(file: Path | str, list: list[str]):
    """
    The function writes a list of strings to a file, with each string on a new line.

    :param file: The `file` parameter in the `write_to_file` function is the path to the file where you
    want to write the list of strings. It can be either a `Path` object or a string representing the
    file path
    :type file: Path | str
    :param list: The `list` parameter in the `write_to_file` function is a list of strings that you want
    to write to the specified file. Each string in the list will be written to the file on a new line
    :type list: list[str]
    """

    with open(file, "w") as f:
        for val in list:
            f.write(f"{val}\n")


def interminal_text_editor(label: str, text: str) -> str:
    """
    Opens an editable terminal prompt with the text already pre-filled.

    :param label: The initial text label to show before the text to edit
    :param text: What i want to edit
    :return: The edited text as a string
    """
    return prompt(
        label, default=text
    )  # Use prompt_toolkit to pre-fill the input with the existing task


def type_writer_effect(text: str, delay=0.005):
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


def project_path(file: str, *relative_parts: str) -> Path:
    """
    Construct a project-relative path from the calling module's location.

    This function resolves a path relative to the project root directory, which is
    determined by searching upward from the given file for the nearest parent
    directory containing a 'src' folder. If no 'src' folder is found, the file's
    parent directory is used as the project root.

    Parameters
    ----------
    file : str
        The __file__ attribute of the calling module. Must be a valid file path
        that exists on the filesystem. It must always be the calling module's __file__ attribute.
    *relative_parts : str
        Variable number of path components to append to the project root.

    Returns
    -------
    Path
        A pathlib.Path object pointing to the constructed project-relative path.
        Parent directories are created if they don't exist.

    Raises
    ------
    TypeError
        If file is empty or None.
    ValueError
        If file is not an existing file on the filesystem.

    Examples
    --------
    >>> from pathlib import Path
    >>> p = project_path(__file__, "config", "settings.json")
    >>> isinstance(p, Path)
    True
    """

    if not file:
        raise TypeError(
            "project_path() requires the first argument '__file__' of the calling module"
        )

    # Normalize to Path
    file_path = Path(file)

    # Ensure the file exists
    if not file_path.is_file():
        raise ValueError(f"The first argument must be __file__, got '{file}'")

    # Start from the file's directory
    p = file_path.resolve()

    # Search upward for the nearest folder containing 'src'
    for parent in [p] + list(p.parents):
        if (parent / "src").is_dir():
            root = parent
            break
    else:
        root = p.parent

    path = root.joinpath(*relative_parts)

    # Ensure parent directories exist
    path.parent.mkdir(parents=True, exist_ok=True)

    return path


if __name__ == "__main__":
    ...
