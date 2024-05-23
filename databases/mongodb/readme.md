# MongoDB

### INSTALATION
Instalation on KDE neon
```
sudo pkcon install mongodb-org
sudo pkcon install mongodb-org-shell #?is this required?
sudo systemctl start mongod
sudo systemctl enable mongod # optionally start mongo after system reboot
# DO RESTART COMPUTER
sudo systemctl status mongod # Verify all ok
```

You can start the shell now
```
mongosh
mongoc
mongo
```
try something
```
use MyDatabase #creates a new database
db.newCollection.insert({name:'John', age:30}) #creates a new collection with one entry
db.newCollection.find() #show all entries in newCollection
db.newCollection.update(
  {name:'John'},
  {$set:{age:31}}
  )
db.newCollection.remove({ name: "John" })
exit #exit the shell
sudo journalctl -u mongod #logs and errors
```
## DATASETS
Get any dataset
!(https://github.com/ozlerhakan/mongodb-json-files/tree/master/datasets)

Include those files in the server
```
#bash
~$mongoimport <path>
```

Show databases/collections
```
mongo
show dbs
show tables
```
Show content
```
db.collection.find()
db['collection'].find()
```
Filter
```
db['collection'].find({name:'abc'})
```
Project
```
db['collection'].find({name:'abc'},{attribute_1=1, 'attribute.subatt'=0}) #1: includes, 0:excludes from projection
```
Sort
```
db['collection'].find({name:'abc'}).sort(area:1) #1: ASC, -1:DESC
```
OPERATORS
```
$in: [1,2,3] #seaches if value matches the list
$lte: 40 #matches if value is less than equal 40
$regex: '/^regex/i' #matches any regex.
  modifiers i: any upper/lower case
$size: 5 #matches if length of something is 5
```
### EJ FIUBA
ej. 4
```
db['countries-small'].find({capital:'Vienna'}) #a
db['countries-small'].find({area:{$lte:20}}) #b
db['countries-small'].find({area:{$lte:20}}, {'name.common':1,area:1}).sort({area:1}) #b+
db['countries-small'].find({region:'Americas', area:{$lte:100}},{name:1,area:1}).sort({area:1}) #c
db['countries-small'].find({borders:'FRA'},{'name.common':1}) #d
db['countries-small'].find({borders:{$in:['FRA','POL]}},{'name.common':1}) #e
db['countries-small'].find({'name.official':{$regex:'Republic'}, borders:{$size:3}},{'name.official':1,borders:1}) #f
```
