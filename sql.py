{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red183\green111\blue179;\red23\green23\blue23;\red202\green202\blue202;
\red140\green211\blue254;\red194\green126\blue101;\red70\green137\blue204;\red212\green214\blue154;\red167\green197\blue152;
}
{\*\expandedcolortbl;;\cssrgb\c77255\c52549\c75294;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c61176\c86275\c99608;\cssrgb\c80784\c56863\c47059;\cssrgb\c33725\c61176\c83922;\cssrgb\c86275\c86275\c66667;\cssrgb\c70980\c80784\c65882;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf4 \strokec4  models.sqlimodel \cf2 \strokec2 import\cf4 \strokec4  *\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  flask \cf2 \strokec2 import\cf4 \strokec4  Flask, request, url_for, render_template, redirect\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4 app = Flask(\cf5 \strokec5 __name__\cf4 \strokec4 , \cf5 \strokec5 static_url_path\cf4 \strokec4 =\cf6 \strokec6 '/static'\cf4 \strokec4 , \cf5 \strokec5 static_folder\cf4 \strokec4 =\cf6 \strokec6 'static'\cf4 \strokec4 )\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4 app.config[\cf6 \strokec6 'DEBUG'\cf4 \strokec4 ] = \cf7 \strokec7 True\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 @app.route\cf4 \strokec4 (\cf6 \strokec6 "/"\cf4 \strokec4 , \cf5 \strokec5 methods\cf4 \strokec4 =[\cf6 \strokec6 'GET'\cf4 \strokec4 ])\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf8 \strokec8 home\cf4 \strokec4 ():\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     \cf2 \strokec2 return\cf4 \strokec4  render_template(\cf6 \strokec6 "index.html"\cf4 \strokec4 )\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 @app.route\cf4 \strokec4 (\cf6 \strokec6 "/home/<pageId>"\cf4 \strokec4 , \cf5 \strokec5 methods\cf4 \strokec4 =[\cf6 \strokec6 'GET'\cf4 \strokec4 ])\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf8 \strokec8 inject\cf4 \strokec4 (\cf5 \strokec5 pageId\cf4 \strokec4 ):\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     \cf2 \strokec2 if\cf4 \strokec4  pageId == \cf9 \strokec9 0\cf4 \strokec4 :\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         pageId = \cf9 \strokec9 1\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     sqli  = Pages()\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     values = sqli.getPage(pageId)\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf8 \strokec8 id\cf4 \strokec4       = values[\cf9 \strokec9 0\cf4 \strokec4 ][\cf9 \strokec9 0\cf4 \strokec4 ]\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     title   = values[\cf9 \strokec9 0\cf4 \strokec4 ][\cf9 \strokec9 1\cf4 \strokec4 ]\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     content = values[\cf9 \strokec9 0\cf4 \strokec4 ][\cf9 \strokec9 2\cf4 \strokec4 ]\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf2 \strokec2 return\cf4 \strokec4  render_template(\cf6 \strokec6 "index.html"\cf4 \strokec4 ,\cf5 \strokec5 title\cf4 \strokec4  = title, \cf5 \strokec5 content\cf4 \strokec4  = content, \cf5 \strokec5 id\cf4 \strokec4  = \cf8 \strokec8 id\cf4 \strokec4 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 @app.errorhandler\cf4 \strokec4 (\cf9 \strokec9 404\cf4 \strokec4 )\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf8 \strokec8 page_not_found\cf4 \strokec4 (\cf5 \strokec5 e\cf4 \strokec4 ):\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     \cf2 \strokec2 return\cf4 \strokec4  render_template(\cf6 \strokec6 "404.html"\cf4 \strokec4 )\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf4 \strokec4  \cf5 \strokec5 __name__\cf4 \strokec4  == \cf6 \strokec6 "__main__"\cf4 \strokec4 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     app.run(\cf5 \strokec5 host\cf4 \strokec4 =\cf6 \strokec6 '0.0.0.0'\cf4 \strokec4 )\cf4 \cb1 \strokec4 \
\
}