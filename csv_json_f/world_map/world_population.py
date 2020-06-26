import json
from country_codes import get_country_code
import pygal
import pygal_maps_world.maps as pymap
from pygal.style import RotateStyle

#加载数据
f_name='population_data.json'
with open(f_name) as f:
    pop_data=json.load(f)

#创建一个包含人口数量的字典
cc_populations={}
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country=pop_dict['Country Name']
        population=int(float(pop_dict['Value']))          #'{:,}'.format(int(pop_dict['Value']))    # pop_dict['Value']
        code=get_country_code(country)
        if code:
            cc_populations[code]=population

#根据人口数量将所有的国家分成三组
cc_pops_1,cc_pops_2,cc_pops_3={},{},{}
for cc,pop in cc_populations.items():
    if pop<10000000:
        cc_pops_1[cc]=pop
    elif pop<1000000000:
        cc_pops_2[cc]=pop
    else:
        cc_pops_3[cc]=pop


wm_style=RotateStyle('#336699')  #改变地图颜色
wm=pymap.World(style=wm_style)
wm.title = 'World Population in 2010,by Country'
wm.add('0-10M',cc_pops_1)
wm.add('10M-1Bn',cc_pops_2)
wm.add('>1Bn',cc_pops_3)
wm.render_to_file('world_population.svg')




# #打印每个国家2010年的人口数量
# for pop_dict in pop_data:
#     if pop_dict['Year']=='2010':
#         country=pop_dict['Country Name']
#         population=int(float(pop_dict['Value']))          #'{:,}'.format(int(pop_dict['Value']))    # pop_dict['Value']
#         code=get_country_code(country)
#         if code:
#             print(code + ': ' + str(population))
#         else:
#             print('ERROR - ' + country)


