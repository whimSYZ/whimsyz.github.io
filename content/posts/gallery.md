---
date: 2021-04-23T01:48:41+08:00
title: "Hugo shortcode gallery"
description: "Creating a gallery shortcode for hugo"
slug: ""
tags: ["css", "html", "hugo"]
categories: ["hugo", "front-end"]
externalLink: ""
series: []
ShowToc: true
TocOpen: true
---

## Apr. 18, 2021

Despite the pain during the term, it always feels empty after finishing all the finals.
So I decided to work on this little project that I have planned for a long time - **a gallery shortcode in hugo**.
My gallery before was simply cropping the images as squares and stacking them up to four columns. Athough
it can fulfill the basic needs, there are several pain points:
- The thumbnail is not configured correctly, so the gallery uses the real images as thumbnails, which slows down
the loading speed and
- My works are done in many different dimensions, and cropping them can cut away some information.
- The method of simply stacking square images can be aesthetically improved
- The images are not sort by time(instead they are sorted by file names), which means some of my oldest works got placed at the front

While the above issue can be addressed by finding and implementing existing short codes such as [hugo-shortcode-gallery](https://github.com/mfg92/hugo-shortcode-gallery) and [hugo-easy-gallery](https://github.com/liwenyip/hugo-easy-gallery), they are less customizable and have limitations(for example,
neither support "sort by time"). Additionally, it is a lot more fun to create one on my own, especially to the purpose of passing the boring spring in Taiyuan :)

So let's start by listing some criteria that I want the gallery to achieve.
- Lazy loading and thumbnails
- Grid layout
- Lightbox
- Sort by time(and presumably other ways)
- Description of images
- Portfolio to group related images


Looks like a lot of todos...but that's it for today, I need to go to sleep now. zZ

## Apr. 20, 2021


## Apr. 21
I tried to do the sorting trick. We can access the image's modified time using EXIF data. However, we I tried to do the following:
```
{{ range sort $images .Exif }}
...
{{ end }}
```
It returns the following error:
```
ERROR executing "shortcodes/gallery.html" at <.Exif>: can't evaluate field Exif in type resource.Resources
```
Seems like hugo can't recognize some image. The problem persists when I delete all but one images with the name "whale.jpg". However,
accessing .Exif after we do `{{ if eq .ResourceType "image" }}` seems ok, so there must be some object in `$images` that are not image.
But we used `{{ $images := .Page.Resources.ByType "image" }}` to get images!


## Apr. 23

Today I have mainly worked on the hover effects and sorting.
