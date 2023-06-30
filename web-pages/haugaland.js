import { getData } from "./main.js";

getData( "https://www.infokanal.com/haugaland_rss.xml")

setInterval(() => {
    getData( "https://www.infokanal.com/haugaland_rss.xml")
}, 300000);
