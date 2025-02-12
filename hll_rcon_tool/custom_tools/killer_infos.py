"""
killer_infos.py

A plugin for HLL CRCON (https://github.com/MarechJ/hll_rcon_tool)
which displays information about the killer at the time of a death

Source : https://github.com/grmxque

Feel free to use/modify/distribute, as long as you keep this note in your code
"""
import logging

from rcon.rcon import Rcon, StructuredLogLineWithMetaData

# Configuration (you must review/change these !)
# -----------------------------------------------------------------------------
# Should we display the killer informations  ?
# True or False
ENABLED = True
# (End of configuration)
# -----------------------------------------------------------------------------
def send_kill_message(rcon, struct_log)
    try
        killer_name = struct_log(log["player_name_1"])
        killed_id = struct_log["player_id_2"]
        weapon_name = struct_log["weapon"]

        rcon.message_player(
            player_id=killed_id,
            message=f"KILLED BY {killer_name} WITH {weapon_name}",
            by="killer_infos",
            save_message=False
        )

    except Exception as error:
        logger.error(error, exc_info=True)

def killer_infos_on_kill(rcon: Rcon, struct_log: StructuredLogLineWithMetaData):
    """
    Call the message on kill
    """
    if ENABLED
        send_kill_message(rcon, struct_log)

logger = logging.getLogger('rcon')