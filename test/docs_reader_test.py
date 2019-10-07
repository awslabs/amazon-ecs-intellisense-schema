# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import unittest
from src.sanitizer import *


class TestDocsMethods(unittest.TestCase):

    def test_empty_tag(self):
        description = ""
        expected = ""
        self.assertEqual(sanitize(description), expected)

    def test_none_tag(self):
        description = None
        expected = "No description available"
        self.assertEqual(sanitize(description), expected)

    def test_none_tag_with_default(self):
        description = None
        default = "For tasks using the EC2 launch type, the container instances require at least version 1.26.0 of the container agent and at least version 1.26.0-1 of the ecs-init package to enable a proxy configuration. "
        expected = "For tasks using the EC2 launch type, the container instances require at least version 1.26.0 of the container agent and at least version 1.26.0-1 of the ecs-init package to enable a proxy configuration. "
        self.assertEqual(sanitize(description, default), expected)

    def test_p_tag(self):
        description = "<p><p> </p><p></p>"
        expected = " "
        self.assertEqual(sanitize(description), expected)

    def test_linux_tag(self):
        description = "<p>The container path, mount options, and size (in MiB) of the tmpfs mount. This parameter maps to the <code>--tmpfs</code> option to <a href=\"https://docs.docker.com/engine/reference/run/\">docker run</a>.</p> <note> <p>If you are using tasks that use the Fargate launch type, the <code>tmpfs</code> parameter is not supported.</p> </note>"
        expected = "The container path, mount options, and size (in MiB) of the tmpfs mount. This parameter maps to the --tmpfs option to https://docs.docker.com/engine/reference/run/ docker run.  If you are using tasks that use the Fargate launch type, the tmpfs parameter is not supported. "
        self.assertEqual(sanitize(description), expected)


if __name__ == '__main__':
    unittest.main()

