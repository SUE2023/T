#!/usr/bin/env python3
""" Utility routes"""
from flask import Blueprint, request, jsonify
from app.utils import bp


@bp.route('/csp-violations', methods=['POST'])
def csp_violations():
    csp_report = request.get_json()
    if csp_report:
        print("CSP Violation Report:", csp_report)
    return jsonify({"status": "received"}), 200
