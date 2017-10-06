const riot = require("riot")

require("./tags/app-timeline.tag")
require("./tags/app-postbox.tag")

addEventListener("load", function(){
    riot.mount("*")
})