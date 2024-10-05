import pyqrcode
content="https://youtube.com/"
url=pyqrcode.create(content)
url.png("myqr6.png",scale=5)
