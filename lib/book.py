#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self.title = title
        self._page_count= page_count

    
    def get_pages(self):
        return self._page_count
    
    
    def set_pages(self,value):
        if type(value) == int: 
            self._page_count = value
        else:
            print( "page_count must be an integer")
            
    page_count = property(get_pages,set_pages)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


    
    
        
    
        