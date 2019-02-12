# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 16:19:13 2019

@author: lxx
"""

annotate_begin = "<annotation>"
annotate_end = "</annotation>"


out_template = \
"""
\t<folder>JPEGImages</folder>
\t<filename>{}</filename>
\t<path>F:\Bolts\JPEGImages\{}</path>
\t<source>
\t	<database>Unknown</database>
\t</source>
\t<size>
\t	<width>2048</width>
\t	<height>2048</height>
\t	<depth>3</depth>
\t</size>
\t<segmented>0</segmented>"""

object_template = \
"""
\t<object>
\t	<name>{}</name>
\t	<pose>Unspecified</pose>
\t	<truncated>0</truncated>
\t	<difficult>0</difficult>
\t	<bndbox>
\t		<xmin>{}</xmin>
\t		<ymin>{}</ymin>
\t		<xmax>{}</xmax>
\t		<ymax>{}</ymax>
\t	</bndbox>
\t</object>"""

#print(out_template)

def populate_object(template, classname, xmin, xmax, ymin, ymax):
    return template.format(classname, xmin, xmax, ymin, ymax)

def populate_header(template, filename):
    return template.format(filename, filename)

def begin_xml():
      return annotate_begin

def end_xml():
      return annotate_end

def write_xml(filename,classname,xmin,ymin,xmax,ymax):
    with open(filename + ".xml", mode="w") as f:
        f.write(begin_xml())
        f.write(populate_header(out_template, filename+".jpg"))
        for i in range(5):
            f.write(populate_object(object_template, classname, xmin,ymin,xmax,ymax))
        f.write("\n"+end_xml())