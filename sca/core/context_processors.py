# This could be moved to settings/base if necessary
SITE_NAME = 'Savorcakes Academy'

# Should use django's site framework
def site_name(request):
    '''
    This returns the name of the site
    '''
    return {'site_name': SITE_NAME}
