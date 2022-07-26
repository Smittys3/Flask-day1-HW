from app import app
from flask import Flask, render_template


@app.route('/')
def index():
    home = [{'img': 'https://thehappyarkansan.com/wp-content/uploads/2017/09/My-All-Time-Favorite-Artists-And-Bands.png'}]
    return render_template('index.html', items=home)


@app.route('/fav_5')
def fav_5():
    artists = [
        {'name': 'Andy Mineo', 'img':'https://relevantmagazine.com/wp-content/uploads/2019/05/AndyMineoSocialMedia.jpg'},
        {'name': 'Trip Lee', 'img':'http://www.reachrecords.com/wp-content/uploads/2015/05/tripbanner-1280x552.jpg'},
        {'name': 'KB', 'img':'https://whoiskb.com/wp-content/uploads/2020/05/kb-in-mask2-FINAL-KBSITE.jpg'},
        {'name': 'Beautiful Eulogy', 'img':'https://yt3.ggpht.com/GbwY9mBqCeMAnfcbAajmt8GLzdTfHBG6k5A0df1lITc0-hejHyLPROtlSvS9JoFK4-PZt6u0QR4=s900-c-k-c0x00ffffff-no-rj'},
        {'name': 'Social Club Misfits', 'img':'https://i.scdn.co/image/ab67616d0000b273005eb659d7583e602bfad8c4'},
        {'name': 'Chris Quilala', 'img':'https://www.jesusfreakhideout.com/artists/full/chrisquilala.jpg'}
    ]
    return render_template('fav_5.html', names=artists)

