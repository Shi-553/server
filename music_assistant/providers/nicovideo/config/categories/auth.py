"""Authentication configuration category for Nicovideo provider."""

from __future__ import annotations

from music_assistant.providers.nicovideo.config.categories.base import ConfigCategoryBase
from music_assistant.providers.nicovideo.config.factory import ConfigFactory


class AuthConfigCategory(ConfigCategoryBase):
    """Authentication settings category."""

    _auth = ConfigFactory("Authentication")

    user_session = _auth.secure_str_or_none_config(
        key="user_session",
        label="User Session ( 'user_session' in Cookie)",
        description="Enter the user_session cookie value.",
    )

    def save_user_session(self, value: str) -> None:
        """Save user session to the setup data."""
        self.provider._update_setup_data("user_session", value)
