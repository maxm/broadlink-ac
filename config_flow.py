from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_MAC
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import ConfigEntryError
from homeassistant.helpers.device_registry import format_mac

from .const import DOMAIN


class BroadlinkACConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Broadlink AC."""

    VERSION = 1

    async def async_step_user(self, user_input: dict | None = None) -> FlowResult:
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            host = user_input.get(CONF_HOST)
            mac = user_input.get(CONF_MAC)

            # Validate MAC address format
            try:
                formatted_mac = format_mac(mac)
            except ValueError:
                errors[CONF_MAC] = "invalid_mac"

            # Validate host (basic validation for example purposes)
            if not host or not isinstance(host, str):
                errors[CONF_HOST] = "invalid_host"

            if not errors:
                # Check for duplicates
                await self.async_set_unique_id(formatted_mac)
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=f"Broadlink AC ({host})",
                    data={CONF_HOST: host, CONF_MAC: formatted_mac},
                )

        # Show the form
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_HOST): str,
                    vol.Required(CONF_MAC): str,
                }
            ),
            errors=errors,
        )
