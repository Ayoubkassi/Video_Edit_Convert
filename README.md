# Video_Edit_Convert

---

## install dependencies :

```
./configure
configure --help
configure
make
make install
```

> Extract Images from a Video : ffmpeg -i video_name.avi -r 1 -s WxH -f image2 foo-%03d.png

> Create video from images : ffmpeg -f image2 -framerate 15 -i foo-%03d.png -s 400x400 foo.avi -y
