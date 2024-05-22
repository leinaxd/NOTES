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
