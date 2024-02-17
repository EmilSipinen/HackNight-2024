# HackNight - 2024.02.16 hackathon

Co-programmed by Emil and Andrew.

This is a very simple, pure OpenCV implementation of a motion tracker. We took
the grey of a Lidl plastic bag and used it to create a motion tracker.

## Quickstart

Clone this repo and `cd` into the directory. Then run:

```bash
pip install opencv-python Flask    # just opencv if you don't want to run the web app

python app.py
```

Then go to `localhost:5000` (or wherever the server is running) and you should
be able to se the motion tracker from your own webcam.

Alternatively, if you just want to run it as a fully local program:

```bash
python test2.py    # the latest on
python test.py     # cool but less useful, how we figured out to use the background subtractor
python main.py     # earliest prototype
```
