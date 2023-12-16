import { getData } from "./main.js";

getData( "https://www.infokanal.com/sunnhordland_rss.xml")

setInterval(() => {
    getData( "https://www.infokanal.com/sunnhordland_rss.xml")
}, 300000);
