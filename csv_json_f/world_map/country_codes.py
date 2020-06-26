from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code

    #若未找到，则返回none
    return None