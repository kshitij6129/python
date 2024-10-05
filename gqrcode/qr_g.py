import pyqrcode
content="https://youtube.com/"
url=pyqrcode.create(content)
url.png("myqr1.png",scale=5)
