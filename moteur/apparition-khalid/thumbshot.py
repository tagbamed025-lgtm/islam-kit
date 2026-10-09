from playwright.sync_api import sync_playwright
import sys
with sync_playwright() as p:
  b=p.chromium.launch(args=['--allow-file-access-from-files'])
  for f,w,h,o in [('v',1080,1920,'Miniature_Khalid_1080x1920.png'),('h',1280,720,'Miniature_Khalid_1280x720.png')]:
    pg=b.new_page(viewport={'width':w,'height':h})
    pg.goto(f'file:///home/claude/khalid/thumb.html?f={f}');pg.wait_for_timeout(800)
    pg.screenshot(path=o,clip={'x':0,'y':0,'width':w,'height':h})
  b.close()
