#!/usr/bin/env python3
"""
    Module for API Autentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class template for managing API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a given path requires authentication.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that do not require authentication.

        Returns:
            bool: False for now, logic will be added later.
        """
        return False
    
    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.

        Args:
            request: The Flask request object.

        Returns:
            str: None for now, logic will be added later.
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
         """
        Retrieves the current user.

        Args:
            request: The Flask request object.

        Returns:
            User: None for now, logic will be added later.
        """
         return None