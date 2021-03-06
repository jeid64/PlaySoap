from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=1)
    config.add_route('home', '/')
    config.add_route('login','/login')
    config.add_route('returnLibrary', '/returnLibrary/{service}/{queue}/{id}')
    config.add_route('addToAjaxQueue','/ajaxqueue/{service}/{queue}/{id}')
    config.add_route('returnQueue', '/returnqueue/{userNumber}/{queue}')
    config.add_route('nextSong', 'nextSong/{userNumber}/{queue}/{id}')
    config.scan()
    return config.make_wsgi_app()
