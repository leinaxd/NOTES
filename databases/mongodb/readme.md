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
$in: [1,2,3]           #seaches if value matches the list
$lte: 40               #matches if value is less than equal 40
$gte: 400              # matches if values is greather than equal 400
$regex: '/^regex/i'    #matches any regex.
                          # - modifiers i: any upper/lower case
$size: 5               #matches if length of something is 5
$or:[1,2]              # if matches any of inner arguments

$exists                #filter for existence
```
UPDATE OPERATORS
```
$set                   #update to a new value
$inc                   #increment a value certain amount
$addToSet              #updates a new value, only if its new
```
AGGREGATE OPERATORS
```
$match
$group
$unwind               #duplica la información de un arreglo por cada item de el
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
ej. 5
```
db['books'].find({$or:[{title:{$regex:/web/i}}, {longDescription:{$regex:/web/i}}]}, {title:1}).sort({title:1}) #a
db['books'].find({}, {title:1, pageCount:1}).sort({pageCount:-1}).limit(12)    #b
db['books'].find({authors:{$size:1}, pageCount:{$gte:400}}, {title:1,authors:1, pageCount:1}) #c
```
ej. 6
```
db['countries-small'].deleteOne({'name.official':'Falkland Islands'}) #a
db['countries-small'].insertOne({'name':{'official':'Freelandia'}}) #b
db['countries-small'].updateMany({region:'Americas'}, {$set:{region:'America'}}) #region: Americas to America
db['countries-small'].updateMany({'name.official':'Russian Federation'},{$inc:{area:1000}}) #d
db['countries-small'].updateMany({landlocked:true}, {$unset:{area:""}}) #e
```
ej. 7
```
db['countries-small'].find({region:'Africa',area:{$gte:1E6}},{'name.official':1,area:1}).sort({area:-1}) #a
db['countries-small'].updateMany({'name.official':{$regex:/united/i}}, {$set:{'languages.spa':'Spanish'}}) #b
db['countries-small'].aggregate([{$group:{_id:'$region',totalArea:{$sum:'$area'}}}]) #c

db['books'].aggregate([{$unwind:'$authors'},{$project:{_id:0,title:1,author:'$authors'}}]) #d
db['books'].aggregate([{$sort:{pageCount:-1}},{$limit:10},{$sort:{title:1}},{$project:{_id:0,title:1,pageCount:1}}]) #e
db['books'].aggregate([{$unwind:'$categories'},{$group:{_id:'$categories',bookCount:{$sum:1}}}]) #f
```
