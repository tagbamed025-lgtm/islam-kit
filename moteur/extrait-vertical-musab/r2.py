from reel import build
cfg={'dir':'r2','end':3.2,'sub':2.6,'tag':"MUS'AB IBN UMAYR · <b>YATHRIB</b>",
 'src':'Ibn Hishâm, <span style="color:var(--gold)">as-Sîra an-Nabawiyya</span>',
 'lines':[(25,0.3),(26,0.2),(27,0.6),(28,0.6),(29,0.9),(32,0.3),(33,0)],
 'shots':lambda c:[
  (0,'M15_clan_chief_spear',[.36,.5,1.0,.38,.45,1.15],{'shake':c['wt'](25,'furieux'),'dust':.6}),
  (c['wt'](25,'Il')-.15,'M15_clan_chief_spear',[.42,.3,1.45,.44,.35,1.55]),
  (c['ls'](26)-.15,'M13_rugs_teaching',[.45,.6,1.0,.45,.55,1.15],{'dust':.6}),
  (c['ls'](27)-.15,'M15_clan_chief_spear',[.4,.45,1.3,.4,.42,1.45]),
  (c['ls'](28)-.15,'M14_spear_sand',[.5,.45,1.25,.5,.5,1.0],{'shake':c['ls'](28)+.35,'dust':.8}),
  (c['wt'](28,'et')-.1,'M16_seated_listener',[.4,.5,1.0,.4,.5,1.12]),
  (c['ls'](29)-.15,'M16_seated_listener',[.38,.4,1.25,.38,.38,1.4],{'bloom':[.4,.25,c['ls'](29)+1.0]}),
  (c['ls'](32)-.15,'M11_lush_oasis',[.5,.55,1.2,.5,.5,1.0],{'dust':.5,'sweep':c['ls'](32)+.8}),
  (c['ls'](33)-.15,'M13_rugs_teaching',[.45,.5,1.1,.45,.5,1.3],{'bloom':[.45,.35,c['wt'](33,'cœurs')],'dust':.7}),
 ]}
build(cfg)
