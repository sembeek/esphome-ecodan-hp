import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor
from esphome.const import CONF_ID
from esphome.const import (
    ENTITY_CATEGORY_NONE
)

from . import ECODAN, CONF_ECODAN_ID


AUTO_LOAD = ["ecodan"]

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_ECODAN_ID): cv.use_id(ECODAN),
        cv.Optional("controller_version_text"): text_sensor.text_sensor_schema(
            icon="mdi:new-box",
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional("heat_source_text"): text_sensor.text_sensor_schema(
            icon="mdi:fire",
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional("status_dhw"): text_sensor.text_sensor_schema(
            icon="mdi:water-boiler",
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional("status_heating_cooling"): text_sensor.text_sensor_schema(
            icon="mdi:thermostat",
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional("status_power"): text_sensor.text_sensor_schema(
            icon="mdi:power",
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional("status_operation"): text_sensor.text_sensor_schema(
            icon="mdi:power",
            entity_category=ENTITY_CATEGORY_NONE,
        ),

    }).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    hp = await cg.get_variable(config[CONF_ECODAN_ID])

    for key, conf in config.items():
        if not isinstance(conf, dict):
            continue
        id = conf.get("id")
        if id and id.type == text_sensor.TextSensor:
            sens = await text_sensor.new_text_sensor(conf)
            cg.add(hp.register_textSensor(sens, key))
