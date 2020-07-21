import secrets
import os

def allowed_file(filename, extn):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in [extn]

def save_file(attachment, type='pdf'):
    #create random file name
    random_hex = secrets.token_hex(8)
    _ , f_ext = os.path.splitext(attachment.filename)
    file_fn = random_hex + f_ext

    #saved file path
    attachment_path = os.path.join('static/' + type, file_fn)
    attachment.save(attachment_path)
    return file_fn