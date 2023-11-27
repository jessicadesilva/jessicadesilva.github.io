import os

secret_key = os.urandom(24).hex()
upload_folder = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "website", "static", "images"
)
allowed_extensions = {"pdf", "png", "jpg", "jpeg", "gif"}

if __name__ == "__main__":
    with open(".env", "w") as f:
        f.write(f"SECRET_KEY={secret_key}\n")
        f.write(f"UPLOAD_FOLDER={upload_folder}\n")
        f.write(f"ALLOWED_EXTENSIONS={allowed_extensions}\n")
