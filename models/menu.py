# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = ' '.join(word.capitalize() for word in request.application.split('_'))

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'
response.meta.copyright = 'Copyright 2011'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default','index'), []),
    (T('User Profile'), False, None, [
        (T('User Profile'), False, URL('default','user_profile')),
        (T('Create User Profile'), False, URL('default','create_user_profile')),
        (T('Update User Profile'), False, URL('default','update_user_profile'))
        ]),
    (T('Book'), False, None,  [
        (T('Book Profile'), False, URL('default', 'book_profile')),
        (T('Create Book Profile'), False, URL('default', 'create_book_profile')),
        (T('Update Book Profile'), False, URL('default', 'update_book_profile'))
        ]),
    (T('Book Shelf'), False, None,  [
        (T('Book Shelf'), False, URL('default', 'book_shelf')),
        (T('Create Book Shelf'), False, URL('default', 'create_book_shelf')),
        (T('Update Book Shelf'), False, URL('default', 'update_book_shelf'))
        ])
    ]

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

