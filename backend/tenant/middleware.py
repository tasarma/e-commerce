from typing import Optional

from django.http.request import HttpRequest
from django.http.response import HttpResponseBadRequest, HttpResponse

from .models import Tenant


class TenantMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        tenant = self.get_tenant(request)
        if tenant:
            request.tenant = tenant
       # else:
        #    return HttpResponseBadRequest("Invalid tenant")

        response = self.get_response(request)
        return response

    def get_hostname(self, request: HttpRequest) -> str:
        return request.headers["Host"].split(":")[0].lower()

    def get_tenant(self, request: HttpRequest) -> Optional[Tenant]:
        hostname = self.get_hostname(request)
        subdomain = hostname.split(".")[0]

        return Tenant.objects.filter(subdomain=subdomain).first()
