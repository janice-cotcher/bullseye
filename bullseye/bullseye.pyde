# bullseye that alternates red and white
size(600, 600)
# black background
background(0)


def circle(d):
    """circle function that is centred in the middle
    of the screen with diameter d"""
    ellipse(300, 300, d, d)


# 6 concentric circles that alternate red and white
circle(600)
circle(500)
circle(400)
circle(300)
circle(200)
circle(100)
