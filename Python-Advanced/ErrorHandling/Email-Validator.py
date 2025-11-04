#Email Validator

class MustContainAtSymbolError(Exception):
    pass

class NameTooShortError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

mail = input()

validDomains = ['com', 'bg', 'org', 'net']

while mail != "End":
    try:
        mailSplit = mail.split('@')
        if len(mailSplit) == 2:
            name = mailSplit[0]
            domain = mailSplit[1]
            if len(name) > 4:
                domainSplit = domain.split('.')
                if len(domainSplit) == 2 and domainSplit[1] in validDomains:
                    print (f"Email is valid")
                else:
                    raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
            else:
                raise NameTooShortError("Name must be more than 4 characters")
        else:
            raise MustContainAtSymbolError("Email must contain @")
    except (InvalidDomainError, NameTooShortError, MustContainAtSymbolError) as e:
        print (e)
    mail = input()
