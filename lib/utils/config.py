"""
Config class, mostly extended from ntlmrelayx
"""
from impacket.examples.ntlmrelayx.utils.config import NTLMRelayxConfig

class KrbRelayxConfig(NTLMRelayxConfig):
    def __init__(self):
        NTLMRelayxConfig.__init__(self)

        # Auth options
        self.dcip = None
        self.aeskey = None
        self.hashes = None
        self.password = None
        self.israwpassword = False
        self.salt = None

        # Krb options
        self.format = 'ccache'

        # LDAP options
        self.dumpdomain = True
        self.addda = True
        self.aclattack = True
        self.validateprivs = True
        self.escalateuser = None
        self.addcomputer = False
        self.delegateaccess = False

        # SCCM attacks options
        self.isSCCMPoliciesAttack = False
        self.SCCMPoliciesClientname = None
        self.SCCMPoliciesSleep = None
        self.isSCCMDPAttack = False
        self.SCCMDPExtensions = None
        self.SCCMDPFiles = None

        # Custom options
        self.victim = None

    # Make sure we have a fixed version of this to avoid incompatibilities with impacket
    def setLDAPOptions(self, dumpdomain, addda, aclattack, validateprivs, escalateuser, addcomputer, delegateaccess, dumplaps, dumpgmsa, dumpadcs, sid):
        self.dumpdomain = dumpdomain
        self.addda = addda
        self.aclattack = aclattack
        self.validateprivs = validateprivs
        self.escalateuser = escalateuser
        self.addcomputer = addcomputer
        self.delegateaccess = delegateaccess
        self.dumplaps = dumplaps
        self.dumpgmsa = dumpgmsa
        self.dumpadcs = dumpadcs
        self.sid = sid

    def setAuthOptions(self, aeskey, hashes, dcip, password, salt, israwpassword=False):
        self.dcip = dcip
        self.aeskey = aeskey
        self.hashes = hashes
        self.password = password
        self.salt = salt
        self.israwpassword = israwpassword

    def setKrbOptions(self, outformat, victim):
        self.format = outformat
        self.victim = victim

        def setIsSCCMPoliciesAttack(self, isSCCMPoliciesAttack):
        self.isSCCMPoliciesAttack = isSCCMPoliciesAttack
    
    def setSCCMPoliciesOptions(self, sccm_policies_clientname, sccm_policies_sleep):
        self.SCCMPoliciesClientname = sccm_policies_clientname
        self.SCCMPoliciesSleep = sccm_policies_sleep
    
    def setIsSCCMDPAttack(self, isSCCMDPAttack):
        self.isSCCMDPAttack = isSCCMDPAttack
    
    def setSCCMDPOptions(self, sccm_dp_extensions, sccm_dp_files):
        self.SCCMDPExtensions = sccm_dp_extensions
        self.SCCMDPFiles = sccm_dp_files
