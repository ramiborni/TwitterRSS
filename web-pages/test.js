import { getData } from "./main.js";

getData( "https://www.infokanal.com/test_rss.xml")

setInterval(() => {
    getData( "https://www.infokanal.com/test_rss.xml")
}, 300000);
