app-timeline
    div(each="{post in posts}")
        div {post.text}
    script.
        fetch("/api/v1/posts").then(r => r.json()).then(r => {
            this.posts = r
            this.update()
        })