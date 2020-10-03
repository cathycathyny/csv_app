import os
import logging
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from fileManager import settings

# Create your views here.


class ServeReactApp(View):
    """
        Serves the compiled frontend entry point (only works if you have run
        `npm run build`).
    """

    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                    This URL is only used when you have built (npm run build) the production
                    version of the app. Visit http://localhost:3000/ after running npm start instead,
                    or run `npm run build` to test the production version.
                """, status=501)
