def Projects():
    projects = [
        {
            'id':5,
            'title':'Star Wars',
            'byline': 'The Last Jedi',
            'year': '2017',
            'head_text':'Rey develops her newly discovered abilities with the guidance of Luke Skywalker, who is unsettled by the strength of her powers. Meanwhile, the Resistance prepares for battle with the First Order.',
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
        },
        {
            'id':6,
            'title':'Passengers',
            'year': '2016',
            'head_text':'A spacecraft traveling to a distant colony planet and transporting thousands of people has a malfunction in its sleep chambers. As a result, two passengers are awakened 90 years early.',
            'img_1': 'images/pasngers_1.jpg',
            'img_1_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'video_1':'https://player.vimeo.com/video/170367649" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen',
            'video_1_text': '',
            'img_2': '',
            'img_3': '',
            'img_4': ''
        },

        {
            'id':1,
            'title':'The Jungle Book',
            'year': '2016',
            'head_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'img_1': 'https://hdwallsource.com/img/2016/9/the-jungle-book-movie-desktop-wallpaper-51835-53541-hd-wallpapers.jpg',
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
            'head_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'img_1': 'https://nerdist.com/wp-content/uploads/2015/10/MartianDiff_FEAT.jpg',
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
            'head_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'img_1': 'http://dotb.tc0bblfg2d81v7kurec.netdna-cdn.com/wp-content/uploads/2015/12/Exodus-Gods-and-Kings.jpg',
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
            'head_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'img_1': ' ',
            'img_1_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'video_1':'https://player.vimeo.com/video/170367649" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen',
            'video_1_text': '',
            'img_2': '',
            'img_3': '',
            'img_4': ''
        },
        {
            'id':5,
            'title':'Fantastic Beasts',
            'head_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'img_1': ' ',
            'img_1_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'video_1':'https://player.vimeo.com/video/170367649" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen',
            'video_1_text': '',
            'img_2': '',
            'img_3': '',
            'img_4': ''
        },

        {
            'id':6,
            'title':'Passengers',
            'year': '2016',
            'head_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'img_1': ' ',
            'img_1_text':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus id vel omnis, veniam nesciunt adipisci quis voluptatum, ex error laudantium, voluptate aspernatur, facere doloribus nisi placeat recusandae provident commodi quas!',
            'video_1':'https://player.vimeo.com/video/170367649" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen',
            'video_1_text': '',
            'img_2': '',
            'img_3': '',
            'img_4': ''
        }
    ]

    return projects