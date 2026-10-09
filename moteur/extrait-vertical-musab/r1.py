from reel import build
cfg={'dir':'r1','end':3.2,'sub':2.6,'tag':'COMPAGNONS · <b>EXTRAIT</b>',
 'src':'Sahîh al-Bukhârî · 1276',
 'lines':[(0,0),(1,0),(2,0),(3,0),(4,1.5),(5,1.3),(40,0.4),(41,0.9),(49,0.4),(50,0)],
 'title':lambda c:{'t0':c['ls'](5)-0.1,'th':c['wt'](5,"l'histoire"),'tn':c['wt'](5,"Mus'ab"),'t1':c['PZ'][5]+1.1},
 'suspense':lambda c:[c['PZ'][4],1.5],
 'dips':lambda c:[[c['PZ'][4]-.2,c['PZ'][4]+2.1]],
 'shots':lambda c:[
  (0,'M18_mount_uhud',[.55,.4,1.0,.56,.36,1.12],{'dust':.5}),
  (c['ls'](1)-.2,'M01_bedouin_cloak',[.5,.5,1.0,.5,.48,1.15],{'sweep':c['ls'](1)+1.0}),
  (c['ls'](2)-.15,'M01_bedouin_cloak',[.5,.3,1.35,.5,.25,1.5]),
  (c['ls'](3)-.15,'M01_bedouin_cloak',[.5,.8,1.5,.5,.75,1.35]),
  (c['ls'](4)-.15,'M05_elegant_walker',[.45,.5,1.15,.44,.45,1.0],{'sweep':c['wt'](4,'élégant')-.3,'dust':.6}),
  (c['PZ'][4]+.2,'M02_mecca_dusk',[.62,.6,1.2,.6,.55,1.0],{'dark':.55}),
  (c['ls'](40)-.15,'M01_bedouin_cloak',[.5,.35,1.2,.5,.3,1.35],{'desat':.25}),
  (c['wt'](40,'et',2)-.15,'M21_dry_grass',[.62,.5,1.05,.58,.5,1.2],{'sweep':c['wt'](40,'et',2)+.6}),
  (c['ls'](41)-.15,'M24_graves_uhud',[.45,.6,1.2,.5,.55,1.0],{'dust':.5,'dark':.25}),
  (c['ls'](49)-.15,'M25_fiery_horizon',[.5,.6,1.0,.5,.55,1.15],{'dust':.4}),
  (c['ls'](50)-.15,'M26_golden_rays',[.62,.5,1.2,.6,.45,1.0],{'dust':.8,'bloom':[.62,.3,c['wt'](50,'dure')]}),
 ]}
build(cfg)
