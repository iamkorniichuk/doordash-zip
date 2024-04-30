# Install

## Appium

You need to have `npm` and `Node.js` to execute next command:

```bash
npm i --location=global appium
```

To check valid Appium's installation run next command:

```bash
appium --version
```

## Project

Clone this repository and go to the directory:

```bash
git clone https://github.com/iamkorniichuk/doordash-zip.git
cd doordash-zip
```

Set up virtual environmnent (Use your casual flow). For example:

```bash
virtualenv venv
./venv/Scripts/activate
pip install -r requirements.txt
```

## Device Config

Open `main.py` into your editor and change config to your device's:

```python
config={
    "platformVersion": "13.0",
    "deviceName": "Pixel 4A",
}
```

## USB Debugging

To enable USB Debugging follow these [steps](https://www.asus.com/support/faq/1046846/#:~:text=Steps%20required%20to%20enable%20USB%20cable%20connection%20vary%20depending%20on%20the%20brand%20of%20your%20device.)

## Proxy

If your device location other than US, use **WIFI proxy** as described below:

<video width="300" controls>
    <source src="/proxy.mp4" type="video/mp4">
</video>

Hostname: `us-px.oxylabs.io`
Port: `10000`

## Run

Just run `main.py` using any of your tools
