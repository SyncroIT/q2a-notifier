import requests, re, html, time
WEBSITE = "https://q2a.di.uniroma1.it/questions/fondamenti-di-programmazione-22-23"
last_parse_time: int = None
last_post_id: int = None

def get_website_content() -> str:
    request = requests.get(WEBSITE)
    return str(request.content)

def get_first_post(content:str) -> str:
    return re.search(r'<div class=\"qa-q-item-main\">((\\n)?)<div class=\"qa-q-item-title\">(.*?)<\/div>((\\n)?)<\/div>', content, re.DOTALL).group()

def get_post_id(post_content:str) -> int:
    return int(re.search(r'<div class=\"qa-q-item-title\">(\\n?)<a href=\"..\/(\d*)\/', post_content, re.DOTALL).group(2))

def get_post_title(post_content:str) -> str: 
    return re.search(r'<span title=\"(.*?)\">(.+?)</span>', post_content, re.DOTALL).group(2)

if __name__ == "__main__":
    while(True):
        content = get_website_content()
        post = get_first_post(content)
        post_id = get_post_id(post)
        title = get_post_title(post)

        # Initialize last_post_id's value when running for the first time
        if(last_post_id == None):
            last_post_id = post_id

        # Check if the first post is different from the last one we got, that'd mean a new post has been created
        if(last_post_id != post_id):
            last_post_id = post_id
            print("A new post has been created", html.unescape(title))
            # TODO Send emails
        time.sleep(45)






