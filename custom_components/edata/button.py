"""Button platform for edata component."""

from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant

from . import const
from .entity import EdataButtonEntity


async def async_setup_entry(hass: HomeAssistant, config_entry, async_add_entities):
    """Set up entry."""
    hass.data.setdefault(const.DOMAIN, {})

    # get configured parameters
    scups = config_entry.data[const.CONF_SCUPS]
    coordinator = hass.data[const.DOMAIN][scups]["coordinator"]
    # add sensor entities
    _entities = []
    _entities.append(
        EdataResetButton(coordinator, "soft_reset", coordinator.async_soft_reset)
    )
    async_add_entities(_entities)

    return True


class EdataResetButton(EdataButtonEntity, ButtonEntity):
    """Representation of an e-data restoration button."""

    _attr_icon = "mdi:restore"
