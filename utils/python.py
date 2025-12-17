from pathlib import Path
from prompt_toolkit import prompt
import sys
import time


# def interminal_text_editor(label: str, text: str) -> str:
#     """
#     Opens an editable terminal prompt with the text already pre-filled.

#     :param label: The initial text label to show before the text to edit
#     :param text: What i want to edit
#     :return: The edited text as a string
#     """
#     return prompt(
#         label, default=text
#     )  # Use prompt_toolkit to pre-fill the input with the existing task


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


def project_path_finder(file: str, *relative_parts: str) -> Path:
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
