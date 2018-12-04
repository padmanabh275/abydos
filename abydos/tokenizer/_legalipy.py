# -*- coding: utf-8 -*-

# Copyright 2014-2018 by Christopher C. Little.
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

"""abydos.tokenizer._legalipy.

LegaliPy tokenizer class
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from ._tokenizer import _Tokenizer

try:
    from syllabipy.legalipy import getOnsets, LegaliPy
except ImportError:  # pragma: no cover
    # If the system lacks the SyllabiPy library, that's fine, but SyllabiPy
    # tokenization won't be supported.
    getOnsets = None
    LegaliPy = None


class LegaliPyTokenizer(_Tokenizer):
    """LegaliPy tokenizer.

    .. versionadded:: 0.4.0
    """

    def __init__(self, scaler=None):
        """Initialize Tokenizer.

        Parameters
        ----------
        scaler : None, str, or function
            A scaling function for the Counter:

                None : no scaling
                'set' : All non-zero values are set to 1.
                a callable function : The function is applied to each value
                    in the Counter. Some useful functions include math.exp,
                    math.log1p, math.sqrt, and indexes into interesting integer
                    sequences such as the Fibonacci sequence.

        .. versionadded:: 0.4.0

        """
        if LegaliPy is None:
            raise TypeError(
                'LegaliPy tokenizer requires installation of SyllabiPy'
                + ' package.'
            )

        super(LegaliPyTokenizer, self).__init__(scaler)

        self._onsets = ['']

    def train_onsets(self, text, threshold=0.0002, clean=True, append=False):
        """Train the onsets on a text.

        Parameters
        ----------
        text : str
            The text on which to train
        threshold : float
            Threshold proportion above which to include onset into onset list
        clean : bool
            If True, the text is stripped of numerals and punctuation
        append : bool
            If True, the current onset list is extended

        .. versionadded:: 0.4.0

        """
        new_onsets = getOnsets(text, threshold, clean)
        if append:
            self._onsets = list(set(self._onsets + new_onsets))
        else:
            self._onsets = new_onsets

    def tokenize(self, string, ipa=False):
        """Tokenize the term and store it.

        The tokenized term is stored as an ordered list and as a Counter
        object.

        Parameters
        ----------
        string : str
            The string to tokenize
        ipa : bool
            If True, indicates that the string is in IPA

        .. versionadded:: 0.4.0

        """
        self._string = string
        self._ordered_list = LegaliPy(string, self._onsets)
        super(LegaliPyTokenizer, self).tokenize()
        return self


if __name__ == '__main__':
    import doctest

    doctest.testmod()
