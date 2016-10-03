# pelican-twitchy

pelican-twitchy is a bootstrap3 based pelican theme, with a static navbar on the left which is toggable to provide more space for content. Parts of it has been taken from the great [pelican-bootstrap3](https://github.com/DandyDev/pelican-bootstrap3) by [DandyDev](http://dandydev.net/), so credit where credit is due to all contributors of pelican-bootstrap3!

## Key Features

*    a sweet landing page
*    lots of space for modifications
*    powered by bootstrap
*    bootswatch theme support
*    fontawesome!
*    pygments theme support
*    `TYPOGRIFY` support
*    DISQUS support
*    Google Analytics support
*    CC License Footer (https://github.com/hlapp/cc-tools)
*    Support ToC plugins

## Theme Settings

### general
Setting name (followed by default value, if exists) | Description
--------------------------------------------------- | -----------
`SITESUBTITLE` | Provide a description of your site, inserted into landing page jumbatron
`RECENT_POST_COUNT = 5` | How many post should be displayed on the landing page.
`EXPAND_LATEST_ON_INDEX` | Expand the Latest Articles Section in the Sidebar if you are on `index.html`
`OPEN_GRAPH = False` | Add Open Graph meta section
`OPEN_GRAPH_IMAGE` | Url to a default image used in Open Graph, can be overwritten on article/page sites via `og_image` metadata

### more colours?
Setting name (followed by default value, if exists) | Description
--------------------------------------------------- | -----------
`BOOTSTRAP_THEME = "bootstrap"` | Which bootstrap theme should be loaded, see static/css for a list.
`PYGMENTS_STYLE = "native"` | Which pygments theme should be loaded, see static/css for a list.
`TYPOGRIFY = False` | If Typogrify css should be loaded
`CUSTOM_CSS` | Can be used to provide an additional css file, e.g.: `CUSTOM_CSS = "extra/custom.css"`

### sidebar
Setting name (followed by default value, if exists) | Description
--------------------------------------------------- | -----------
`SHARE = False` | Provide simple non tracking sharing buttons (fb, g+, twitter) for articles/pages and the landing page
`SOCIAL` | Links to your profile on other site, complete with icon, e.g.: `SOCIAL = (('Twitter', 'https://twitter.com/derwinlu'), ('Bitbucket', 'https://bitbucket.org/winlu'))`
`SITELOGO` | Add a SiteLogo to your Sidebar, expects the path to the logo similar to `CUSTOM_CSS`
`SITELOGO_SIZE` | width attribute of `SITELOGO`'s `img` tag.
`HIDE_SITENAME` | hides the sitename from the sidebar, useful if your sitelogo already contains your sitename.
`DISPLAY_RECENT_POSTS_ON_MENU` | Displays recent articles in the sidebar, count is determined by `RECENT_POST_COUNT`
`DISPLAY_PAGES_ON_MENU` | Displays pages in sidebar.
`DISPLAY_CATEGORIES_ON_MENU` | Displays category list in sidebar.
`DISPLAY_TAGS_ON_MENU` | Displays tag list in sidebar.

### cc license
These settings add a CC License note to the footer.

`CC_LICENSE` : Valid Settings are
*   `CC-BY` - attribution
*   `CC-BY-SA` - ShareAlike
*   `CC-BY-ND` - NoDerivatives
*   `CC-BY-NC` - attribution, No Commercial reuse
*   `CC-BY-NC-SA` - combination of above
*   `CC-BY-NC-ND` - combination of above

Alternatively, choose by features directly:
*   `CC_LICENSE_DERIVATIVES` - `yes` if permitted, `no` if not, `ShareAlike` if allowed under same terms
*   `CC_LICENSE_COMMERCIAL` - `yes` if allowed, `no` if not

`CC_ATTR_MARKUP` can be set to `True` if you want to include attribution markup in th elicense mark.

### DISQUS
Setting name (followed by default value, if exists) | Description
--------------------------------------------------- | -----------
`DISQUS_SITENAME` | Identifier set via DISQUS to identify the site.
`DISQUS_LOAD_LATER` | If `True` only display a button which will load DISQUS comments only after the button has been pressed.
`DISQUS_NO_ID` | If `True` does not prefix identifiers to article comments (same behaviour as standard `notmyidea` theme).

### Google Analytics
Setting name (followed by default value, if exists) | Description
--------------------------------------------------- | -----------
`GOOGLE_ANALYTICS` | GA Tracking Id
`GOOGLE_ANALYTICS_UNIVERSAL` | Universal Tracking Id
`GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY` | Property Id

### Open Graph
Setting name (followed by default value, if exists) | Description
--------------------------------------------------- | -----------
`OPEN_GRAPH_FB_APP_ID` | Add open graph section to articles
`OPEN_GRAPH_IMAGE` | Add image to OG section


## TODO
*    better social sharing support, maybe with lazy loaded widgets instead of simple sharer links?

##preview 
###live example
[heroicdebugging.biz](http://www.heroicdebugging.biz)
###big
![Preview big](/preview_big.PNG)
###small
![Preview small](/preview_small.PNG)
###article with toc
![Preview article](/preview_article.PNG)
