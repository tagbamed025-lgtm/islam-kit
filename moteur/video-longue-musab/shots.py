import json
g = json.load(open('align.json'))
def t(i): return g[i][0]
def mid(a,b): return (a+b)/2

S = []
def photo(img, s, e, kb='zoomin'):
    S.append({'type':'photo','img':img,'start':s,'end':e,'kb':kb})
def motion(name, s, e):
    S.append({'type':'motion','name':name,'start':s,'end':e})

# minute 1 -------------------------------------------------
photo('M18_mount_uhud', t(0)[0], t(0)[1], 'zoomout')
photo('M01_bedouin_cloak', t(1)[0], t(1)[1], 'zoomin')
photo('M01_bedouin_cloak', t(2)[0], t(2)[1], 'pan-r')
photo('M01_bedouin_cloak', t(3)[0], t(3)[1], 'pan-l')
photo('M05_elegant_walker', t(4)[0], t(4)[1], 'zoomin')
photo('M02_mecca_dusk', t(5)[0], t(5)[1], 'zoomout')
photo('M03_noble_silk', t(6)[0], t(6)[1], 'zoomin')
m = mid(*t(7))
photo('M03_noble_silk', t(7)[0], m, 'pan-r')
photo('M04_perfume_incense', m, t(7)[1], 'zoomin')
photo('M04_perfume_incense', t(8)[0], t(8)[1], 'pan-l')
photo('M05_elegant_walker', t(9)[0], t(9)[1], 'zoomout')
photo('M06_oil_lamp_house', t(10)[0], t(10)[1], 'zoomin')
photo('M06_oil_lamp_house', t(11)[0], t(11)[1], 'pan-r')
photo('M06_oil_lamp_house', t(12)[0], t(12)[1], 'zoomin')
m = mid(*t(13))
photo('M06_oil_lamp_house', t(13)[0], m, 'zoomout')
photo('M07_bolted_door', m, t(13)[1], 'zoomin')

# minute 2 -------------------------------------------------
photo('M07_bolted_door', t(14)[0], t(14)[1], 'pan-l')
photo('M07_bolted_door', t(15)[0], t(15)[1], 'zoomin')
photo('M07_bolted_door', t(16)[0], t(16)[1], 'pan-r')
photo('M08_patched_garment', t(17)[0], t(17)[1], 'zoomin')
photo('M09_red_sea_boat', t(18)[0], t(18)[1], 'zoomout')
photo('M08_patched_garment', t(19)[0], t(19)[1], 'pan-l')
photo('M08_patched_garment', t(20)[0], t(20)[1], 'zoomin')
photo('M10_desert_road_walker', t(21)[0], t(21)[1], 'pan-r')
photo('M11_lush_oasis', t(22)[0], t(22)[1], 'zoomout')
photo('M11_lush_oasis', t(23)[0], t(23)[1], 'zoomin')
photo('M12_two_travelers', t(24)[0], t(24)[1], 'pan-r')
photo('M15_clan_chief_spear', t(25)[0], t(25)[1], 'zoomin')
photo('M16_seated_listener', t(26)[0], t(26)[1], 'pan-l')
photo('M16_seated_listener', t(27)[0], t(27)[1], 'zoomin')
photo('M14_spear_sand', t(28)[0], t(28)[1], 'zoomout')
photo('M13_rugs_teaching', t(29)[0], t(29)[1], 'zoomin')

# minute 3 -------------------------------------------------
photo('M17_tribal_gathering', t(30)[0], t(30)[1], 'pan-r')
photo('M17_tribal_gathering', t(31)[0], t(31)[1], 'zoomin')
photo('M11_lush_oasis', t(32)[0], t(32)[1], 'zoomout')
photo('M13_rugs_teaching', t(33)[0], t(33)[1], 'zoomin')
motion('title_card', t(34)[0], t(34)[1])
motion('banner_handoff', t(35)[0], t(35)[1])
motion('troops_clash', t(36)[0], t(36)[1])
motion('banner_falls', t(37)[0], t(37)[1])
photo('M20_fallen_banner', t(38)[0], t(38)[1], 'zoomin')
m = mid(*t(39))
photo('M20_fallen_banner', t(39)[0], m, 'zoomout')
photo('M01_bedouin_cloak', m, t(39)[1], 'pan-r')
photo('M21_dry_grass', t(40)[0], t(40)[1], 'zoomin')
photo('M24_graves_uhud', t(41)[0], t(41)[1], 'zoomout')

# minute 4 -------------------------------------------------
photo('M23_abundant_meal', t(42)[0], t(42)[1], 'zoomin')
photo('M23_abundant_meal', t(43)[0], t(43)[1], 'pan-l')
photo('M22_modest_meal', t(44)[0], t(44)[1], 'zoomin')
photo('M22_modest_meal', t(45)[0], t(45)[1], 'pan-r')
photo('M23_abundant_meal', t(46)[0], t(46)[1], 'zoomout')
photo('M22_modest_meal', t(47)[0], t(47)[1], 'zoomin')
photo('M24_graves_uhud', t(48)[0], t(48)[1], 'pan-l')
photo('M25_fiery_horizon', t(49)[0], t(49)[1], 'zoomin')
photo('M26_golden_rays', t(50)[0], t(50)[1], 'zoomout')

json.dump(S, open('shots.json','w'), ensure_ascii=False, indent=1)
print(len(S), 'shots, last end', S[-1]['end'])
