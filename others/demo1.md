```python
import requests,pprint


params = {'action':'list_course', 'pagenum':'1', 'pagesize':20 }
response = requests.get("http://localhost/api/mgr/sq_mgr/",params=params)

retListBefore = response.json()['retlist']



payload  = {
    'action':'add_course',
    'data':'{"name":"python语言","desc":"python语言基础和提升","display_idx":"2"}'
}

response = requests.post("http://localhost/api/mgr/sq_mgr/",data=payload)


retDict = response.json()
pprint.pprint(retDict)
assert retDict['retcode'] == 0



params = {'action':'list_course', 'pagenum':'1', 'pagesize':20 }
response = requests.get("http://localhost/api/mgr/sq_mgr/",params=params)

retDict = response.json()
pprint.pprint(retDict)
retListAfter = response.json()['retlist']

newcourse = None
for one in retListAfter:
    if one not in retListBefore:
        newcourse = one
        break

assert newcourse!=None
assert newcourse['name']=='python语言'
assert newcourse['desc']=='python语言基础和提升'
assert newcourse['display_idx']==2

print('test case pass')
```
