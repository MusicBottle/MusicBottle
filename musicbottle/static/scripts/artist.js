function onImageError(url_str, image) {
    "use strict";
    image.onerror = "";
    image.src = url_str+"/missing.png";
    return true;
}
