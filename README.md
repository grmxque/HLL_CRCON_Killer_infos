# HLL_CRCON_Killer_infos

A plugin for Hell Let Loose (HLL) CRCON (see : https://github.com/MarechJ/hll_rcon_tool)  
that displays killer informations on death

## Install

> [!NOTE]
> The shell commands given below assume your CRCON is installed in `/root/hll_rcon_tool`.  
> You may have installed your CRCON in a different folder.
>
> Some Ubuntu Linux distributions disable the `root` user and `/root` folder by default.  
> In these, your default user is `ubuntu`, using the `/home/ubuntu` folder.  
> You should then find your CRCON in `/home/ubuntu/hll_rcon_tool`.
>
> If so, you'll have to adapt the commands below accordingly.

- Log into your CRCON host machine using SSH and enter these commands (one line at at time) :

  First part  
  If you already have installed any other "custom tools" from ElGuillermo, you can skip this part.  
  (though it's always a good idea to redownload the files, as they could have been updated)
  ```shell
  cd /root/hll_rcon_tool
  wget https://raw.githubusercontent.com/ElGuillermo/HLL_CRCON_restart/refs/heads/main/restart.sh
  mkdir custom_tools
  ```

  Second part
  ```shell
  wget https://raw.githubusercontent.com/grmxque/HLL_CRCON_Killer_infos/refs/heads/main/hll_rcon_tool/custom_tools/killer_infos.py -O /root/hll_rcon_tool/custom_tools/killer_infos.py
  ```

- Edit `/root/hll_rcon_tool/rcon/hooks.py`
    - (update rcon.logs.loop import as follow) 
      ```python
      from rcon.logs.loop import (
          on_camera,
          on_chat,
          on_connected,
          on_disconnected,
          on_match_end,
          on_match_start,
          on_kill,
      )
      ```
    - (add this line in the import part, on top of the file)
      ```python
      import custom_tools.killer_infos as killer_infos
      ```
    - (add these lines at the very end of the file)
      ```python
      @on_kill
      def killerinfos_on_kill(rcon: Rcon, struct_log: StructuredLogLineWithMetaData):
          killer_infos.killer_infos_on_kill(rcon, struct_log)
      ```

## Config
- Edit `/root/hll_rcon_tool/custom_tools/killer_infos.py` and set the parameters to fit your needs.
- Restart CRCON :
  ```shell
  cd /root/hll_rcon_tool
  sh ./restart.sh
  ```

## Limitations
⚠️ Any change to these files requires a CRCON rebuild and restart (using the `restart.sh` script) to be taken in account :
- `/root/hll_rcon_tool/custom_tools/killer_infos.py`
- `/root/hll_rcon_tool/rcon/hooks.py`

⚠️ This plugin requires a modification of the `/root/hll_rcon_tool/rcon/hooks.py` file, which originates from the official CRCON depot.  
If any CRCON upgrade implies updating this file, the usual upgrade procedure, as given in official CRCON instructions, will **FAIL**.  
To successfully upgrade your CRCON, you'll have to revert the changes back, then reinstall this plugin.  
- To revert to the original file :
  ```shell
  cd /root/hll_rcon_tool
  git restore rcon/hooks.py
  ```