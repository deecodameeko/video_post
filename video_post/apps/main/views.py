from api import Api
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import facebook
import json
import os

def index(request):

    return render(request,'main/index.html', {'APP_ID':settings.FACEBOOK_APP_ID})


def post_video(request):

    '''
    get the video url from the api
    post it using the facebook(check should happen on client side but doing a sanity test is never a bad idea before attempting to post)
    this will be an ajax call...responses to follow
    '''

    user = None
    user = facebook.get_user_from_cookie(request.COOKIES, settings.FACEBOOK_APP_ID, settings.FACEBOOK_SECRET_KEY)

    if user.get('access_token'):
        #let's get the user's 
        #api = Api()    
        #video = api.get_video_url(submission_id)
        kwargs = {'title':'testing', 'description':'just a test'}
        graph = facebook.GraphAPI(user['access_token'])
        graph.put_media(os.path.join(os.getcwd(), 'sample_video.mp4'), None, False, **kwargs)
        response = json.dumps({'status':200})

    else:
        #send back error stating they're not logged in(btw this should never happen)
        response = json.dumps({'status':401})

    return HttpResponse(response, mimetype='application/x-javascript')	

def post_photo(request):

    '''
    this is just an example....you'd probably want to not post a static image but load one from a remote path on your machine
    '''

    user = None
    user = facebook.get_user_from_cookie(request.COOKIES, settings.FACEBOOK_APP_ID, settings.FACEBOOK_SECRET_KEY)

    if user.get('access_token'):
        kwargs = {'title':'testing', 'description':'just a test'}
        graph = facebook.GraphAPI(user['access_token'])
        graph.put_media(os.path.join(os.getcwd(), 'http_slash.jpg'), None, True, **kwargs)
        response = json.dumps({'status': 200})

    else:
        response = json.dumps({'status': 401, 'message': 'no access token found'})

    return HttpResponse(response, mimetype='application/x-javascript')


@csrf_exempt
def save_access_token(request, access_token):

    request.session['access_token'] = access_token
    return HttpResponse(json.dumps({'status': 200}), mimetype='application/x-javascript')

