
const fs = require('fs')
var myObj = { "name":"runoob", "alexa":10000, "site":null };

/*
var array = [{"id": "foo", "bar": "jobs"},{"id": "barrrrr","bar": "steve"}];
console.log(array[0].id);
*/



fs.readFile('modinfos.json', 'utf8' , (err, data) => {
    if (err) {
      console.error(err)
      return
    }
    var obj = JSON.parse(data)
    //console.log(obj[0].id);
    for(var i = 0; i < obj.length; i++) {
      console.log(obj[i].id);
      
    }
  })


