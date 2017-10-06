app-postbox
    form(method="POST",action="/api/v1/posts")
        textarea(name="text",content="投稿内容")
        input(type="submit",value="投稿")