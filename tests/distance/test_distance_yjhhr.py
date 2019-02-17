# -*- coding: utf-8 -*-

# Copyright 2019 by Christopher C. Little.
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

"""abydos.tests.distance.test_distance_yjhhr.

This module contains unit tests for abydos.distance.YJHHR
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import YJHHR


class YJHHRTestCases(unittest.TestCase):
    """Test YJHHR functions.

    abydos.distance.YJHHR
    """

    cmp = YJHHR()

    def test_yjhhr_dist(self):
        """Test abydos.distance.YJHHR.dist."""
        # Base cases
        self.assertEqual(self.cmp.dist('', ''), 0.0)
        self.assertEqual(self.cmp.dist('a', ''), 0.0)
        self.assertEqual(self.cmp.dist('', 'a'), 0.0)
        self.assertEqual(self.cmp.dist('abc', ''), 1.0)
        self.assertEqual(self.cmp.dist('', 'abc'), 1.0)
        self.assertEqual(self.cmp.dist('abc', 'abc'), 0.0)
        self.assertEqual(self.cmp.dist('abcd', 'efgh'), 1.0)

        self.assertAlmostEqual(self.cmp.dist('Nigel', 'Niall'), 0.6666666667)
        self.assertAlmostEqual(self.cmp.dist('Niall', 'Nigel'), 0.6666666667)
        self.assertAlmostEqual(self.cmp.dist('Colin', 'Coiln'), 0.6666666667)
        self.assertAlmostEqual(self.cmp.dist('Coiln', 'Colin'), 0.6666666667)
        self.assertAlmostEqual(self.cmp.dist('ATCAACGAGT', 'AACGATTAG'), 0.5)

    def test_yjhhr_dist_abs(self):
        """Test abydos.distance.YJHHR.dist_abs."""
        # Base cases
        self.assertEqual(self.cmp.dist_abs('', ''), 0.0)
        self.assertEqual(self.cmp.dist_abs('a', ''), 0.0)
        self.assertEqual(self.cmp.dist_abs('', 'a'), 0.0)
        self.assertEqual(self.cmp.dist_abs('abc', ''), 4.0)
        self.assertEqual(self.cmp.dist_abs('', 'abc'), 4.0)
        self.assertEqual(self.cmp.dist_abs('abc', 'abc'), 0.0)
        self.assertEqual(self.cmp.dist_abs('abcd', 'efgh'), 10.0)

        self.assertAlmostEqual(self.cmp.dist_abs('Nigel', 'Niall'), 6.0)
        self.assertAlmostEqual(self.cmp.dist_abs('Niall', 'Nigel'), 6.0)
        self.assertAlmostEqual(self.cmp.dist_abs('Colin', 'Coiln'), 6.0)
        self.assertAlmostEqual(self.cmp.dist_abs('Coiln', 'Colin'), 6.0)
        self.assertAlmostEqual(
            self.cmp.dist_abs('ATCAACGAGT', 'AACGATTAG'), 7.0
        )


if __name__ == '__main__':
    unittest.main()
