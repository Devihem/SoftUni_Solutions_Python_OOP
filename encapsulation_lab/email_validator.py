class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email: str):
        name, mail_domain = email.split('@')
        mail, domain = mail_domain.split('.')

        check_name = self.__is_name_valid(name)
        check_mail = self.__is_mail_valid(mail)
        check_domain = self.__is_domain_valid(domain)

        return all([check_name, check_mail, check_domain])
