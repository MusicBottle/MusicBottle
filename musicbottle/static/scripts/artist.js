function onImageError(url_str, image) {
    "use strict";
    image.onerror = "";
    image.src = url_str+"missing.png";
    return true;
}

function getWikiText(wiki_str,wiki_site) {
    "use strict";
    var wp = document.getElementById("wp-summary");
    console.log(wiki_str)
    wiki_str = wiki_str.replace(/href="\/wiki\//g,"href=\""+wiki_site+"wiki/");
    wiki_str = wiki_str.replace(/<sup[^]+\/sup>/g,"");
    console.log(wiki_str)

    wp.innerHTML = wiki_str;
}
