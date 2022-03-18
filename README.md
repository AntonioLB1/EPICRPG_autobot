# Automatize EPIC-RPG discord's bot 

## Automatize farm
Download:
- EPIC_RPG_autobot.exe
- params_AutobotRPG.json

Both in the same folder. The _.json_ must have this structure:
```json
{
    "hunt": {
        "do": true,
        "heal": false,
        "frequency_hunt_per_heal": 4,
        "buy_lifepotion": false,
        "lifepotion_per_buy": 10,
        "time_per_hunt": 61
    },
    "chop": {
        "do": true,
        "what": "axe"
    },
    "farm": {
        "do": true,
        "buy_seed": true,
        "what": "potato"
    },
    "adventure": {
        "do": true,
        "heal_before": true,
        "heal_after": true,
        "try_frecuency": 60,
        "trys_until_heal_before": 0
    }
}
```
Explaining each section:
- Hunt: for _rpg hunt_
  - "do": _true_ if you want to farm it, _false_ if don't.
  - "heal": _true_ if you want to heal after hunt, _false_ if don't.
  - "frequency_hunt_per_heal": if "heal" is _true_, how many hunts between each heal.
  - "buy_lifepotion": _true_ if you want to buy life potions, _false_ if don't.
  - "lifepotion_per_buy": if "buy_lifepotion" is _true_, how many life potions uses between buy.
  - "time_per_hunt": time in seconds between hunts
     - Standar is 60s (61s recommended), in Anniversary is 40s 
- Chop: for _rpg chop/fish/axe/net/pickup/..."_
  - "do": _true_ if you want to farm it, _false_ if don't.
  - "what": what do you farm, see this: https://epic-rpg.fandom.com/wiki/Working_Commands
- Farm: for _rpg farm [normal/potato/carrot/bread]"_
  - "do": _true_ if you want to farm it, _false_ if don't.
  - "buy_seed": _true_ if you want to buy normal seed before farm, _false_ if don't.
  - "what": if "buy_seed" is false, you can farm no-standart seed. See https://epic-rpg.fandom.com/wiki/Farming
- adventure: _rpg adventure_
  - "do": _true_ if you want to farm it, _false_ if don't.
  - "heal_before": _true_ if you want to heal before adventure, _false_ if don't.
  - "heal_after": _true_ if you want to heal after adventure, _false_ if don't.
  - "heal_after": _true_ if you want to heal after adventure, _false_ if don't.
  - "try_frecuency": minutes beetwen trys, each "minute" is given by "time_per_hunt". 
  - "trys_until_heal_before": trys between "heal_before".
If you dont want to do someone of this four commands, open the file and write _false_ in the corresponding "do".

