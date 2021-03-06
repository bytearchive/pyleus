"""Package containing pyleus implementation of major Storm entities.
"""
from __future__ import absolute_import

from collections import namedtuple

DEFAULT_STREAM = "default"

StormTuple = namedtuple('StormTuple', "id comp stream task values")
"""Namedtuple representing a Storm tuple.

* **id**\(``str`` or ``long``): tuple identifier
* **comp**\(``str``): name of the emitting component
* **stream**\(``str``): name of the input stream the tuple belongs to
* **values**\(``tuple``): values contained by the tuple
"""


def is_tick(tup):
    """Tell whether the tuple is a tick tuple or not.

    :param tup: tuple to investigate
    :type tup: :class:`~.StormTuple`
    :return: ``True`` if the tuple is a tick tuple, ``False`` otherwise
    :rtype: ``bool``
    """
    # Tick tuples (generated by Storm; introduced 0.8) are defined as being
    # from the __system component and __tick stream.
    return tup.comp == '__system' and tup.stream == '__tick'


class StormWentAwayError(Exception):
    """Raised when the connection between the component and Storm terminates.
    """

    def __init__(self):
        message = "Got EOF while reading from Storm"
        super(StormWentAwayError, self).__init__(message)


from pyleus.storm.bolt import Bolt, SimpleBolt
from pyleus.storm.spout import Spout

_ = [Bolt, SimpleBolt, Spout] # pyflakes
