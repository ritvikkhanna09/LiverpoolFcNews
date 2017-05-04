from bs4 import BeautifulSoup
import mechanize
import urllib
def main():
    br = mechanize.Browser()
    br.set_handle_robots(False)
    url = "http://www.liverpoolfc.com/news/first-team"
    page = br.open(url)
    html = page.read()	
    soup = BeautifulSoup( html,"html.parser")
    
    ###for text in soup.findAll('p'):
        ###if (text.has_attr('class')) and text['class'] == ["post-synopsis"]:print (text.contents[0])

    for text in soup.findAll('p',{'class':"post-synopsis synopsis"}):
        a=text.contents[0]
        print("==>"+a.lstrip())
			
if __name__=="__main__":
    main()	
