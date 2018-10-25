import ftplib 

__author__      = "Devendra Dora"


src_dir='/home/devendradora/Downloads/test'
ftp_ip ='127.0.253.189'
ftp_user='dev'
ftp_password='dev@876'


ftp_dest_dir="/home/ubuntu"


def uploadFileToFTP(ftp_ip,ftp_user,ftp_password,src,dest):
    print("Trying to connect to "+ftp_ip+"\n Upload Files : "+src+" -> "+dest)
    ftp = ftplib.FTP(ftp_ip,ftp_user,ftp_password)
    #ftp.set_debuglevel(2)
    ftp.set_pasv(True)
    ftp.storbinary('STOR '+dest, open(src, 'rb'))
    ftp.quit()
    print("upload done\n")


class FTP_TLS_UNROUTABLE_HOST(ftplib.FTP_TLS, object):
    def makepasv(self):
        _, port = super(FTP_TLS_UNROUTABLE_HOST, self).makepasv()
        return self.host, port

def uploadFileToFTPTLS(ftp_ip,ftp_user,ftp_password,src,dest):
    print("Trying to connect to "+ftp_ip+"\n Upload Files : "+src+" -> "+dest)
    ftp = FTP_TLS_UNROUTABLE_HOST(ftp_ip,ftp_user,ftp_password)
    #ftp.set_debuglevel(2)
    ftp.set_pasv(True)
    ftp.storbinary('STOR '+dest, open(src, 'rb'))
    ftp.quit()
    print("upload done\n")


if __name__== "__main__":
	uploadFileToFTP(ftp_ip,ftp_user,ftp_password,src+"/"+filename,ftp_dest_dir+"/"+filename)
