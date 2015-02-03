from base import ProxyModuleBase


class allFail(ProxyModuleBase):
    def onResponse(self, **kwargs):
        self.response_object.handleStatus(version='HTTP/1.1',
                                          code=404,
                                          message="Sorry bub, Not found")
