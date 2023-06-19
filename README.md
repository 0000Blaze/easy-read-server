# Easy Read Server
- Application developed in Python Flask App with production engine as gunicorn
- Reverse Proxied with Apache and globally hosted URL with Ngrok
- OCR handled by Tesseract
- TTS handled by gtts package
- Focused mostly on preprocessing steps before OCR

## Steps of project
- Capture the image from the mobile platform through globally hosted url in ngrok
- Initially before binarization estimate the k parameter with trained liner regression model
- Perform binarization with local algorithm Sauvola ( initially compared performance with global method OTSU)
- Perform Segmentation
- Perform Noise Reduction to remove salt and pepper noise as well as marginal noise with the help of border proximity thresholding
- Perform Top down segmentation, enabling to understand article formated multi column text as well

## Easy Read mobile app
- https://github.com/0000Blaze/EasyRead
- Mobile client application developed in React Native Expo Framework
