---
title: Using OpenCV and Jupyter Docker
author: koblas
type: post
date: 2017-01-02T13:16:37+00:00
url: /p/opencv-and-juypter-docker/633
categories:
  - development
  - opencv

---

Working on getting some OCR work done in OpenCV and trying to wrap my head around how the library works and
the functions it provides. Since I'm doing all of the work in Python realizes that while it's possible to
write a good Python program to visualize the steps it was getting bit repetitive.

For example my ptyhon code had the following block to display a set of images (OpenCV images):

	def show_image(images):
		for idx, idata in enumerate(images):
			title, img = idata
			plt.subplot(1, len(images), idx+1)
			plt.title(title)
			plt.imshow(img, 'gray')
			plt.xticks([])
			plt.yticks([])
		plt.show()

Relizing that a lot of what I was doing was iterative development were I wanted to see intermediate results, 
decided that it would make more sense to move to Jupyter Notbook development so I created the following docker:

# Moving to Jupyter

Create a `Dockerfile`

    FROM jupyter/datascience-notebook

    # install in the default python3 environment
    RUN pip install 'opencv-python==3.1.0.3'
    # install in the python2 environment also
    RUN bash -c "source activate python2 && pip install 'opencv-python==3.1.0.3'"

Build the notebook:

	docker build --rm -t jupyter/opencv-notebook .

Run the notbook:

	docker run -v /Users/koblas/opencv_testing:/home/jovyan/work -d -p 8888:8888 jupyter/opencv-notebook

Now could write the following to display images in my notebook:

	from io import BytesIO
	from PIL import Image
	import IPython.display

	def showimage(cimg):
		img = Image.fromarray(cimg)
		b = BytesIO()
		img.save(b, format='png')

		IPython.display.display(IPython.display.Image(data=b.getvalue(), format='png', embed=True))
