let sendURLbtn = document.getElementById('sendURL') 
let topaxURL = document.getElementById('topaxURL')

let container = document.getElementById('posts')

let allPosts = []

let offset = 10 // Nombre de topics affichés MAX 

let ListeningToThread = undefined 

let displayPosts = function (posts) {

    let html = ""

    for (let i = 0; i < posts.length; i++) {
        html += "<div class='post'><div class='header'><img class='avatar' src='" + posts[i][0] + "'></img><div class='pseudo'>" + posts[i][1] + "</div><div class='date'>" + posts[i][2] + "</div></div><div class='content'>"+ posts[i][3] +"</div></div>"
    }

    container.innerHTML = html

}

sendURLbtn.onclick = () => {

    if (!topaxURL.value.includes('https://www.jeuxvideo.com/forums/')) {
        alert('Le lien est incorrect !')
    } else {
        if (ListeningToThread != undefined) {
            window.clearInterval(ListeningToThread)
        }

        ajax.get('/watchTopic/', {url : topaxURL.value}, (data) => {
            let newURL = JSON.parse(data).response
    
            ListeningToThread = window.setInterval(() => {
                ajax.get('/getLastPosts/', {url : newURL}, (data) => {
                    let posts = JSON.parse(data).posts 
    
                    if (posts.length > 0) {
                        for (let i = 0; i < posts.length; i++) {
                            allPosts.unshift(posts[i])
                        }
                        console.log(allPosts)
    
                        if (allPosts.length > offset) {
                            allPosts = allPosts.slice(0, offset)
                        }
                        displayPosts(allPosts)
                    }
                    
                })
            }, 5000)
        })
    }
}