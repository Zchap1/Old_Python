'''MENU
Home
SUBSCRIBE
MENU
How to make a web crawler in under 50 lines of Python code
24 SEPTEMBER 2011 on How-To, Programming, Python, Python 3, Tutorial, Web Crawler, Web Spider
Interested to learn how Google, Bing, or Yahoo work? Wondering what it takes to crawl the web, and what a simple web crawler looks like? In under 50 lines of Python (version 3) code, here's a simple web crawler! (The full source with comments is at the bottom of this article).



And let's see how it is run. Notice that you enter in a starting website, a word to find, and the maximum number of pages to search through.



Okay, but how does it work?
Let's first talk about what a web crawler's purpose is. As described on the Wikipedia page, a web crawler is a program that browses the World Wide Web in a methodical fashion collecting information. What sort of information does a web crawler collect? Typically two things:
'''
'''
Web page content (the text and multimedia on a page)
Links (to other web pages on the same website, or to other websites entirely)
Which is exactly what this little "robot" does. It starts at the website that you type into the spider() function and looks at all the content on that website. This particular robot doesn't examine any multimedia, instead it is just looking for "text/html" as described in the code. Each time it visits a web page it collects two sets of data: All the text on the page, and all the links on the page. If the word isn't found in the text on the page, the robot takes the next link in its collection and repeats the process, again collecting the text and the set of links on the next page. Again and again, repeating the process, until the robot has either found the word or has runs into the limit that you typed into the spider() function.

Is this how Google works?
Sort of. Google has a whole fleet of web crawlers constantly crawling the web, and crawling is a big part of discovering new content (or keeping up to date with websites that are constantly changing or adding new stuff). However you probably noticed that this search took awhile to complete, maybe a few seconds. On more difficult search words it might take even longer. There's another big component to search engines called indexing. Indexing is what you do with all the data that the web crawler collects. Indexing means that you parse (go through and analyze) the web page content and create a big collection (think database or table) of easily accessible and quickly retrievable information. So when you visit Google and type in "kitty cat", your search word is going straight* to the collection of data that has already been crawled, parsed, and analyzed. In fact, your search results are already sitting there waiting for that one magic phrase of "kitty cat" to unleash them. That's why you can get over 14 million results within 0.14 seconds.

*Your search terms actually visit a number of databases simultaneously such as spell checkers, translation services, analytic and tracking servers, etc.

Let's look at the code in more detail!
The following code should be fully functional for Python 3.x. It was written and tested with Python 3.2.2 in September 2011. Go ahead and copy+paste this into your Python IDE and run it or modify it!
'''
from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse

# We are going to create a class called LinkParser that inherits some
# methods from HTMLParser which is why it is passed into the definition
class LinkParser(HTMLParser):

    # This is a function that HTMLParser normally has
    # but we are adding some functionality to it
    def handle_starttag(self, tag, attrs):
        # We are looking for the begining of a link. Links normally look
        # like <a href="www.someurl.com"></a>
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    # We are grabbing the new URL. We are also adding the
                    # base URL to it. For example:
                    # www.netinstructions.com is the base and
                    # somepage.html is the new URL (a relative URL)
                    #
                    # We combine a relative URL with the base URL to create
                    # an absolute URL like:
                    # www.netinstructions.com/somepage.html
                    newUrl = parse.urljoin(self.baseUrl, value)
                    # And add it to our colection of links:
                    self.links = self.links + [newUrl]

    # This is a new function that we are creating to get links
    # that our spider() function will call
    def getLinks(self, url):
        self.links = []
        # Remember the base URL which will be important when creating
        # absolute URLs
        self.baseUrl = url
        # Use the urlopen function from the standard Python 3 library
        response = urlopen(url)
        # Make sure that we are looking at HTML and not other things that
        # are floating around on the internet (such as
        # JavaScript files, CSS, or .PDFs for example)
        if response.getheader('Content-Type')=='text/html':
            htmlBytes = response.read()
            # Note that feed() handles Strings well, but not bytes
            # (A change from Python 2.x to Python 3.x)
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString, self.links
        else:
            return "",[]

# And finally here is our spider. It takes in an URL, a word to find,
# and the number of pages to search through before giving up
def spider(url, word, maxPages):  
    pagesToVisit = [url]
    numberVisited = 0
    foundWord = False
    # The main loop. Create a LinkParser and get all the links on the page.
    # Also search the page for the word or string
    # In our getLinks function we return the web page
    # (this is useful for searching for the word)
    # and we return a set of links from that web page
    # (this is useful for where to go next)
    while numberVisited < maxPages and pagesToVisit != [] and not foundWord:
        numberVisited = numberVisited +1
        # Start from the beginning of our collection of pages to visit:
        url = pagesToVisit[0]
        pagesToVisit = pagesToVisit[1:]
        try:
            print(numberVisited, "Visiting:", url)
            parser = LinkParser()
            data, links = parser.getLinks(url)
            if data.find(word)>-1:
                foundWord = True
                # Add the pages that we visited to the end of our collection
                # of pages to visit:
                pagesToVisit = pagesToVisit + links
                print(" **Success!**")
        except:
            print(" **Failed!**")
    if foundWord:
        print("The word", word, "was found at", url)
    else:
        print("Word never found")

'''
Magic!

Further reading
In December 2014 I wrote a guide on making a web crawler in Java and in November 2015 I wrote a guide on making a web crawler in Node.js / Javascript. Check those out if you're interested in seeing how to do this in another language.

If Python is your thing, a book is a great investment, such as the following



Good luck!


 
Stephen
Read more posts by this author.

Share this post
  
View or post Comments

Load Comments
How I taught myself to program (and which languages in what order)
Interested in learning to program and write code? Wondering what programming language you should teach yourself? Curious how other…
Everything you need to get a website up and running
We live in 2011, complete with computers and the ever present internet and world wide web. Nearly everything has…
'Net Instructions © 2011-2016Proudly published with Ghost'''
