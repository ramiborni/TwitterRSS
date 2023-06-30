import { getData } from "./main.js";

getData( "https://www.infokanal.com/{category_name}_rss.xml")

setInterval(() => {
    getData( "https://www.infokanal.com/{category_name}_rss.xml")
}, 300000);
