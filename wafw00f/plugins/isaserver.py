#!/usr/bin/env python


NAME = 'Microsoft ISA Server'


def is_waf(self):
    isaservermatch = [
        'Forbidden ( The server denied the specified Uniform Resource Locator (URL). Contact the server administrator.  )',
        'Forbidden ( The ISA Server denied the specified Uniform Resource Locator (URL)'
    ]
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        response, page = r    
        if response.reason in isaservermatch:
            return True
        # This is also found in response page of URLs
        if any(a in page for a in (b'The ISA Server denied the specified Uniform Resource Locator (URL)',
            b'The server denied the specified Uniform Resource Locator (URL). Contact the server administrator.')):
            return True
    return False