# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

from bs4 import BeautifulSoup


def sanitize(text, default="No description available"):
    """
    Removes all html tags but includes the href links inside the text. If no text is given then it will return
    the default value "No description currently available"

    Example: sanitize("<p>This is a paragraph with a
    link <a href=\"https://docs.docker.com/engine/reference/run/\">docker run</a></p>")
    :param text: a String that my contain html tags
    :param default: the value given if there is no description. Customizable message for the user
    :return: the text without html tags
    """

    if text is not None:
        anchor_tag_removal = text.replace("<a href=\"", "").replace("\">", " ")
        return BeautifulSoup(anchor_tag_removal, 'lxml').get_text()

    return default
