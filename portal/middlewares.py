"""
App specific middlewares.
"""

import secure

secure_headers = secure.Secure(
    server=secure.Server(),
    hsts=secure.StrictTransportSecurity(),
    xfo=secure.XFrameOptions(),
    xxp=secure.XXSSProtection(),
    content=secure.XContentTypeOptions(),
    csp=secure.ContentSecurityPolicy(),
    referrer=secure.ReferrerPolicy(),
)


def set_secure_headers(get_response):
    def middleware(request):
        response = get_response(request)
        secure_headers.framework.django(response)
        return response

    return middleware
