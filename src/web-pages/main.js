import rssParser from 'https://cdn.jsdelivr.net/npm/rss-parser@3.13.0/+esm'

const testDate = (entryPubDate) => {
    const currentTime = new Date();
    const pubDate = new Date(entryPubDate);
    const timeDifference = currentTime - pubDate;
    const timeDifferenceInMinutes = Math.floor(timeDifference / 60000);
    return timeDifferenceInMinutes <= 30
}

const isHorizontal = () => {
    const currentScript = document.location.href;
    const originHtmlFile = currentScript.substring(currentScript.lastIndexOf('/') + 1, currentScript.length);
    return originHtmlFile.indexOf('horizontal') >= 0
}

const getData = async (url) => {
    var parser = new rssParser({
        customFields: {
            item: ['media:content']
        }
    });
    await parser.parseURL(
        url
        ,
        function (err, result) {
            if (err) throw err;
            document.getElementById('newslist').innerHTML = "";
            result.items.forEach(function (entry) {
                const media = entry['media:content'].$.url
                const title = entry.title.split(':')
                const prefix = `${title[0]}:${title[1]}:`
                title.splice(0, 2)
                const text = title.join(' ');
                const content = `<a class="${(testDate(entry.pubDate) && isHorizontal()) ? "news-item-less-30" : ""}" href="${entry.link}" target="_blank" title="${entry.title}">
                  <img class="news-item-image" src="${media}" alt="${entry.title}"/>
                  <center><b>${prefix}</b> ${text}</center>
                </a>`.trim();
                const listItem = document.createElement('div')
                listItem.className = (testDate(entry.pubDate) && !isHorizontal()) ? "news-item news-item-less-30" : "news-item";
                listItem.innerHTML = content;
                document.getElementById('newslist').append(listItem);
            });
        }
    );
}

export {getData};