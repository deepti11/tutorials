#from django.http import HttpResponse, Http404
#from django.template import loader
from .models import Album, Song
from django.shortcuts import render, get_object_or_404

def index(request):
    html =  ''
    all_albums = Album.objects.all()

    #for album in all_albums:
    #    url = '/music/' + str(album.id) + '/'
    #    html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    #template = loader.get_template('music/index.html')

    context = {'all_albums': all_albums}
    #return HttpResponse(html)
    #return HttpResponse(template.render(context,request))
    # render has in built Http Response
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    #return HttpResponse("<h2> Details for Album ID:" + str(album_id) + "</h2>")
    #try:
    #    album = Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
    #    raise Http404("Album does not exist")
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html',
                  {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html',
                      {'album': album,
                       'error_message': 'You did not select any valid song',})

    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html',
                  {'album': album})
