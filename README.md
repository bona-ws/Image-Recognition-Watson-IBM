# Image recognition application with Watson IBM

What i have done here :

- Create a web app
- Train a model in IBM watson
- Connect the web app with watson API
- Run locally and play with it.

## How to run this app

Change the host address in server.py with your local IP.

```groovy
 app.run(host='192.168.43.71', port=port)
```

Make sure you already install all requirement list in requirement.txt file.

```groovy
Flask==1.0.3
Flask-WTF==0.14.2
ibm-watson==3.0.4
python-dotenv==0.10.3
```

Just it ! Now open your Terminal in your app path, and run :

```groovy
python server.py
```

## Try it online

If you just wanna try the app without install it, you can visit : [My watson web app](https://bona-wibowo-computer-vision-app.mybluemix.net/)
