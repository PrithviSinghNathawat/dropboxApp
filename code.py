import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.BAEucSCQB-evpI3oy6S8psd7-CMQgaRoszpsxk26TU9J57YmbC4SZ23WHjywEE1ftbtv9QOlwXT7WiKenXOmKrpkXYojnNmWZ0ubrZGSOVPSsFJX0OnjaWPj-P-ZWbs9MjpE0VM'
    transferData=TransferData(access_token)

    file_from=input('enter the source path:')
    file_to=input('enter the destined path:')

    transferData.upload_file(file_from,file_to)
    print('files have been moved')

main()
