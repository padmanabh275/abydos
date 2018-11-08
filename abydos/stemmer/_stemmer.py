# -*- coding: utf-8 -*-

# Copyright 2018 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.stemmer._stemmer.

The stemmer._stemmer module implements abstract class Stemmer.
"""

from __future__ import unicode_literals


class Stemmer(object):
    """Abstract Stemmer class."""

    def stem(self, word, *args, **kwargs):
        """Return stem.

        Args:
            word (str): The word to stem
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments

        Returns:
            str: Word stem

        """
        pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()
