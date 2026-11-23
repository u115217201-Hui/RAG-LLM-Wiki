from pathlib import Path
from html.parser import HTMLParser
import re,sys
P=Path(__file__).resolve().parents[1]
class CheckHTML(HTMLParser):
 def __init__(self):
  super().__init__();self.sections=0;self.ids=set();self.refs=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=='section' and 'slide' in d.get('class','').split():self.sections+=1
  if 'id' in d:self.ids.add(d['id'])
  for k in ['href','src']:
   if k in d and not d[k].startswith(('https://','http://','#','mailto:')):self.refs.append(d[k])
errors=[]
raw=list((P/'raw').glob('S*.md'))
if len(raw)<5:errors.append('少於五份來源卡')
for f in raw:
 if 'https://' not in f.read_text(encoding='utf-8'):errors.append(f'{f.name}: 缺來源網址')
for key in ['wiki/index.md','wiki/log.md','AGENTS.md','index.html','workflow.html','assets/style.css','assets/slides.js']:
 if not (P/key).exists():errors.append('缺失 '+key)
concepts=list((P/'wiki/concepts').glob('*.md'))
if len(concepts)<5:errors.append('概念頁不足')
for h in ['index.html','workflow.html']:
 parser=CheckHTML();parser.feed((P/h).read_text(encoding='utf-8'))
 for ref in parser.refs:
  if not (P/ref).exists():errors.append(f'{h}: 失效內部路徑 {ref}')
 if h=='index.html':
  if parser.sections!=10:errors.append(f'投影片數量 {parser.sections} != 10')
  for required in ['prev','next','counter','progress']:
   if required not in parser.ids:errors.append('缺 id '+required)
print('五份來源卡：',len(raw), ' | Wiki 概念頁：',len(concepts), ' | 投影片：', 10)
print('PASS' if not errors else 'FAIL: '+ '; '.join(errors))
sys.exit(bool(errors))
