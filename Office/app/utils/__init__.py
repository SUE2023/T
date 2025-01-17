#!/usr/bin/env python3
"""Initialization Module """

from flask import Blueprint

bp = Blueprint("utils", __name__)

from app.utils import routes
