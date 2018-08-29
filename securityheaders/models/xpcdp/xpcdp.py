from securityheaders.models import SecurityHeader
from securityheaders.models.xpcdp import XPermittedCrossDomainPoliciesDirective
from securityheaders.models.annotations import description, headername

@description('This header defines a cross-domain policy for clients such as Adobe Flash Player or Adobe Acrobat.')
@headername('x-permitted-cross-domain-policies')
class XPermittedCrossDomainPolicies(SecurityHeader):
    directive = XPermittedCrossDomainPoliciesDirective
    
    def __init__(self, unparsedstring):
        SecurityHeader.__init__(self, unparsedstring, XPermittedCrossDomainPolicies.directive)
    
    def is_none(self):
        try:
            if self.parsedstring:
                return XPermittedCrossDomainPoliciesDirective.NONE in self.parsedstring.keys()
            return False
        except:
            pass
        return False
