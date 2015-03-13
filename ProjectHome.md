PyMapia is distributed under MIT License

PyMapia is a client written by Davide Carboni <dcarboni@gmail.com> to access Wikimapia services

PyMapia is not affiliated nor endorsed in any way by Wikimapia

PyMapia is released AS IS, no warranties see MIT License for details.

PyMapia is not endorsed by my current employer CRS4 neither by other organizations I have been affiliated in the past.

---

## low level API mapped on function box ##

```
def box(west,south,east,north,
        options=None,
        disable=None,
        page=1,
        count=50,
        language=None,
        category=None):
```

## high level API to load all places with multiple HTTP get(s) if necessary until max\_results ##

```
def places(west,south,east,north,options=None,disable=None,language=None,category=None,max_results=1000):
```

## low level API mapped to function object ##
```
def wobject(placeid):
```
