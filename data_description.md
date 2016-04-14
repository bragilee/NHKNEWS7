**lfw**
	
	labeled faces wild dataset.
	it contains both raw images and deepfunneled images.

**nhknews_day**

	nhknews dataset.
	it contains 111 categories with 2932 images.
	images are extracted according to shot ID.(stop at shotXX)
	images numbers range from 1 to 267, mean number is 26.

**nhknews_shot**

	nhknews dataset.
	it contains 111 categories.
	images are extracted according to shot ID frame. (stop at shotXX_YYY)
	
**nhknews_track**

	nhknews dataset.
	it contains 111 categories.
	images are extracted according to shot ID with number with track. (stop at shotXX_YYY_TrackZ)
	
	
**In each directory**

* The "raw" folder in each kind of dataset contains raw images.
* The "pairs.txt" file in each kind of dataset is for accuracy evaluation.
* The "nhknews_XXX_vgg_labels.csv" is for acuracy evaluation of VGG feature, specifically is used with "representation" file. 