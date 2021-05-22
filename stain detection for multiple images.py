#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[2]:


import os
os.chdir("C:\\Users\\My PC\\CoVictory=Dust detection\\images")


# In[3]:


orig_imgs=[]
for dirname, dirnames, filenames in os.walk("C:\\Users\\My PC\\CoVictory=Dust detection\\images"):
  for filename in filenames:
    if filename.endswith('.jpeg'):
       orig_imgs.append(filename)
orig_imgs


# In[33]:


# This will import Image and ImageEnhance modules
from PIL import Image, ImageEnhance
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
import os
import argparse

for i in range(0,len(orig_imgs)):
    # Opening Image
    im = Image.open(orig_imgs[i])
    
    # Creating object of Color class
    im3 = ImageEnhance.Color(im)
    
    # showing resultant image
    x=im3.enhance(5.0)
    x.save(r"contrast{0}.jpeg".format(i+1))
    


# In[35]:


contrast_imgs=[]
for dirname, dirnames, filenames in os.walk("C:\\Users\\My PC\\CoVictory=Dust detection\\images"):
  for filename in filenames:
    if filename.endswith('.jpeg') and filename.startswith("contrast"):
       contrast_imgs.append(filename)
contrast_imgs


# In[36]:


#to sort the array in terms of length
contrast_imgs.sort(key=len)
print(contrast_imgs)


# In[ ]:


"""for j in contrast_imgs:
    class DetectColor:
        #RGB to Hex convertion
        def RGB_to_HEX(self,color):
            return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))
        
        #reading image in RGB colour space
        def get_image(self,image_path):
            image = cv2.imread(image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            return image
        
        #image=whos colours we want to extract
        #no_of_colours= the no of colours we want to extract from the image
        #show_chart=boolian value which decides on whther to show the pichart or no
        def get_colors(self,image, number_of_colors, show_chart):
            image = image.reshape(image.shape[0]*image.shape[1], 3)
            
            
            #KMeans algorithm creates clusters based on the supplied count of clusters.
            #finding clusters of colours that mostly appearing
            clf = KMeans(n_clusters = number_of_colors)
        
            #to fit the image
            labels = clf.fit_predict(image)
            counts = Counter(labels)
        
            # sort to ensure correct color percentage
            #counts=to count the no of labels
            counts = dict(sorted(counts.items()))
            #print(counts)
            #center_colors=colors in RBG format
            center_colors = clf.cluster_centers_
            #print(center_colors)
            # We get rgb colors by iterating through the keys
            rgb_colors = [center_colors[i] for i in counts.keys()]
            #print(rgb_colors)
            hex_colors = [self.RGB_to_HEX(rgb_colors[i]) for i in counts.keys()]
            
            if (show_chart):
                plt.figure(figsize = (6, 6))
                plt.pie(counts.values(), labels = hex_colors, colors = hex_colors,wedgeprops={"edgecolor":"0",'linewidth': 1})
                #print(counts.values())
                total=sum(counts.values())
                areas_in_percent=[]
                for i in counts.values():
                    area=(i/total)*100
                    #print(area)
                    areas_in_percent.append(area)
                print("areas of each on percentage",areas_in_percent)
            stains=0
            for i in areas_in_percent:
                if i > 2.66 and i < 15:
                    stains=stains+i
            print("stains",stains)

            return rgb_colors

        
"""    


# In[37]:


#link=https://towardsdatascience.com/color-identification-in-images-machine-learning-application-b26e770c4c71

total_stains=[]
class DetectColor:
    #RGB to Hex convertion
    def RGB_to_HEX(self,color):
        return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))
    
    #reading image in RGB colour space
    def get_image(self,image_path):
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image

    
    #image=whos colours we want to extract
    #no_of_colours= the no of colours we want to extract from the image
    #show_chart=boolian value which decides on whther to show the pichart or no
    def get_colors(self,image, number_of_colors, show_chart):
        image = image.reshape(image.shape[0]*image.shape[1], 3)
        
        #KMeans algorithm creates clusters based on the supplied count of clusters.
        #finding clusters of colours that mostly appearing
        clf = KMeans(n_clusters = number_of_colors)
        
        #to fit the image
        labels = clf.fit_predict(image)
        counts = Counter(labels)
        
        # sort to ensure correct color percentage
        #counts=to count the no of labels
        counts = dict(sorted(counts.items()))
        print(counts)
        #center_colors=colors in RBG format
        center_colors = clf.cluster_centers_
        print(center_colors)
        # We get rgb colors by iterating through the keys
        rgb_colors = [center_colors[i] for i in counts.keys()]
        print(rgb_colors)
        hex_colors = [self.RGB_to_HEX(rgb_colors[i]) for i in counts.keys()]
        
        if (show_chart):
            plt.figure(figsize = (6, 6))
            plt.pie(counts.values(), labels = hex_colors, colors = hex_colors,wedgeprops={"edgecolor":"0",'linewidth': 1})
            print(counts.values())
            total=sum(counts.values())
            areas_in_percent=[]
            for i in counts.values():
                area=(i/total)*100
                #print(area)
                areas_in_percent.append(area)
            print("areas of each on percentage",areas_in_percent)
        stains=0
        for i in areas_in_percent:
            if i > 2.66 and i < 15:
                stains=stains+i
        print("stains",stains)
        total_stains.append(stains)

        return rgb_colors
        


# In[38]:


if __name__ == "__main__":
    #img = 'crop.jpeg'
    obj = DetectColor()
    for i in contrast_imgs:
        color = obj.get_colors(obj.get_image(i),4 ,True)


# In[39]:


total_stains


# In[42]:


final=[]
for i in total_stains:
    if i>0 and i<4.5:
        final.append("CLEAN")
            
    if i>4.5 and i<14:
        final.append("REUSABLE BY WASH")
    if i>14:
        final.append("DISCARD")
print(final)


# In[ ]:




