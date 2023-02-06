from django.shortcuts import render
import json
import requests

# Create your views here.

from django.http import HttpResponse
import datetime

asset_base_url = "http://www.suitedtoadventure.com:1337"


class Content:
    def __init__(self, cid, slug):
        self.api_url = f"{asset_base_url}/api"
        self.cid = cid
        self.slug = slug

    def single(self):
        r = requests.get(f"{self.api_url}/{self.slug}/?populate=%2A")
        print(r.url)
        return r.json()

    def all(self):
        r = requests.get(self.api_url + "/content-customs/")
        return r.json()


def get_content(cid, slug):
    content = Content(cid, slug)
    return content.single()


def index(request):
    page_content = get_content(None, 'home-page')

    page_title = 'Home | Suited To Adventure'
    banner_headline = page_content['data']['attributes']['banner_title']
    banner_subtitle = page_content['data']['attributes']['banner_caption']
    banner_bg_image = f"{asset_base_url}{page_content['data']['attributes']['banner_bg_image']['data']['attributes']['url']}"
    text_1 = page_content['data']['attributes']['section_1_text_1']
    image_1 = f"{asset_base_url}{page_content['data']['attributes']['section_1_image_1']['data']['attributes']['url']}"

    return render(request, 'bootstrap-5-full-image-cover-template-main/home.html', { 'page_title': page_title, 'banner_headline': banner_headline, 'banner_subtitle': banner_subtitle, 'banner_bg_image': banner_bg_image, 'text_1': text_1, 'image_1': image_1})


def inside(request):
    page_title = 'Inside Page Demo | Suited To Adventure'
    page_headline = 'Inside Headline'
    page_content = '<h2>Headline Two</h2><p>This is example content only.</p><h3>Headline Three</h3><p>Also some example content.</p>'
    return render(request, 'bootstrap-5-full-image-cover-template-main/inside.html', {'page_headline': page_headline, 'page_title': page_title, 'page_content': page_content})


def blog(request, year, month, slug):
    page_title = 'Blog | Suited To Adventure'
    page_headline = 'Blog'
    page_content = '<h2>Headline Two</h2><p>This is blog content only.</p><h3>Headline Three</h3><p>Also some blog content.</p>'

    # making api call to strapi > get blog post
    # returns json / dictionary > iterate to render content variables

    return render(request, 'bootstrap-5-full-image-cover-template-main/blog.html', {'metadata': {'article_year': year, 'article_month': month, 'article_slug': slug}, 'page_headline': page_headline, 'page_title': page_title, 'page_content': page_content})
