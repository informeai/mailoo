from smtplib import SMTP_SSL, SMTP, SMTPAuthenticationError,SMTPException,SMTPHeloError,SMTPResponseException,SMTPServerDisconnected
from email.message import EmailMessage
from email.mime.text import MIMEText


class Mail:
    """
    Python class for creating Emails and sending via SMTP servers ...
    Class Use:
    If the User Email is from GMAIL -> Necessary to create application key, Link: https://support.google.com/mail/answer/185833?hl=en,
    in possession of the key, use as the password.
    If the User Email is from OUTLOOK, HOTMAIL, YAHOO -> Use default email and password.

    """

    def __init__(self,user_email:str, key_acess:str):
        """
        Email Object Initialization Method ...
        Creates an instance of the Mail Object.
        """
        self.user_email = user_email
        self.key_acess = key_acess
        self.host, self.port = self._provider(self.user_email)
        return

    def send(self,subject:str,msg:str=None,email:str=None,file_html:str=None,file_emails:str=None):
        """
        Method responsible for sending emails ...
        USE:
        msg or file_html -> message to be sent / html file to be sent.
        email or file_emails -> single recipient email / file 'TXT', containing emails.
        subject -> Email Subject.

        """
        if msg and file_html or email and file_emails:
            print(f'Duplicated of Arguments : USE -> msg ou file_html, emails ou file_emails')
        else:

            if not msg and not file_html:
                print(f'Write a message or send an html file.')

            if file_emails and msg:
                list_emails_msg = self._load_emails(file_emails)
                for email in list_emails_msg:
                    self._send_text(msg,subject,email)
            elif msg and email:
                self._send_text(msg,subject,email)
            elif file_emails and file_html:
                list_emails_html = self._load_emails(file_emails)
                for email in list_emails_html:
                    self._send_file(file_html,subject,email)
            else:
                self._send_file(file_html,subject,email)
            
        

    def _send_file(self, file, subject:str,dest_email:str):
        """
        Method Used for sending files. Ex: * .html, * .txt.
        """
        self.file = file
        
        try:
            with open(self.file,'rb') as arquivo:
                content_html = arquivo.read()
                arquivo.close()
        except FileNotFoundError:
            print(f'FILE: \033[1;91m{self.file}\033[0;0m4 not Existed.\n')
        else:
            print(f'File Read Successfully.\n')
            

        self.msg = content_html
        self.subject = subject
        self.dest_email = dest_email
        self.msg = self._html(self.msg, self.dest_email,subject=self.subject)
        
        if self.host == 'smtp.office365.com':
            try:
                with  SMTP(self.host, self.port) as mail_noSSl:
                    mail_noSSl.starttls()
                    mail_noSSl.login(self.user_email, self.key_acess)
                    mail_noSSl.send_message(self.msg, self.user_email, self.dest_email)
                    mail_noSSl.quit()
            except Exception as err:
                print(f'ERROR: {err}')
            else:
                print(f'Email sent to the RECIPIENT: \033[1;32m{self.dest_email}\033[0;0m  done.')
        else:
            with SMTP_SSL(self.host, self.port) as mail:
                try:
                    mail.login(self.user_email,self.key_acess)
                except SMTPAuthenticationError:
                    print(f'The Server did not accept the USER combination: {self.user_email} , more the PASSWORD')
                except SMTPHeloError:
                    print(f'The Email Server did not respond to the login request.')
                except SMTPServerDisconnected:
                    print(f'The Server Unexpectedly Disconnected.')
                except SMTPResponseException as resp_err:
                    print(f'There was an error with the server response.\n CODE: {resp_err.smtp_code}.\n ERROR: {resp_err.smtp_error}')
                except SMTPException:
                    print(f'No Authentication method found.')
                
                try:
                    mail.send_message(self.msg,self.user_email,self.dest_email)
                    mail.quit()
                except Exception as err:
                    print(err)
                else:
                    print(f'Email sent to the RECIPIENT: \033[1;32m{self.dest_email}\033[0;0m done.')

    def _send_text(self, text, subject:str,dest_email:str):
        """
       Method Used to send plain text or html in-line.
        """
        self.msg = text
        self.subject = subject
        self.dest_email = dest_email
        
            
        self.msg = self._html(self.msg, self.dest_email,subject=self.subject)


        if self.host == 'smtp.office365.com':
            try:
                with SMTP(self.host, self.port) as mail_noSSl:
                    mail_noSSl.starttls()
                    mail_noSSl.login(self.user_email, self.key_acess)
                    mail_noSSl.send_message(self.msg, self.user_email, self.dest_email)
                    mail_noSSl.quit()
            except Exception as err:
                print(f'ERROR: {err}')
            else:
                print(f'Email sent to the RECIPIENT: \033[1;32m{self.dest_email}\033[0;0m  done.')
        else:
            with SMTP_SSL(self.host, self.port) as mail:
                try:
                    mail.login(self.user_email,self.key_acess)
                except SMTPAuthenticationError:
                    print(f'The Server did not accept the USER combination: {self.user_email} , more the PASSWORD.')
                except SMTPHeloError:
                    print(f'The Email Server did not respond to the login request.')
                except SMTPServerDisconnected:
                    print(f'The server unexpectedly disconnected.')
                except SMTPResponseException as resp_err:
                    print(f'There was an error with the server response.\n CODE: {resp_err.smtp_code}.\n ERROR: {resp_err.smtp_error}')
                except SMTPException:
                    print(f'No Authentication method found.')
                    
                try:
                    mail.send_message(self.msg,self.user_email,self.dest_email)
                    mail.quit()
                except Exception as err:
                    print(err)
                else:
                    print(f'Email sent to the RECIPIENT: \033[1;32m{self.dest_email}\033[0;0m done.')

    def _html(self, msg, dest_email,subject=None):
        self.msg = msg
        self.subject = subject
        self.dest_email = dest_email
        self.obj_email = EmailMessage()
        self.obj_email['Subject'] = self.subject
        self.obj_email['From'] = self.user_email
        self.obj_email['To'] = self.dest_email
        self.obj_email.set_type('text/html', header='Content-Type', requote=False)
        self.obj_email.set_payload(self.msg,charset='utf-8')
        
        return self.obj_email
        

    def _provider(self, user:str):
        if "@gmail" in user:
            return ('smtp.gmail.com', 465)
        elif "@outlook" in user or "@hotmail" in user:
            return ('smtp.office365.com', 587)
        elif "@yahoo" in user:
            return ('smtp.mail.yahoo.com', 465)
        
            
    def _load_emails(self,file:str) -> list:
        lista_emails = []
        try:
            with open(file, 'rt') as arq_emails:
                emails = arq_emails.readlines()
                for email in emails:
                    if '\n' in email:
                        email = email[:-1]
                    lista_emails.append(email)
            arq_emails.close()
        except FileNotFoundError:
            print(f'File:  \033[1;91m{file}\033[0;0m unrecognized.')
        else:
            print(f'List of Uploaded Email Files.')
            return lista_emails
        
