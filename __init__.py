import sys, os, json

if len(sys.argv)<2:
    exit('please specify input file')
else:
    filepath=sys.argv[1]
if not os.path.isfile(filepath):
    exit('file does not exist')    
if not filepath.endswith('.json'):
    exit('not a proper theme file')
def proper_line(s):
    while s[0] in ['\t',' ']:
      s=s[1:]
    if len(s)<2:
      return True
    else:
      return not '/' in s
f=open(filepath)
text=f.readlines()
lines=[]
for i in text:
   if proper_line(i):
       lines.append(i)
data=''
for i in lines:
  data=data+i
data=eval(data)

colors=data['colors']
tokenColors=data['tokenColors']

print('=================================')
print(colors)
print('=================================')
print(tokenColors)

res_ui={}
res_syntax={}



sames={
       "editor.background"                 : "EdTextBg",
       #"editor.foreground"                 : "EdTextFont",
       "tab.inactiveBackground"            : "TabPassive",
       "tab.activeBackground"              : "TabBg",
       "sideBar.background"                : "SideBg",
       "statusBar.background"              : "StatusBg",
       #"statusBar.foreground"              : "StatusFont",
       "editor.selectionBackground"        : "EdSelBg",
       "tab.border"                        : "TabBorderActive",
       "editorLink.activeForeground"       : "EdLinks",
       "editorCursor.foreground"           : "EdCaret",
       "editorMarkerNavigation.background" : "EdMarkers",
       "activityBar.background"            : "StatusBg",
       #"activityBarBadge.foreground"       : "StatusFont",
      }

def hex_to_dec(hexwas):
  intset=0
  for i in hexwas:
    intset=intset*16
    if i in '0123456789':
      intset=intset+int(i)
    elif i=='A':
      intset=intset+10
    elif i=='B':
      intset=intset+11
    elif i=='C':
      intset=intset+12
    elif i=='D':
      intset=intset+13
    elif i=='E':
      intset=intset+14
    elif i=='F':
      intset=intset+15
  return intset

def dec_to_hex(int_was):
  hex_set=''
  def int_to_hex_num(iwas):
    if iwas<10:
      return str(i)
    elif iwas==10:
      return 'A'
    elif iwas==10:
      return 'B'
    elif iwas==10:
      return 'C'
    elif iwas==10:
      return 'D'
    elif iwas==10:
      return 'E
    return 'F'
  while int_was > 0:
    hex_set=int_to_hex_num(int_was % 16)+hex_set
    int_was = int_was // 16
  return hex_set
    

def inv(color):
  color=color[1:]
  hex_nums=[
        color[:2],
        color[2:4],
        color[4:]
       ]
  int_nums=[]
  for i in hex_nums:
    int_nums.append(hex_to_dec(i))
  new_int_nums=[]
  for i in int_nums:
    if i>128:
      new_int_nums.append(i-126)
    else:
      new_int_nums.append(i+126)
  res='#'
  for i in new_int_nums:
    if len(dec_to_hex(i))<2:
      res=res+'0'+dec_to_hex(i)
    else:
      res=res+dec_to_hex(i)

for i in sames:
  if i in colors:
    res_ui[sames[i]]=colors[i]

if not 'EdTextBg' in res_ui:
  exit('Not enoygh data to make a theme')

if 'EdTextBg' in res_ui:
  res_ui['EdTextFont']=inv(res_ui['EdTextBg'])
  
if not 'TreeViewBg' in res_ui:
  res_ui['TreeViewBg']=res_ui['EdTextBg']
    
print(res_ui)

json.dump(res_ui,open('res.cuda-theme-ui.json','w'))

editor_bg=colors['editor.background']
#print (bg)