from typing import TypedDict


class Request(TypedDict):
    """An HTTP request."""

    uri: str
    """
    URI. Does not include the host name or protocol.

    Example:

        .. code-block:: text

            /foo/bar.html
    """
