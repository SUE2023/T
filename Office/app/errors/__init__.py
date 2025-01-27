#!/usr/bin/env python3
"""Initialization of the Module"""
from flask import Blueprint

bp = Blueprint("errors", __name__)

from app.errors import handlers
