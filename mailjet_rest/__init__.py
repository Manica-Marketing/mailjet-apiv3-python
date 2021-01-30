#!/usr/bin/env python
# coding=utf-8
from module_mailjet.mailjet_rest.client import MailjetClient
from module_mailjet.mailjet_rest.utils.version import get_version

__version__ = get_version()

__all__ = (MailjetClient, get_version)