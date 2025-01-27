#!/usr/bin/python3
"""Module Initialization"""
from flask import Blueprint

bp = Blueprint("main", __name__)

from app.main import bp
