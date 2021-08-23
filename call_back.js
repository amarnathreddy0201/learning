const userLeft = false
const userWatchingCatMeme = false

function watchTutorialCallback(callback, errcallback) {
    if (userLeft) {
        errcallback({
            name: "User Left",
            message: ":("
        })
    } else if (userWatchingCatMeme) {
        errcallback({
            name: "user watching Cat Meme",
            message: "webdev simplified <cat"
        })
    } else {
        callback("thumbs up and subscribe")
    }
}