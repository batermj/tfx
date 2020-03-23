# Lint as: python2, python3
# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for tfx.types.annotations."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Standard Imports

import tensorflow as tf

from tfx.types import annotations
from tfx.types import artifact
from tfx.types import standard_artifacts


class AnnotationsTest(tf.test.TestCase):

  def testArtifactGenericAnnotation(self):
    # pylint: disable=pointless-statement
    # Error: type hint whose parameter is not an Artifact subclass.
    with self.assertRaisesRegexp(ValueError,
                                 'expects .* a concrete subclass of'):
      annotations._ArtifactGeneric[int]

    # Error: type hint with abstract Artifact subclass.
    with self.assertRaisesRegexp(ValueError,
                                 'expects .* a concrete subclass of'):
      annotations._ArtifactGeneric[artifact.Artifact]

    # Error: type hint with abstract Artifact subclass.
    with self.assertRaisesRegexp(ValueError,
                                 'expects .* a concrete subclass of'):
      annotations._ArtifactGeneric[artifact.ValueArtifact]

    # OK.
    annotations._ArtifactGeneric[standard_artifacts.Examples]
    # pylint: enable=pointless-statement


if __name__ == '__main__':
  tf.test.main()