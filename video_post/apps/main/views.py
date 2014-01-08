from django.shortcuts import render
from forms import VideoForm
# Create your views here.
def index(request):

	return render(request,'main/index.html')

def authenticate(request):

	pass
'''
<?php 
$app_id = "YOUR_APP_ID";
$app_secret = "YOUR_APP_SECRET"; 
$my_url = "YOUR_POST_LOGIN_URL"; 
$video_title = "YOUR_VIDEO_TITLE";
$video_desc = "YOUR_VIDEO_DESCRIPTION";

$code = $_REQUEST["code"];

if(empty($code)) {
   $dialog_url = "http://www.facebook.com/dialog/oauth?client_id=" 
     . $app_id . "&redirect_uri=" . urlencode($my_url) 
     . "&scope=publish_stream";
    echo("<script>top.location.href='" . $dialog_url . "'</script>");
}

$token_url = "https://graph.facebook.com/oauth/access_token?client_id="
    . $app_id . "&redirect_uri=" . urlencode($my_url) 
    . "&client_secret=" . $app_secret 
    . "&code=" . $code;
$access_token = file_get_contents($token_url);
 
$post_url = "https://graph-video.facebook.com/me/videos?"
    . "title=" . $video_title. "&description=" . $video_desc 
    . "&". $access_token;

echo '<form enctype="multipart/form-data" action=" '.$post_url.' "  
     method="POST">';
echo 'Please choose a file:';
echo '<input name="file" type="file">';
echo '<input type="submit" value="Upload" />';
echo '</form>';
?>
'''
