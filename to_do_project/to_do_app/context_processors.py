def user_avatar(request):
    if request.user.is_authenticated:
        try:
            return {'user_avatar': request.user.userprofile.avatar}
        except:
            return {'user_avatar': None}
    return {'user_avatar': None}