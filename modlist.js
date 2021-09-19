const curseforge = require("mc-curseforge-api");
const fs = require('fs');
/*
curseforge.getMods({ index: 1000, pageSize: 60 }).then((mods) => {
    //console.log(mods);
    const modsd = JSON.stringify(mods,null, 2);
 */
curseforge.getMods({ gameVersion: "1.12.2" }).then((mods) => {
    console.log(mods);
    
    const modsd = JSON.stringify(mods,null, 2);
    fs.writeFile('modinfos.json', modsd, (err) => {
        if (err) {
            throw err;
        }

        console.log("JSON data is saved.");
    });
    
}); 


