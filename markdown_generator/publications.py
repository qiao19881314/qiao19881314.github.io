
# coding: utf-8

# # Publications markdown generator for qiao19881314
# 
# Takes a TSV of publications with metadata and converts them for use with [qiao19881314.github.io](qiao19881314.github.io). This is an interactive Jupyter notebook, with the core python code in publications.py. Run either from the `markdown_generator` folder after replacing `publications.tsv` with one that fits your format.
# 
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard TSV format and citation style.
# 

# ## Data format
# 
# The TSV needs to have the following columns: pub_date, title, venue, excerpt, citation, site_url, and paper_url, with a header at the top. 
# 
# - `excerpt` and `paper_url` can be blank, but the others must have values. 
# - `pub_date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`


# ## Import pandas
# 
# We are using the very handy pandas library for dataframes.

# In[2]:

import pandas as pd


# ## Import TSV
# 
# Pandas makes this easy with the read_csv function. We are using a TSV, so we specify the separator as a tab, or `\t`.
# 
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this kind of data and comma-separated values can get messed up. However, you can modify the import statement, as pandas also has read_excel(), read_json(), and others.

# In[3]:
import os
os.chdir("markdown_generator")
publications = pd.read_csv("publications.tsv", sep="\t", header=0)


# ## Escape special characters
# 
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

# In[4]:

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


# ## Creating the markdown files
# 
# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then does the description for the individual page. If you don't want something to appear (like the "Recommended citation")

# In[5]:

import os
for row, item in publications.iterrows():
    
    md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"
    # html_filename = str(item.pub_date) + "-" + item.url_slug
    html_filename = item.url_slug  # paper_name
    year = item.pub_date[:4]
    
    ## YAML variables
    
    md = "---\ntitle: \""   + item.title + '"\n'
    
    md += """collection: publications"""
    
    # md += """\npermalink: /publication/""" + html_filename
    md += """\npermalink: /files/""" + html_filename
    
    if len(str(item.excerpt)) > 5:
        md += "\nexcerpt: '" + html_escape(item.excerpt) + "'"
    
    md += "\ndate: " + str(item.pub_date) 
    
    md += "\nvenue: '" + html_escape(item.venue) + "'"
    
    if len(str(item.paper_url)) > 5:
        md += "\npaperurl: '" + item.paper_url + "'"
    
    md += "\ncitation: '" + html_escape(item.citation) + "'"
    
    md += "\n---"
    
    ## Markdown description for individual page
    
    if len(str(item.paper_url)) > 5:
        md += "\n\n<a href='" + item.paper_url + "'>Download paper here</a>\n" 
        
    if len(str(item.excerpt)) > 5:
        md += "\n" + html_escape(item.excerpt) + "\n"
        
    md += "\nRecommended citation: " + item.citation
    md_filename = os.path.basename(os.path.splitext(html_filename)[0]+".md")  # md和pdf保持一直
       
    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)


#  Invalid argument @ dir_s_mkdir - H:/academicpages.github.io-master/_site/publication/2019/3/4-http: (Errno::EINVAL)
#  是因为我上传了论文信息后产生的， 应该是publications.tsv中有文字不是acsii编码
'''
应该是url_slug出错， qiao1314更改为正常的academicpages
http://qiao1314.github.io/files/paper1.pdf
http://qiao1314.github.io/files/paper2.pdf
http://qiao1314.github.io/files/paper3.pdf
http://qiao1314.github.io/files/paper4.pdf
http://qiao1314.github.io/files/paper5.pdf
http://qiao1314.github.io/files/paper6.pdf
http://qiao1314.github.io/files/paper7.pdf
http://qiao1314.github.io/files/paper8.pdf
http://qiao1314.github.io/files/paper9.pdf
http://qiao1314.github.io/files/paper10.pdf
http://qiao1314.github.io/files/paper11.pdf
http://qiao1314.github.io/files/paper12.pdf
http://qiao1314.github.io/files/paper13.pdf
http://qiao1314.github.io/files/paper14.pdf
http://qiao1314.github.io/files/paper15.pdf
http://qiao1314.github.io/files/paper16.pdf
http://qiao1314.github.io/files/paper17.pdf
http://qiao1314.github.io/files/paper18.pdf
http://qiao1314.github.io/files/paper19.pdf
http://qiao1314.github.io/files/paper20.pdf

http://academicpages.github.io/files/paper1.pdf
http://academicpages.github.io/files/paper2.pdf
http://academicpages.github.io/files/paper3.pdf
http://academicpages.github.io/files/paper4.pdf
http://academicpages.github.io/files/paper5.pdf
http://academicpages.github.io/files/paper6.pdf
http://academicpages.github.io/files/paper7.pdf
http://academicpages.github.io/files/paper8.pdf
http://academicpages.github.io/files/paper9.pdf
http://academicpages.github.io/files/paper10.pdf
http://academicpages.github.io/files/paper11.pdf
http://academicpages.github.io/files/paper12.pdf
http://academicpages.github.io/files/paper13.pdf
http://academicpages.github.io/files/paper14.pdf
http://academicpages.github.io/files/paper15.pdf
http://academicpages.github.io/files/paper16.pdf
http://academicpages.github.io/files/paper17.pdf
http://academicpages.github.io/files/paper18.pdf
http://academicpages.github.io/files/paper19.pdf
http://academicpages.github.io/files/paper20.pdf

文件地址错误，导致pdf链接打不开
'''