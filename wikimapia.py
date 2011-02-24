"""
PyMapia is distributed under MIT License

PyMapia is a client written by Davide Carboni <dcarboni@gmail.com> to access Wikimapia services

PyMapia is not affiliated nor endorsed in any way by Wikimapia

PyMapia is released AS IS, no warranties see MIT License for details.

PyMapia is not endorsed by my current employer CRS4 neither by other organizations I have been affiliated in the past. 

"""


import json
import urllib





#write your API key here
key=None

box_url="""http://api.wikimapia.org/?function=box&key=%s&bbox=%f,%f,%f,%f"""
object_url="""http://api.wikimapia.org/?function=object&key=%s&id=%s&format=json"""

if key==None: raise Exception("API Key is None")

def box(west,south,east,north,
        options=None,
        disable=None,
        page=1,
        count=50,
        language=None,
        category=None):
        
  """low level API mapped on function box"""

  params="&format=json"+("&options="+options if options else "") + ("&disable="+disable if disable else "") + ("&page="+str(page) if page else "") +("&count="+str(count) if count else "") +("&language="+language if language else "") + ("&category="+category if category else "")
        
  query=box_url + params
  
  print "query",query%(key,west,south,east,north)
  c=urllib.urlopen(query%(key,west,south,east,north))
  data=c.read()
  rslt=json.loads(data)
  
  
  
  return rslt
  


def places(west,south,east,north,options=None,disable=None,language=None,category=None,max_results=1000):
  """
  high level API to load all places with multiple HTTP get(s) if necessary until max_results
  """
  rslt=box(west,south,east,north,options,disable=disable,language=language,category=category)
  found=rslt['found']
  print 'found',found
  elements=rslt['folder']
  
  for page in range(2,min(1+found/50, max_results/50)):
    rslt=box(west,south,east,north,options=options,disable=disable,language=language,category=category,page=page)
    elements.extend(rslt['folder'])
 
  print 'elements',len(elements)
  return elements[:max_results]


def wobject(pid):
  """
  low level API mapped to function object
  """
  q = object_url%(key,str(pid))
  print 'q',q
  c=urllib.urlopen(q)
  data=c.read()
  return json.loads(data)
   
  
  
  




 
