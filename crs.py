{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red183\green111\blue179;\red23\green23\blue23;\red202\green202\blue202;
\red140\green211\blue254;\red194\green126\blue101;\red70\green137\blue204;\red89\green138\blue67;\red67\green192\blue160;
\red212\green214\blue154;\red167\green197\blue152;\red196\green83\blue86;\red205\green173\blue106;}
{\*\expandedcolortbl;;\cssrgb\c77255\c52549\c75294;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c61176\c86275\c99608;\cssrgb\c80784\c56863\c47059;\cssrgb\c33725\c61176\c83922;\cssrgb\c41569\c60000\c33333;\cssrgb\c30588\c78824\c69020;
\cssrgb\c86275\c86275\c66667;\cssrgb\c70980\c80784\c65882;\cssrgb\c81961\c41176\c41176;\cssrgb\c84314\c72941\c49020;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf4 \strokec4  models.sqlimodel \cf2 \strokec2 import\cf4 \strokec4  *\cb1 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  flask \cf2 \strokec2 import\cf4 \strokec4  Flask, request, url_for, render_template, redirect, make_response, request, session\cb1 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  flask_cors \cf2 \strokec2 import\cf4 \strokec4  CORS\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 app = Flask(\cf5 \strokec5 __name__\cf4 \strokec4 , \cf5 \strokec5 static_url_path\cf4 \strokec4 =\cf6 \strokec6 '/static'\cf4 \strokec4 , \cf5 \strokec5 static_folder\cf4 \strokec4 =\cf6 \strokec6 'static'\cf4 \strokec4 )\cb1 \
\
\cb3 app.config[\cf6 \strokec6 'DEBUG'\cf4 \strokec4 ] = \cf7 \strokec7 True\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 # Load default config and override config from an environment variable\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8 # You can also replace password with static password:  PASSWORD='pass!@#example'\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 app.config.update(\cf9 \strokec9 dict\cf4 \strokec4 (\cb1 \
\cb3     \cf5 \strokec5 SECRET_KEY\cf4 \strokec4 = \cf6 \strokec6 "woopie"\cf4 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 SESSION_COOKIE_HTTPONLY\cf4 \strokec4  = \cf7 \strokec7 True\cf4 \cb1 \strokec4 \
\cb3 ))\cb1 \
\
\cb3 allowed_origins = [\cb1 \
\cb3     \cf6 \strokec6 "http://127.0.0.1:5000"\cf4 \cb1 \strokec4 \
\cb3 ]\cb1 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 @app.route\cf4 \strokec4 (\cf6 \strokec6 "/"\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf10 \strokec10 start\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 return\cf4 \strokec4  render_template(\cf6 \strokec6 "index.html"\cf4 \strokec4 )\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 @app.route\cf4 \strokec4 (\cf6 \strokec6 "/login"\cf4 \strokec4 , \cf5 \strokec5 methods\cf4 \strokec4 =[\cf6 \strokec6 'GET'\cf4 \strokec4 , \cf6 \strokec6 'POST'\cf4 \strokec4 ])\cb1 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf10 \strokec10 login\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     sqli  = Classes()\cb1 \
\cb3     values = sqli.getUser(request.form[\cf6 \strokec6 'username'\cf4 \strokec4 ])\cb1 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4  values:\cb1 \
\cb3         \cf2 \strokec2 if\cf4 \strokec4  values[\cf11 \strokec11 0\cf4 \strokec4 ][\cf11 \strokec11 2\cf4 \strokec4 ] == request.form[\cf6 \strokec6 'password'\cf4 \strokec4 ]:\cb1 \
\cb3             session[\cf6 \strokec6 'userId'\cf4 \strokec4 ] = values[\cf11 \strokec11 0\cf4 \strokec4 ][\cf11 \strokec11 0\cf4 \strokec4 ]\cb1 \
\cb3             session[\cf6 \strokec6 'loggedin'\cf4 \strokec4 ] = \cf7 \strokec7 True\cf4 \cb1 \strokec4 \
\cb3             pref = sqli.getColor(values[\cf11 \strokec11 0\cf4 \strokec4 ][\cf11 \strokec11 0\cf4 \strokec4 ])\cb1 \
\cb3             color = pref[\cf11 \strokec11 0\cf4 \strokec4 ][\cf11 \strokec11 0\cf4 \strokec4 ]\cb1 \
\cb3             \cf2 \strokec2 return\cf4 \strokec4  redirect(url_for(\cf6 \strokec6 'xhr_get_info_stealing'\cf4 \strokec4 ))\cb1 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  render_template(\cf6 \strokec6 "index.html"\cf4 \strokec4 )\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 @app.route\cf4 \strokec4 (\cf6 \strokec6 "/confidential"\cf4 \strokec4 , \cf5 \strokec5 methods\cf4 \strokec4 =[\cf6 \strokec6 'GET'\cf4 \strokec4 , \cf6 \strokec6 'POST'\cf4 \strokec4 ])\cb1 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf10 \strokec10 xhr_get_info_stealing\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 if\cf4 \strokec4 (session[\cf6 \strokec6 'loggedin'\cf4 \strokec4 ]):\cb1 \
\cb3         response = make_response(render_template(\cf6 \strokec6 'loggedin.html'\cf4 \strokec4 ))\cb1 \
\cb3         response.headers.set(\cf6 \strokec6 "Access-Control-Allow-Origin"\cf4 \strokec4 , \cf6 \strokec6 ""\cf4 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  response\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 @app.errorhandler\cf4 \strokec4 (\cf11 \strokec11 404\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf10 \strokec10 page_not_found\cf4 \strokec4 (\cf5 \strokec5 e\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 return\cf4 \strokec4  render_template(\cf6 \strokec6 "404.html"\cf4 \strokec4 )\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf4 \strokec4  \cf5 \strokec5 __name__\cf4 \strokec4  == \cf6 \strokec6 "__main__"\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     cors = CORS(app, \cf5 \strokec5 resources\cf4 \strokec4 =\{\cf7 \strokec7 r\cf12 \strokec12 "/\cf13 \strokec13 *\cf12 \strokec12 "\cf4 \strokec4 : \{\cf6 \strokec6 "origins"\cf4 \strokec4 : \cf6 \strokec6 "*"\cf4 \strokec4 \}\})\cb1 \
\cb3     app.run(\cf5 \strokec5 host\cf4 \strokec4 =\cf6 \strokec6 '0.0.0.0'\cf4 \strokec4 )\cb1 \
\
\
}