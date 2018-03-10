def Projects():
    projects = [
        {
            'id':5,
            'title':'Star Wars',
            'byline': 'The Last Jedi',
            'year': '2017',
            'head_text':'Rey develops her newly discovered abiliti.',
            'media':
                    {
                        'img_1': 'images/star_wars.jpg',
                        'img_1_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
                        'video_1':'https://player.vimeo.com/video/170367649" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen',
                        'video_1_text': '',
                        'img_2': 'images/star_wars_2.jpg',
                        'img_2_text':'tekst uz sliku 2',
                        'img_3': 'images/star_wars_3.jpg',
                        'img_3_text':'tekst uz sliku 3',
                        'img_4': 'images/star_wars_4.jpg',
                        'img_4_text':'tekst uz sliku 4'
                   }
        },
        {
            'id':6,
            'title':'Passengers',
            'year': '2016',
            'head_text':'Lorem ipsum dolor sit amet!',
            'img_1': 'images/Passengers.jpg',
            'img_1_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'video_1':'https://player.vimeo.com/video/170367649" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen',
            'video_1_text': '',
            'img_2': 'https://images5.alphacoders.com/789/789272.jpg',
            'img_3': 'http://www.maacindia.com/blog/wp-content/uploads/2016/04/sketches-of-characters-from-disney.jpg',
            'img_4': ''
        },

        {
            'id':1,
            'title':'The Jungle Book',
            'year': '2016',
            'head_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'img_1': 'images/The_Jungle_Book.jpg',
            'img_1_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'video_1':'https://player.vimeo.com/video/170367649" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen',
            'video_1_text': '',
            'img_2': 'https://images5.alphacoders.com/789/789272.jpg',
            'img_3': 'http://www.maacindia.com/blog/wp-content/uploads/2016/04/sketches-of-characters-from-disney.jpg',
            'img_4': ''
        },
        {
            'id':2,
            'title':'The Martian',
            'year': '2015',
            'head_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'img_1': 'images/Martian.jpg',
            'img_1_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'video_1':'https://player.vimeo.com/video/170367649" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen',
            'video_1_text': '',
            'img_2': '',
            'img_3': '',
            'img_4': ''
        },
        {
            'id':3,
            'title':'Exodus',
            'byline': 'Gods and Kings',
            'year': '2014',
            'head_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'img_1': 'images/Exodus.jpg',
            'img_1_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'video_1':'https://player.vimeo.com/video/170367649" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen',
            'video_1_text': '',
            'img_2': '',
            'img_3': '',
            'img_4': ''
        },
        {
            'id':4,
            'title':'Gardians of the galaxy',
            'year': '2014',
            'head_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'img_1': 'images/galaxy.jpg',
            'img_1_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'video_1':'https://player.vimeo.com/video/170367649" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen',
            'video_1_text': '',
            'img_2': '',
            'img_3': '',
            'img_4': ''
        },
        {
            'id':5,
            'title':'Fantastic Beasts and Where to Find Them',
            'year': '2016',
            'head_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'img_1': 'images/fantastic.jpg',
            'img_1_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'video_1':'https://player.vimeo.com/video/170367649" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen',
            'video_1_text': '',
            'img_2': '',
            'img_3': '',
            'img_4': ''
        },

        {
            'id':6,
            'title':'Doctor Strange',
            'year': '2016',
            'head_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'img_1': 'images/strange.jpg',
            'img_1_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'video_1':'https://player.vimeo.com/video/170367649" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen',
            'video_1_text': '',
            'img_2': '',
            'img_3': '',
            'img_4': ''
        },
        {
            'id':6,
            'title':'Doctor Strange',
            'year': '2016',
            'head_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'img_1': 'images/strange.jpg',
            'img_1_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'video_1':'https://player.vimeo.com/video/170367649" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen',
            'video_1_text': '',
            'img_2': '',
            'img_3': '',
            'img_4': ''
        }


    ]

    return projects